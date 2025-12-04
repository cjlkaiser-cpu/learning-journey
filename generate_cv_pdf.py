#!/usr/bin/env python3
"""
CV PDF Generator - Carlos Lorente Kaiser
Generates a clean, professional PDF CV
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

# Colors
PRIMARY = HexColor("#1a365d")      # Dark blue
SECONDARY = HexColor("#2d3748")    # Dark gray
ACCENT = HexColor("#3182ce")       # Blue accent
TEXT = HexColor("#1a202c")         # Near black
LIGHT_TEXT = HexColor("#4a5568")   # Gray text
LIGHT_BG = HexColor("#f7fafc")     # Light background
LINE = HexColor("#e2e8f0")         # Light line

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()

    # Name header
    styles.add(ParagraphStyle(
        name='Name',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=2*mm,
        fontName='Helvetica-Bold'
    ))

    # Tagline
    styles.add(ParagraphStyle(
        name='Tagline',
        fontSize=11,
        leading=14,
        textColor=ACCENT,
        spaceAfter=4*mm,
        fontName='Helvetica-Oblique'
    ))

    # Contact info
    styles.add(ParagraphStyle(
        name='Contact',
        fontSize=9,
        leading=12,
        textColor=LIGHT_TEXT,
        spaceAfter=6*mm,
        fontName='Helvetica'
    ))

    # Section header
    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontSize=12,
        leading=16,
        textColor=PRIMARY,
        spaceBefore=6*mm,
        spaceAfter=3*mm,
        fontName='Helvetica-Bold'
    ))

    # Subsection header
    styles.add(ParagraphStyle(
        name='SubHeader',
        fontSize=10,
        leading=13,
        textColor=SECONDARY,
        spaceBefore=3*mm,
        spaceAfter=1*mm,
        fontName='Helvetica-Bold'
    ))

    # Body text
    styles.add(ParagraphStyle(
        name='Body',
        fontSize=9,
        leading=12,
        textColor=TEXT,
        spaceAfter=2*mm,
        fontName='Helvetica',
        alignment=TA_JUSTIFY
    ))

    # Bullet points
    styles.add(ParagraphStyle(
        name='BulletItem',
        fontSize=9,
        leading=12,
        textColor=TEXT,
        leftIndent=8*mm,
        spaceAfter=1*mm,
        fontName='Helvetica',
        bulletIndent=3*mm,
        bulletFontSize=9
    ))

    # Small text
    styles.add(ParagraphStyle(
        name='Small',
        fontSize=8,
        leading=10,
        textColor=LIGHT_TEXT,
        fontName='Helvetica'
    ))

    # Tech stack
    styles.add(ParagraphStyle(
        name='Tech',
        fontSize=8,
        leading=11,
        textColor=ACCENT,
        fontName='Helvetica-Oblique'
    ))

    return styles

def create_section_line():
    """Create a subtle horizontal line"""
    return HRFlowable(
        width="100%",
        thickness=0.5,
        color=LINE,
        spaceBefore=2*mm,
        spaceAfter=2*mm
    )

def build_cv():
    """Build the CV PDF"""
    output_path = Path(__file__).parent / "CV_Carlos_Lorente_Kaiser.pdf"

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm
    )

    styles = create_styles()
    story = []

    # === HEADER ===
    story.append(Paragraph("CARLOS LORENTE KAISER", styles['Name']))
    story.append(Paragraph(
        "Physicist + Pharmacist → AI Engineer | Healthcare + Tech + Science",
        styles['Tagline']
    ))
    story.append(Paragraph(
        "Madrid, Spain  •  cjlkaiser@hotmail.com  •  github.com/cjlkaiser-cpu",
        styles['Contact']
    ))

    # === PROFILE ===
    story.append(Paragraph("PROFILE", styles['SectionHeader']))
    story.append(create_section_line())
    story.append(Paragraph(
        "Dual scientific background combining <b>Theoretical Physics</b> (UAM) and <b>Pharmacy</b> (CEU), "
        "with international experience at <b>Università La Sapienza, Rome</b>. "
        "This rare combination enables me to bridge fundamental science, healthcare, and AI engineering "
        "with mathematical rigor, clinical expertise, and technical execution.",
        styles['Body']
    ))

    # === IMPACT METRICS ===
    story.append(Paragraph("KEY ACHIEVEMENTS", styles['SectionHeader']))
    story.append(create_section_line())

    metrics = [
        "• Improved Spanish pharmacy LLM accuracy: <b>30% → 93%+</b> (63-point gain)",
        "• Built and deployed <b>8 production applications</b> in 3 months",
        "• Created <b>minerOS</b>: Original data mining methodology",
        "• Validated <b>200 clinical cases</b> with systematic scientific methodology",
        "• Classified <b>1,361 photos</b> with custom ML pipeline (GPU-accelerated)",
    ]
    for m in metrics:
        story.append(Paragraph(m, styles['BulletItem']))

    # === PROJECTS ===
    story.append(Paragraph("FEATURED PROJECTS", styles['SectionHeader']))
    story.append(create_section_line())

    # BioMistral
    story.append(Paragraph("BioMistral RAG v1.3 — AI Validation Research", styles['SubHeader']))
    story.append(Paragraph("Python • Ollama • RAG • LLMs • Chain of Thought", styles['Tech']))
    story.append(Paragraph(
        "Rigorous scientific validation of Spanish pharmacy AI model. Implemented RAG with Chain of Thought "
        "and JSON structured output. Developed specialized geriatric mode with STOPP/START criteria. "
        "Achieved 93%+ accuracy while identifying critical safety gaps for healthcare applications.",
        styles['Body']
    ))

    # DirectOS
    story.append(Paragraph("DirectOS v8.1 — Visual Pipeline Designer", styles['SubHeader']))
    story.append(Paragraph("JavaScript (Vanilla) • FastAPI • AI Agents • RAG", styles['Tech']))
    story.append(Paragraph(
        "Production-ready IDE with integrated AI agents and offline-first architecture. "
        "3,000+ lines of vanilla JavaScript following KISS principles. Features Scout Agent for intelligent "
        "debugging and Human-in-the-Loop workflow ensuring production safety.",
        styles['Body']
    ))

    # minerOS
    story.append(Paragraph("minerOS — Original Data Mining Methodology", styles['SubHeader']))
    story.append(Paragraph("Framework Design • System Architecture", styles['Tech']))
    story.append(Paragraph(
        "Created reusable methodology from first principles: \"ORO → GEMAS → TESORO\". "
        "Six modular components successfully applied across 3 production projects. "
        "Core principle: \"Sin magia negra\" — everything debuggeable.",
        styles['Body']
    ))

    # PhotoMine
    story.append(Paragraph("PhotoMine v1.4 — AI Photo Classifier", styles['SubHeader']))
    story.append(Paragraph("Python • CLIP • ML • GPU Acceleration (Apple MPS)", styles['Tech']))
    story.append(Paragraph(
        "End-to-end ML pipeline processing 1,361 photos with semantic classification. "
        "GPU-accelerated on Apple Silicon, EXIF/GPS extraction, Flask dashboard. "
        "Full implementation of minerOS methodology in production.",
        styles['Body']
    ))

    # === TECHNICAL SKILLS ===
    story.append(Paragraph("TECHNICAL SKILLS", styles['SectionHeader']))
    story.append(create_section_line())

    skills_data = [
        ["<b>Languages</b>", "Python, JavaScript (Vanilla), SQL"],
        ["<b>AI/ML</b>", "RAG, CLIP, LLM Validation, Ollama, Chain of Thought, Embeddings"],
        ["<b>Backend</b>", "Flask, FastAPI, REST APIs, Node.js"],
        ["<b>Databases</b>", "SQLite, PostgreSQL, ChromaDB (Vector)"],
        ["<b>Tools</b>", "Git/GitHub, VS Code, Claude API, AI Agents (HITL)"],
    ]

    for skill_row in skills_data:
        story.append(Paragraph(f"{skill_row[0]}: {skill_row[1]}", styles['BulletItem']))

    # === EDUCATION ===
    story.append(Paragraph("EDUCATION", styles['SectionHeader']))
    story.append(create_section_line())

    story.append(Paragraph("Licenciado en Física Teórica — Universidad Autónoma de Madrid (UAM)", styles['SubHeader']))
    story.append(Paragraph(
        "Mathematical foundations, computational physics, research methodology, algorithmic thinking.",
        styles['Body']
    ))

    story.append(Paragraph("Licenciado en Farmacia — Universidad CEU", styles['SubHeader']))
    story.append(Paragraph(
        "Clinical pharmacy, pharmacology, drug interactions, healthcare regulations.",
        styles['Body']
    ))

    story.append(Paragraph("International Experience — Università La Sapienza, Rome", styles['SubHeader']))
    story.append(Paragraph(
        "Academic year in Italy. International research environment. Italian language proficiency.",
        styles['Body']
    ))

    # === LANGUAGES ===
    story.append(Paragraph("LANGUAGES", styles['SectionHeader']))
    story.append(create_section_line())
    story.append(Paragraph(
        "<b>Spanish</b> (Native)  •  <b>English</b> (Fluent - Technical & Scientific)  •  <b>Italian</b> (Proficient)",
        styles['Body']
    ))

    # === VALUE PROPOSITION ===
    story.append(Paragraph("UNIQUE VALUE", styles['SectionHeader']))
    story.append(create_section_line())
    story.append(Paragraph(
        "<b>Triple Domain Expertise:</b> Physics (mathematical rigor) + Healthcare (clinical knowledge) + "
        "AI Engineering (technical execution). Rare ability to bridge scientists, clinicians, and engineers. "
        "Scientific approach to software: systematic validation, original methodologies, evidence-based AI safety.",
        styles['Body']
    ))

    # === FOOTER ===
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph(
        "Full learning journey documented at: github.com/cjlkaiser-cpu/learning-journey",
        styles['Small']
    ))
    story.append(Paragraph(
        "\"From understanding the universe to helping people — one validated AI system at a time.\"",
        styles['Small']
    ))

    # Build PDF
    doc.build(story)
    print(f"✅ CV generated: {output_path}")
    return output_path

if __name__ == "__main__":
    build_cv()
