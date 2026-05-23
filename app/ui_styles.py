# """
# ui_styles.py - Custom CSS for the GENBOT Strategic Intelligence Portal
# Implements a formal, government-style Light Theme.
# """

# def get_govt_css(primary, secondary, accent, success, text, bg):
#     """Returns a string of CSS for a professional government portal."""
#     return f"""
#     <style>
#     /* Global Background and Typography */
#     .stApp {{
#         background-color: {bg};
#         color: {text};
#         font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
#     }}

#     /* Sidebar Navigation Styling */
#     [data-testid="stSidebar"] {{
#         background-color: {primary};
#         border-right: 2px solid {accent};
#     }}
#     /* Target only text elements inside the sidebar to prevent affecting main content */
#     [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
#     [data-testid="stSidebar"] [data-testid="stWidgetLabel"] label,
#     [data-testid="stSidebar"] h1 {{
#         color: white !important;
#     }}
#     .st-emotion-cache-6qob1r {{
#         background-color: rgba(255, 255, 255, 0.1) !important;
#     }}

#     /* Main Header Banner */
#     .header-banner {{
#         background-color: {primary};
#         padding: 2.0rem;
#         border-radius: 12px;
#         text-align: center;
#         margin-bottom: 2rem;
#         border-bottom: 4px solid {accent};
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
#     }}
#     .header-banner h1 {{
#         color: white !important;
#         margin: 0;
#         font-weight: 800;
#         letter-spacing: -1px;
#     }}
#     .header-banner p {{
#         color: #e2e8f0 !important;
#         margin-top: 0.5rem;
#         font-size: 1.1rem;
#     }}

#     /* Formal Cards */
#     .govt-card {{
#         background-color: {secondary};
#         padding: 2rem;
#         border-radius: 12px;
#         border: 1px solid #e5e7eb;
#         box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
#         margin-bottom: 1.5rem;
#     }}
#     .govt-card-header {{
#         color: {primary};
#         font-weight: 700;
#         font-size: 1.25rem;
#         margin-bottom: 1rem;
#         border-bottom: 2px solid {bg};
#         padding-bottom: 0.5rem;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }}

#     /* Metrics & Stats */
#     [data-testid="stMetricValue"] {{
#         color: {primary} !important;
#         font-weight: 800 !important;
#     }}
    
#     /* Result Items (Summary Bullets) */
#     .result-item {{
#         background-color: #f9fafb;
#         border-left: 5px solid {primary};
#         padding: 1.25rem;
#         margin-bottom: 1rem;
#         border-radius: 0 8px 8px 0;
#         line-height: 1.6;
#         color: {text};
#     }}
#     .result-item-alt {{
#         border-left-color: {accent};
#     }}

#     /* Buttons & File Uploader Contrast Fixes */
#     .stButton>button {{
#         background-color: {primary} !important;
#         color: white !important;
#         border-radius: 8px !important;
#         border: none !important;
#         padding: 0.6rem 2rem !important;
#         font-weight: 600 !important;
#         transition: all 0.2s ease;
#     }}
#     .stButton>button:hover {{
#         background-color: #1e40af !important;
#         transform: translateY(-1px);
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
#     }}

#     /* Fix: Visible filename text after upload */
#     [data-testid="stFileUploaderFileName"] {{
#         color: {text} !important;
#         font-weight: 600 !important;
#     }}
#     /* Fix: Uploader button (Browse) visibility */
#     [data-testid="stFileUploader"] button {{
#         border: 1px solid {primary} !important;
#         color: {primary} !important;
#         background-color: white !important;
#     }}

#     /* Dashboard Hero Banner (Full Image) */
#     .hero-banner {{
#         width: 100vw;
#         margin-left: calc(-50vw + 50%);
#         margin-top: -3.5rem;
#         height: 580px;
#         background-size: 100% 100%;
#         background-position: center;
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#         align-items: center;
#         text-align: center;
#         position: relative;
#         box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
#         border-bottom: 5px solid {accent};
#     }}
#     .hero-overlay {{
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: rgba(30, 58, 138, 0.65); /* Navy Overlay with transparency */
#         z-index: 1;
#     }}
#     .hero-content {{
#         position: relative;
#         z-index: 2;
#         padding: 0 2rem;
#     }}
#     .hero-content h1 {{
#         color: white !important;
#         font-size: 3.5rem !important;
#         font-weight: 900 !important;
#         margin-bottom: 0.5rem !important;
#         letter-spacing: -2px !important;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
#     }}
#     .hero-content p {{
#         color: #f1f5f9 !important;
#         font-size: 1.25rem !important;
#         font-weight: 500 !important;
#         opacity: 0.9;
#     }}

#     /* Tags & Badges */
#     .status-badge {{
#         display: inline-block;
#         padding: 0.25rem 0.75rem;
#         border-radius: 9999px;
#         font-size: 0.75rem;
#         font-weight: 600;
#         background-color: {bg};
#         color: {primary};
#         border: 1px solid {primary};
#     }}

#     /* Table Customization */
#     .stDataFrame {{
#         border: 1px solid #e5e7eb;
#         border-radius: 8px;
#     }}

#     </style>
#     """


"""
ui_styles.py - GENBOT Strategic Intelligence Portal
India.gov.in inspired theme — Navy + Saffron + White
Fixes:
  - Metric labels now visible (white text on colored background)
  - Division Mandate card properly styled
  - Dashboard attractive, clear, user-friendly
  - India.gov.in color palette applied throughout
"""

# ── India.gov.in Official Color Palette ──────────────────────────────────────
INDIA_NAVY      = "#1B3A6B"   # Primary navy (header, sidebar)
INDIA_SAFFRON   = "#FF6B00"   # Saffron accent (borders, highlights)
INDIA_GREEN     = "#138808"   # Indian flag green (success states)
INDIA_WHITE     = "#FFFFFF"
INDIA_LIGHT_BG  = "#F4F6FA"   # Light page background
INDIA_CARD_BG   = "#FFFFFF"
INDIA_TEXT      = "#1A1A2E"
INDIA_MUTED     = "#64748B"
INDIA_BORDER    = "#E2E8F0"


def get_govt_css(primary=INDIA_NAVY, secondary=INDIA_CARD_BG,
                 accent=INDIA_SAFFRON, success=INDIA_GREEN,
                 text=INDIA_TEXT, bg=INDIA_LIGHT_BG):
    return f"""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>

    /* ── Global ─────────────────────────────────────────────────────────── */
    .stApp {{
        background-color: {bg};
        color: {text};
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    }}
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }}

    /* ── Sidebar ─────────────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {primary} 0%, #0f2347 100%);
        border-right: 3px solid {accent};
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {{
        background-color: rgba(255,255,255,0.15) !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
        border-radius: 8px !important;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: rgba(255,255,255,0.2) !important;
    }}

    /* ── Hero Banner ─────────────────────────────────────────────────────── */
    .hero-banner {{
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        margin-top: -3.5rem;
        height: 560px;
        background-size: cover;
        background-position: center top;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        border-bottom: 5px solid {accent};
    }}
    .hero-overlay {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(27,58,107,0.80) 0%, rgba(15,35,71,0.70) 100%);
        z-index: 1;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        padding: 0 2rem;
    }}
    .hero-content h1 {{
        color: white !important;
        font-size: 3.2rem !important;
        font-weight: 900 !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -1px !important;
        text-shadow: 2px 3px 8px rgba(0,0,0,0.6) !important;
    }}
    .hero-content p {{
        color: #f1f5f9 !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        opacity: 0.95 !important;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5) !important;
    }}
    .hero-badge {{
        display: inline-block;
        background: {accent};
        color: white !important;
        padding: 0.3rem 1.2rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}

    /* ── ✅ FIX: Metric Cards — labels now visible ────────────────────────── */
    /* Wrap metrics in .metric-card div for proper styling */
    .metric-card {{
        background: linear-gradient(135deg, {primary} 0%, #0f2347 100%);
        border-radius: 14px;
        padding: 1.4rem 1.2rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 4px 12px rgba(27,58,107,0.25);
        border-bottom: 4px solid {accent};
    }}
    .metric-card .metric-label {{
        color: #cbd5e1 !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
        margin-bottom: 0.5rem !important;
    }}
    .metric-card .metric-value {{
        color: white !important;
        font-size: 2.4rem !important;
        font-weight: 900 !important;
        line-height: 1.1 !important;
    }}
    .metric-card .metric-sub {{
        color: {accent} !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        margin-top: 0.25rem !important;
    }}

    /* ── ✅ FIX: Streamlit native metric visibility ───────────────────────── */
    [data-testid="stMetricLabel"] {{
        color: {primary} !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {primary} !important;
        font-weight: 900 !important;
        font-size: 2rem !important;
    }}
    [data-testid="stMetric"] {{
        background: white !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid {INDIA_BORDER} !important;
        border-left: 4px solid {accent} !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }}

    /* ── ✅ FIX: Division Mandate / Govt Cards ───────────────────────────── */
    .govt-card {{
        background-color: {secondary};
        padding: 1.8rem 2rem;
        border-radius: 14px;
        border: 1px solid {INDIA_BORDER};
        border-left: 5px solid {primary};
        box-shadow: 0 2px 8px rgba(0,0,0,0.07);
        margin-bottom: 1.5rem;
    }}
    .govt-card-header {{
        color: {primary};
        font-weight: 800;
        font-size: 1.15rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding-bottom: 0.6rem;
        border-bottom: 2px solid {bg};
    }}
    .govt-card p, .govt-card li {{
        color: {text} !important;
        font-size: 0.95rem;
        line-height: 1.7;
    }}

    /* ── Mandate / About Banner ──────────────────────────────────────────── */
    .mandate-banner {{
        background: linear-gradient(135deg, {primary} 0%, #0f2347 100%);
        border-radius: 14px;
        padding: 2rem;
        border-left: 6px solid {accent};
        margin-bottom: 1.5rem;
    }}
    .mandate-banner h3 {{
        color: white !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
    }}
    .mandate-banner p {{
        color: #cbd5e1 !important;
        line-height: 1.7 !important;
        font-size: 0.95rem !important;
    }}

    /* ── Capability Cards (Dashboard feature grid) ───────────────────────── */
    .capability-card {{
        background: white;
        border-radius: 14px;
        padding: 1.5rem;
        border: 1px solid {INDIA_BORDER};
        border-top: 4px solid {accent};
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .capability-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(27,58,107,0.15);
    }}
    .capability-card .cap-icon {{
        font-size: 2rem;
        margin-bottom: 0.75rem;
    }}
    .capability-card h4 {{
        color: {primary} !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }}
    .capability-card p {{
        color: {INDIA_MUTED} !important;
        font-size: 0.85rem !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }}

    /* ── Header Banner (non-hero pages) ─────────────────────────────────── */
    .header-banner {{
        background: linear-gradient(135deg, {primary} 0%, #0f2347 100%);
        padding: 1.8rem 2rem;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 1.5rem;
        border-bottom: 4px solid {accent};
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}
    .header-banner h1 {{
        color: white !important;
        margin: 0;
        font-weight: 800;
        font-size: 2rem !important;
    }}
    .header-banner p {{
        color: #e2e8f0 !important;
        margin-top: 0.4rem;
        font-size: 1rem;
    }}

    /* ── Tricolor Top Bar ────────────────────────────────────────────────── */
    .tricolor-bar {{
        height: 6px;
        background: linear-gradient(90deg, #FF6B00 33.3%, white 33.3%, white 66.6%, #138808 66.6%);
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        margin-bottom: 0;
    }}

    /* ── Section Divider ─────────────────────────────────────────────────── */
    .section-divider {{
        border: none;
        height: 2px;
        background: linear-gradient(90deg, {accent}, {primary}, transparent);
        margin: 1.5rem 0;
        border-radius: 2px;
    }}

    /* ── Result Items ────────────────────────────────────────────────────── */
    .result-item {{
        background-color: #f9fafb;
        border-left: 5px solid {primary};
        padding: 1.1rem 1.4rem;
        margin-bottom: 0.9rem;
        border-radius: 0 10px 10px 0;
        line-height: 1.7;
        color: {text};
        font-size: 0.95rem;
    }}
    .result-item-alt {{
        border-left-color: {accent};
        background-color: #fff8f3;
    }}

    /* ── Buttons ─────────────────────────────────────────────────────────── */
    .stButton > button {{
        background: linear-gradient(135deg, {primary} 0%, #0f2347 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 0.65rem 2rem !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 8px rgba(27,58,107,0.3) !important;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, {accent} 0%, #cc5500 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(255,107,0,0.35) !important;
    }}

    /* ── Download Button — all selector variants for cross-version compat ── */
    [data-testid="stDownloadButton"] > button,
    [data-testid="stDownloadButton"] button,
    .stDownloadButton > button,
    .stDownloadButton button,
    div[data-testid="stDownloadButton"] button {{
        background: linear-gradient(135deg, {accent} 0%, #e65c00 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: 2px solid {accent} !important;
        padding: 0.65rem 2rem !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 14px rgba(255,107,0,0.45) !important;
    }}
    [data-testid="stDownloadButton"] > button:hover,
    [data-testid="stDownloadButton"] button:hover,
    .stDownloadButton > button:hover,
    .stDownloadButton button:hover {{
        background: linear-gradient(135deg, #ff8c00 0%, #cc4400 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 22px rgba(255,107,0,0.55) !important;
    }}
    [data-testid="stDownloadButton"] > button:active,
    .stDownloadButton > button:active {{
        transform: translateY(0px) !important;
        box-shadow: 0 2px 8px rgba(255,107,0,0.3) !important;
    }}
    /* Ensure icon/text inside download button is white */
    [data-testid="stDownloadButton"] button p,
    [data-testid="stDownloadButton"] button span,
    .stDownloadButton button p,
    .stDownloadButton button span {{
        color: white !important;
    }}

    /* ── File Uploader ───────────────────────────────────────────────────── */
    [data-testid="stFileUploaderFileName"] {{
        color: {text} !important;
        font-weight: 600 !important;
    }}
    [data-testid="stFileUploader"] button {{
        border: 2px solid {primary} !important;
        color: {primary} !important;
        background-color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }}
    [data-testid="stFileUploader"] {{
        border: 2px dashed {INDIA_BORDER} !important;
        border-radius: 12px !important;
        background: #fafbff !important;
    }}

    /* ── Input Fields ────────────────────────────────────────────────────── */
    .stTextInput input, .stSelectbox div {{
        border-radius: 8px !important;
        border-color: {INDIA_BORDER} !important;
    }}
    .stTextInput input:focus {{
        border-color: {primary} !important;
        box-shadow: 0 0 0 3px rgba(27,58,107,0.1) !important;
    }}

    /* ── Tabs ────────────────────────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {{
        background: #f1f5f9 !important;
        border-radius: 10px !important;
        padding: 4px !important;
        gap: 4px !important;
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 8px !important;
        font-weight: 600 !important;
        color: {INDIA_MUTED} !important;
        padding: 0.5rem 1.2rem !important;
    }}
    .stTabs [aria-selected="true"] {{
        background: {primary} !important;
        color: white !important;
    }}

    /* ── DataFrames ──────────────────────────────────────────────────────── */
    .stDataFrame {{
        border: 1px solid {INDIA_BORDER} !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }}

    /* ── Spinner / Status ────────────────────────────────────────────────── */
    .stSpinner > div {{
        border-top-color: {primary} !important;
    }}

    /* ── Status Badge ────────────────────────────────────────────────────── */
    .status-badge {{
        display: inline-block;
        padding: 0.2rem 0.8rem;
        border-radius: 9999px;
        font-size: 0.72rem;
        font-weight: 700;
        background-color: #EEF2FF;
        color: {primary};
        border: 1px solid {primary};
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}
    .status-badge-success {{
        background-color: #ECFDF5;
        color: {success};
        border-color: {success};
    }}
    .status-badge-warning {{
        background-color: #FFF7ED;
        color: {accent};
        border-color: {accent};
    }}

    /* ── Language Pill ───────────────────────────────────────────────────── */
    .lang-pill {{
        display: inline-block;
        background: rgba(255,107,0,0.1);
        color: {accent};
        border: 1px solid {accent};
        border-radius: 999px;
        padding: 0.15rem 0.7rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.1rem;
    }}

    /* ── Footer ──────────────────────────────────────────────────────────── */
    .portal-footer {{
        text-align: center;
        padding: 1.5rem;
        color: {INDIA_MUTED};
        font-size: 0.82rem;
        border-top: 2px solid {INDIA_BORDER};
        margin-top: 3rem;
    }}
    .portal-footer span {{
        color: {accent};
        font-weight: 600;
    }}

    /* ── Expander ────────────────────────────────────────────────────────── */
    .streamlit-expanderHeader {{
        background: #f1f5f9 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        color: {primary} !important;
    }}

    /* ── Radio Buttons ───────────────────────────────────────────────────── */
    .stRadio label {{
        font-weight: 500 !important;
        color: {text} !important;
    }}

    /* ── Checkbox ────────────────────────────────────────────────────────── */
    .stCheckbox label {{
        font-weight: 500 !important;
        color: {text} !important;
    }}

    /* ── Warning / Info / Error boxes ───────────────────────────────────── */
    .stAlert {{
        border-radius: 10px !important;
    }}

    </style>
    """


# ── Dashboard HTML Components ─────────────────────────────────────────────────

def tricolor_bar():
    """Returns the Indian tricolor top bar HTML."""
    return '<div class="tricolor-bar"></div>'


def metric_card(icon, label, value, sub=""):
    """Returns a properly styled metric card with visible label."""
    return f"""
    <div class="metric-card">
        <div class="metric-label">{icon} {label}</div>
        <div class="metric-value">{value}</div>
        {"<div class='metric-sub'>" + sub + "</div>" if sub else ""}
    </div>
    """


def capability_card(icon, title, description):
    """Returns a capability/feature card for the dashboard."""
    return f"""
    <div class="capability-card">
        <div class="cap-icon">{icon}</div>
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """


def mandate_banner(title, description):
    """Returns the Division Mandate banner with proper dark background and white text."""
    return f"""
    <div class="mandate-banner">
        <h3>📋 {title}</h3>
        <p>{description}</p>
    </div>
    """


def section_divider():
    return '<hr class="section-divider">'


def portal_footer():
    return """
    <div class="portal-footer">
        🇮🇳 <span>GENBOT Strategic Intelligence Portal</span> &nbsp;·&nbsp; 
        Powered by Modular Multi-Model NLP &nbsp;·&nbsp; 
        v1.1 Production &nbsp;·&nbsp; 
        Built for <span>Bharat</span>
    </div>
    """