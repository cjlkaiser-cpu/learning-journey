---
id: gradio
name: Gradio
category: Frontend
level: solid
---

# Gradio

Framework de Python para crear interfaces web interactivas para modelos de ML/IA. Alternativa simple a Streamlit/Dash.

## Primer uso

**Proyecto:** GPT Bach WTC (20 ene 2026)
**Contexto:** Web interface para generación musical con transformer

## Conceptos Básicos

### App Simple
```python
import gradio as gr

def greet(name):
    return f"Hello {name}!"

app = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text"
)

app.launch()
```

### Components Usados

#### Inputs
```python
# Sliders
temperature = gr.Slider(
    minimum=0.1,
    maximum=2.0,
    value=1.0,
    step=0.1,
    label="Temperature"
)

# Number inputs
max_tokens = gr.Number(
    value=1024,
    label="Max Tokens",
    minimum=100,
    maximum=4000
)

# Text
seed = gr.Number(
    value=None,
    label="Seed (optional)"
)
```

#### Outputs
```python
# Image
piano_roll = gr.Image(
    label="Piano Roll",
    type="filepath"
)

# HTML (custom rendering)
metrics = gr.HTML(
    label="Musical Metrics"
)

# File download
midi_file = gr.File(
    label="📥 Download MIDI"
)
```

### Layout con Blocks
```python
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# My App")

    with gr.Row():
        with gr.Column(scale=1):
            # Controls
            slider = gr.Slider(...)
            button = gr.Button("Generate")

        with gr.Column(scale=2):
            # Output
            output = gr.Image(...)

    # Connect
    button.click(
        fn=generate_fn,
        inputs=[slider],
        outputs=[output]
    )
```

### Progress Tracking
```python
def generate_music(
    temperature: float,
    progress=gr.Progress()
) -> str:
    progress(0, desc="🎵 Starting...")

    # ... process ...
    progress(0.3, desc="🎹 Generating tokens...")

    # ... more processing ...
    progress(0.7, desc="📊 Computing metrics...")

    progress(1.0, desc="✅ Complete!")
    return result
```

### Custom Theme
```python
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="purple",
    neutral_hue="slate"
)

app = gr.Blocks(theme=theme)
```

## Caso de Uso: GPT Bach WTC

### Arquitectura Completa
```python
def create_interface():
    with gr.Blocks(theme=gr.themes.Soft()) as app:
        gr.Markdown("""
        # 🎵 Bach WTC Generator
        Generate Bach-style preludes with AI
        """)

        with gr.Row():
            # Left: Controls
            with gr.Column(scale=1):
                temperature = gr.Slider(0.1, 2.0, 1.0)
                top_k = gr.Slider(10, 100, 50)
                top_p = gr.Slider(0.7, 0.98, 0.9)
                max_tokens = gr.Number(1024, minimum=100)
                seed = gr.Number(None, label="Seed")

                generate_btn = gr.Button(
                    "🎵 Generate",
                    variant="primary"
                )

                status = gr.Markdown("Ready!")

            # Right: Output
            with gr.Column(scale=2):
                piano_roll = gr.Image(label="Piano Roll")
                metrics = gr.HTML(label="Metrics")

                with gr.Row():
                    midi = gr.File(label="MIDI")
                    musicxml = gr.File(label="MusicXML")

        # Connect button
        generate_btn.click(
            fn=generate_music,
            inputs=[temperature, top_k, top_p, max_tokens, seed],
            outputs=[piano_roll, metrics, midi, musicxml, status]
        )

    return app
```

### Generation Function
```python
def generate_music(
    temperature: float,
    top_k: int,
    top_p: float,
    max_tokens: int,
    seed: Optional[int],
    progress=gr.Progress()
) -> Tuple[str, str, str, str, str]:
    """Generate music and return all outputs."""

    # Set seed
    if seed is not None:
        torch.manual_seed(seed)

    progress(0.1, desc="🎹 Generating tokens...")

    # Generate tokens
    with torch.no_grad():
        tokens = model.generate(
            start_tokens,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
        )

    progress(0.5, desc="🎼 Creating score...")

    # Decode to music
    events = tokenizer.decode(tokens)
    score = events_to_score(events)

    progress(0.8, desc="📊 Computing metrics...")

    # Compute metrics
    metrics = analyzer.compute_metrics(events)
    metrics_html = create_metrics_html(metrics)

    # Create visualization
    piano_roll_img = create_piano_roll(events)

    progress(0.95, desc="💾 Exporting files...")

    # Export files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    midi_path = f"outputs/generated_{timestamp}.mid"
    xml_path = f"outputs/generated_{timestamp}.musicxml"

    score.write('midi', fp=midi_path)
    score.write('musicxml', fp=xml_path)

    progress(1.0, desc="✅ Complete!")

    status = f"✅ Generated {len(events)} events successfully!"

    return (
        piano_roll_img,
        metrics_html,
        midi_path,
        xml_path,
        status
    )
```

### Custom HTML Output
```python
def create_metrics_html(metrics: Dict) -> str:
    """Create formatted HTML for metrics display."""
    return f"""
    <div style="font-family: monospace;">
        <h3>📊 Musical Metrics</h3>
        <table>
            <tr>
                <td><b>Overall Score:</b></td>
                <td>{metrics['overall_score']:.1f}/100</td>
            </tr>
            <tr>
                <td><b>Out-of-key:</b></td>
                <td>{metrics['out_of_key_ratio']:.1%}</td>
            </tr>
            <tr>
                <td><b>Interval Entropy:</b></td>
                <td>{metrics['interval_entropy']:.2f}</td>
            </tr>
        </table>
    </div>
    """
```

## Deployment

### Local
```python
app.launch(
    server_name="0.0.0.0",  # Accept external connections
    server_port=7860,
    share=False  # No public URL
)
```

### Public URL (Temporary)
```python
app.launch(share=True)
# Genera URL pública temporal (72h)
# https://xyz123.gradio.live
```

### HuggingFace Spaces
```yaml
# README.md
---
title: My App
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
---
```

Deployment automático al hacer `git push`.

## Ventajas vs Otras Opciones

**vs Streamlit:**
- ✅ Mejor para ML/IA (progress tracking, file uploads)
- ✅ Más componentes out-of-the-box
- ✅ Deployment más fácil (HuggingFace Spaces)
- ❌ Menos flexible para custom layouts

**vs Dash/Plotly:**
- ✅ Muchísimo más simple (menos boilerplate)
- ✅ Mejor para prototipado rápido
- ❌ Menos control sobre UI

**vs FastAPI + React:**
- ✅ 10x más rápido de desarrollar
- ✅ No requiere frontend separado
- ❌ Menos personalizable

## Limitaciones

- UI limitada (no tan customizable como React)
- Menos componentes avanzados que Streamlit
- Puede ser lento con muchos usuarios concurrentes
- No hay state persistence built-in

## Recursos

- **Documentación:** https://gradio.app/docs/
- **Playground:** https://gradio.app/playground/
- **HuggingFace Spaces:** https://huggingface.co/spaces

## Proyectos

- [GPT Bach WTC](../projects/gpt-bach-wtc.md) - Interfaz completa para generación musical

---

**Estado:** Solid - App completa con todos los componentes
**Próximo:** Explorar componentes avanzados, custom themes
