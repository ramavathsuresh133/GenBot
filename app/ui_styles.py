"""
ui_styles.py - Custom CSS for the GENBOT Strategic Intelligence Portal
Implements a formal, government-style Light Theme.
"""

def get_govt_css(primary, secondary, accent, success, text, bg):
    """Returns a string of CSS for a professional government portal."""
    return f"""
    <style>
    /* Global Background and Typography */
    .stApp {{
        background-color: {bg};
        color: {text};
        font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}

    /* Sidebar Navigation Styling */
    [data-testid="stSidebar"] {{
        background-color: {primary};
        border-right: 2px solid {accent};
    }}
    /* Target only text elements inside the sidebar to prevent affecting main content */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] label,
    [data-testid="stSidebar"] h1 {{
        color: white !important;
    }}
    .st-emotion-cache-6qob1r {{
        background-color: rgba(255, 255, 255, 0.1) !important;
    }}

    /* Main Header Banner */
    .header-banner {{
        background-color: {primary};
        padding: 2.0rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 4px solid {accent};
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .header-banner h1 {{
        color: white !important;
        margin: 0;
        font-weight: 800;
        letter-spacing: -1px;
    }}
    .header-banner p {{
        color: #e2e8f0 !important;
        margin-top: 0.5rem;
        font-size: 1.1rem;
    }}

    /* Formal Cards */
    .govt-card {{
        background-color: {secondary};
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }}
    .govt-card-header {{
        color: {primary};
        font-weight: 700;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid {bg};
        padding-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}

    /* Metrics & Stats */
    [data-testid="stMetricValue"] {{
        color: {primary} !important;
        font-weight: 800 !important;
    }}
    
    /* Result Items (Summary Bullets) */
    .result-item {{
        background-color: #f9fafb;
        border-left: 5px solid {primary};
        padding: 1.25rem;
        margin-bottom: 1rem;
        border-radius: 0 8px 8px 0;
        line-height: 1.6;
        color: {text};
    }}
    .result-item-alt {{
        border-left-color: {accent};
    }}

    /* Buttons & File Uploader Contrast Fixes */
    .stButton>button {{
        background-color: {primary} !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease;
    }}
    .stButton>button:hover {{
        background-color: #1e40af !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}

    /* Fix: Visible filename text after upload */
    [data-testid="stFileUploaderFileName"] {{
        color: {text} !important;
        font-weight: 600 !important;
    }}
    /* Fix: Uploader button (Browse) visibility */
    [data-testid="stFileUploader"] button {{
        border: 1px solid {primary} !important;
        color: {primary} !important;
        background-color: white !important;
    }}

    /* Dashboard Hero Banner (Full Image) */
    .hero-banner {{
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        margin-top: -3.5rem;
        height: 580px;
        background-size: 100% 100%;
        background-position: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        border-bottom: 5px solid {accent};
    }}
    .hero-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(30, 58, 138, 0.65); /* Navy Overlay with transparency */
        z-index: 1;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        padding: 0 2rem;
    }}
    .hero-content h1 {{
        color: white !important;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -2px !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .hero-content p {{
        color: #f1f5f9 !important;
        font-size: 1.25rem !important;
        font-weight: 500 !important;
        opacity: 0.9;
    }}

    /* Tags & Badges */
    .status-badge {{
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        background-color: {bg};
        color: {primary};
        border: 1px solid {primary};
    }}

    /* Table Customization */
    .stDataFrame {{
        border: 1px solid #e5e7eb;
        border-radius: 8px;
    }}

    </style>
    """
