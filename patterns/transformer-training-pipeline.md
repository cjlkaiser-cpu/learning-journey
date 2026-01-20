---
id: transformer-training-pipeline
name: Transformer Training Pipeline
problem: Entrenar modelos transformer desde cero con buenas prácticas
flow: [pytorch, gradio, matplotlib, numpy]
---

# Transformer Training Pipeline

Pipeline completo para entrenar modelos transformer from scratch. Probado en GPT Bach WTC (4.29M params, 100 epochs, 99% de calidad Bach).

## Problem

Entrenar un transformer desde cero requiere:
- Arquitectura correcta (attention, feed-forward, normalization)
- Training loop robusto (optimizer, scheduler, gradient clipping)
- Data augmentation apropiada
- Early stopping inteligente
- Checkpointing y monitoreo
- Generation inference
- Deployment a producción

## Solution

### 1. Tokenización Estructurada

**Crítico para dominios específicos (música, código, etc.)**

```python
# Vocabulario con estructura fija
class Vocabulary:
    SPECIAL = ['<PAD>', '<START>', '<END>', '<BAR>', '<REST>']
    NOTES = ['C4', 'D4', 'E4', ...]  # Domain-specific
    VOICES = ['<VOICE:1>', '<VOICE:2>', ...]
    DURATIONS = ['<DUR:1.0>', '<DUR:0.5>', ...]
    TIME_DELTAS = ['<TIME:+0.25>', '<TIME:+0.5>', ...]

# Orden fijo garantizado
# Ejemplo: <NOTE:C4> <VOICE:1> <DUR:1.0> <TIME:+0.25>
```

**Ventajas:**
- Previene errores sintácticos
- Más fácil de decodificar
- Validación estructural en tests

### 2. Arquitectura Transformer

```python
class MusicGPT(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int = 256,
        n_heads: int = 8,
        n_layers: int = 4,
        d_ff: int = 1024,
        dropout: float = 0.1,
        max_seq_len: int = 4096
    ):
        super().__init__()

        # Embeddings
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.pos_enc = RelativePositionalEncoding(d_model, max_seq_len)
        self.bar_pos_enc = BarPositionalEncoding(d_model)

        # Transformer blocks
        self.blocks = nn.ModuleList([
            TransformerBlock(d_model, n_heads, d_ff, dropout)
            for _ in range(n_layers)
        ])

        # Output
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

        # Weight tying
        self.head.weight = self.token_emb.weight
```

**Decisiones clave:**
- **Pre-norm** > post-norm (mejor para deep models)
- **Relative positional encoding** > sinusoidal (aprende patrones)
- **Weight tying** reduce parámetros ~20%
- **GELU** > ReLU para transformers

### 3. Data Augmentation Escalonada

```python
class StagedAugmentation:
    def get_params(self, epoch: int):
        if epoch < 10:
            # Learn base patterns first
            return {
                'apply': False,
                'pitch_shift': 0,
                'tempo_scale': 1.0
            }
        elif epoch < 30:
            # Light augmentation
            return {
                'apply': random() < 0.5,
                'pitch_shift': choice([-1, 0, 1]),
                'tempo_scale': uniform(0.95, 1.05)
            }
        else:
            # Heavy augmentation
            return {
                'apply': random() < 0.8,
                'pitch_shift': choice([-2, -1, 0, 1, 2]),
                'tempo_scale': uniform(0.85, 1.15)
            }
```

**Estrategia:**
1. Epochs 0-9: Sin augmentation (aprender base)
2. Epochs 10-29: Light (50% prob)
3. Epochs 30+: Heavy (80% prob)

**Evita overfitting sin comprometer aprendizaje inicial.**

### 4. Musical Early Stopping

```python
class MusicalEarlyStopping:
    def __init__(
        self,
        patience: int = 15,
        loss_weight: float = 0.3,
        musical_weight: float = 0.7
    ):
        self.patience = patience
        self.loss_weight = loss_weight
        self.musical_weight = musical_weight

    def __call__(self, val_loss, musical_metrics):
        # Combined score
        loss_component = 1.0 - (val_loss / self.baseline_loss)
        musical_component = musical_metrics['overall_score'] / 100

        score = (
            self.loss_weight * loss_component +
            self.musical_weight * musical_component
        )

        # Track best
        if score > self.best_score:
            self.best_score = score
            self.counter = 0
            return False  # Don't stop

        self.counter += 1
        return self.counter >= self.patience
```

**Idea:** Loss bajo ≠ calidad musical alta. Combinar ambos.

### 5. Training Loop

```python
def train_epoch(model, dataloader, optimizer, scheduler, augmenter):
    model.train()

    for batch in dataloader:
        # Augment data
        if augmenter:
            batch = augmenter.augment(batch, epoch)

        # Forward
        input_ids = batch['input_ids']
        target_ids = batch['target_ids']
        attention_mask = batch['attention_mask']

        logits = model(input_ids, attention_mask=attention_mask)

        # Loss (ignore padding)
        loss = F.cross_entropy(
            logits.view(-1, vocab_size),
            target_ids.view(-1),
            ignore_index=pad_token_id
        )

        # Backward
        optimizer.zero_grad()
        loss.backward()

        # Gradient clipping (CRÍTICO)
        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        optimizer.step()

    scheduler.step()
```

### 6. Optimizer & Scheduler

```python
# AdamW (mejor que Adam para transformers)
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=3e-4,
    betas=(0.9, 0.95),  # β2=0.95 para transformers
    weight_decay=0.01
)

# Warmup + Cosine decay
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
    optimizer,
    T_max=epochs,
    eta_min=3e-5
)

# Warmup manual (primeros 5 epochs)
for epoch in range(warmup_epochs):
    for param_group in optimizer.param_groups:
        param_group['lr'] = base_lr * (epoch + 1) / warmup_epochs
```

### 7. Generation (Autoregressive)

```python
@torch.no_grad()
def generate(
    model,
    start_tokens: torch.Tensor,
    max_new_tokens: int = 1000,
    temperature: float = 1.0,
    top_k: int = 50,
    top_p: float = 0.9
) -> torch.Tensor:
    model.eval()
    tokens = start_tokens

    for _ in range(max_new_tokens):
        # Get predictions
        logits = model(tokens)[:, -1, :]

        # Temperature scaling
        logits = logits / temperature

        # Top-k filtering
        if top_k > 0:
            indices_to_remove = logits < torch.topk(logits, top_k)[0][..., -1, None]
            logits[indices_to_remove] = float('-inf')

        # Top-p (nucleus) filtering
        if top_p < 1.0:
            sorted_logits, sorted_indices = torch.sort(logits, descending=True)
            cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
            sorted_indices_to_remove = cumulative_probs > top_p
            sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
            sorted_indices_to_remove[..., 0] = 0
            indices_to_remove = sorted_indices[sorted_indices_to_remove]
            logits[indices_to_remove] = float('-inf')

        # Sample
        probs = F.softmax(logits, dim=-1)
        next_token = torch.multinomial(probs, num_samples=1)

        # Append
        tokens = torch.cat([tokens, next_token], dim=1)

        # Check for END token
        if next_token.item() == end_token_id:
            break

    return tokens
```

### 8. Checkpointing

```python
def save_checkpoint(
    model,
    optimizer,
    scheduler,
    epoch,
    val_loss,
    path: Path
):
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict(),
        'epoch': epoch,
        'val_loss': val_loss
    }, path)

# Save strategy
# 1. Best model (val_loss)
# 2. Best musical score (combined score)
# 3. Every N epochs
# 4. Last checkpoint
```

### 9. Monitoring (TensorBoard)

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('runs/experiment')

# Log scalars
writer.add_scalar('Loss/train', train_loss, epoch)
writer.add_scalar('Loss/val', val_loss, epoch)
writer.add_scalar('LR', lr, epoch)

# Log metrics
writer.add_scalar('Metrics/out_of_key', out_of_key_ratio, epoch)
writer.add_scalar('Metrics/interval_entropy', interval_entropy, epoch)

# Log generated samples
writer.add_text('Samples/epoch_10', generated_text, 10)

# Log model graph
writer.add_graph(model, sample_input)
```

### 10. Deployment (Gradio)

```python
import gradio as gr

def create_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Model Generator")

        with gr.Row():
            temperature = gr.Slider(0.1, 2.0, 1.0)
            top_k = gr.Slider(10, 100, 50)

            generate_btn = gr.Button("Generate")

        output = gr.Image()

        generate_btn.click(
            fn=generate_fn,
            inputs=[temperature, top_k],
            outputs=[output]
        )

    return app

app = create_interface()
app.launch()
```

## Resultados (GPT Bach WTC)

- **100 epochs** (~2h CPU)
- **Best val loss:** 1.9693 (epoch 21)
- **Musical quality:** 59.55/100 (99% de Bach!)
- **Out-of-key:** 6.92% (mejor que Bach original 11.99%)
- **Parámetros:** 4.29M
- **Inference:** ~15-30s para 1000 tokens

## Best Practices

### DO ✅
- Gradient clipping (max_norm=1.0)
- Learning rate warmup (5 epochs)
- Pre-norm architecture
- Weight tying
- AdamW optimizer
- Cosine LR decay
- Early stopping con patience
- Checkpointing cada N epochs
- TensorBoard logging

### DON'T ❌
- Post-norm para deep models
- Adam sin weight decay
- Constant learning rate
- Train hasta 100% convergencia (overfitting)
- Confiar solo en val_loss
- Ignorar gradient norms
- No hacer checkpoints intermedios

## Recursos

- **"Attention Is All You Need"** (Vaswani et al., 2017)
- **"Language Models are Few-Shot Learners"** (GPT-3 paper)
- **Andrej Karpathy - nanoGPT:** https://github.com/karpathy/nanoGPT
- **HuggingFace Transformers:** https://huggingface.co/docs/transformers

## Proyectos

- [GPT Bach WTC](../projects/gpt-bach-wtc.md) - Implementación completa

---

**Aplicable a:** Música, código, matemáticas, cualquier dominio con estructura
**Escalabilidad:** Probado 4M-10M params en CPU, escalable a GPUs para >100M
