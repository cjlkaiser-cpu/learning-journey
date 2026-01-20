---
id: pytorch
name: PyTorch
category: IA
level: solid
---

# PyTorch

Framework de deep learning desarrollado por Meta/Facebook. Usado para implementar transformers from scratch.

## Primer uso

**Proyecto:** GPT Bach WTC (20 ene 2026)
**Contexto:** Transformer architecture completa (4.29M params)

## Conceptos Aprendidos

### Tensor Operations
```python
import torch

# Crear tensors
x = torch.tensor([[1, 2], [3, 4]])
x = torch.zeros(2, 3)
x = torch.randn(2, 3)

# Operaciones
y = x.transpose(0, 1)
z = torch.matmul(x, y)
```

### Autograd
```python
x = torch.randn(3, requires_grad=True)
y = x * 2
y.backward(torch.ones_like(y))
print(x.grad)  # dy/dx
```

### Neural Networks (nn.Module)
```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(256, 512)

    def forward(self, x):
        return self.linear(x)

model = MyModel()
output = model(input_tensor)
```

### Transformer Components

#### Multi-Head Attention
```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        self.d_head = d_model // n_heads
        self.n_heads = n_heads

        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        # Scaled dot-product attention
        # Implementación completa en GPT Bach WTC
```

#### Layer Normalization
```python
# Pre-norm vs Post-norm
# Pre-norm (mejor para deep models):
x = x + self_attention(layer_norm(x))

# Post-norm (original transformer):
x = layer_norm(x + self_attention(x))
```

### Training Loop
```python
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=3e-4,
    betas=(0.9, 0.95),
    weight_decay=0.01
)

scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
    optimizer,
    T_max=epochs
)

for epoch in range(epochs):
    for batch in dataloader:
        # Forward
        output = model(batch['input'])
        loss = criterion(output, batch['target'])

        # Backward
        optimizer.zero_grad()
        loss.backward()

        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(
            model.parameters(),
            max_norm=1.0
        )

        optimizer.step()

    scheduler.step()
```

### Model Saving/Loading
```python
# Save
torch.save({
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'epoch': epoch,
    'loss': loss
}, 'checkpoint.pt')

# Load
checkpoint = torch.load('checkpoint.pt', weights_only=False)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
```

### Generation (Autoregressive)
```python
@torch.no_grad()
def generate(model, start_tokens, max_new_tokens=100):
    model.eval()
    tokens = start_tokens

    for _ in range(max_new_tokens):
        # Get predictions for last token
        logits = model(tokens)[:, -1, :]

        # Sample from distribution
        probs = F.softmax(logits / temperature, dim=-1)
        next_token = torch.multinomial(probs, num_samples=1)

        # Append to sequence
        tokens = torch.cat([tokens, next_token], dim=1)

    return tokens
```

## Best Practices Aprendidas

### Optimización
- **AdamW > Adam** para transformers
- **Gradient clipping** esencial (max_norm=1.0)
- **Learning rate warmup** (5 epochs) + cosine decay
- **Weight tying** entre embeddings y output projection

### Arquitectura
- **Pre-norm** mejor que post-norm para deep models
- **Causal masking** crítico para autoregresivo
- **Dropout 0.1** estándar para transformers
- **GELU** > ReLU para transformers

### Training
- **Checkpointing** cada N epochs
- **Early stopping** con patience
- **Validation** cada epoch
- **TensorBoard** para monitoreo

### Memory Management
```python
# Clear cache
torch.cuda.empty_cache()

# Gradient accumulation para grandes modelos
for i, batch in enumerate(dataloader):
    loss = model(batch) / accumulation_steps
    loss.backward()

    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

## CPU vs GPU

**CPU:**
- ✅ Viable para modelos <10M params
- ✅ Suficiente para prototyping
- ⏱️ ~2h para 100 epochs (4.29M params)

**GPU:**
- ⚡ 10-50x más rápido
- 💰 Requiere hardware específico
- 🔥 Mejor para producción

## Recursos

- **Documentación:** https://pytorch.org/docs/
- **Tutorials:** https://pytorch.org/tutorials/
- **"Attention Is All You Need"** (Vaswani et al., 2017)
- **GPT Bach WTC** - Implementación completa de transformer

## Proyectos

- [GPT Bach WTC](../projects/gpt-bach-wtc.md) - Transformer from scratch

---

**Estado:** Solid - Transformer completo implementado
**Próximo:** Fine-tuning, arquitecturas más complejas
