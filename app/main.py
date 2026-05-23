"""
main.py - GENBOT Strategic Intelligence Portal (Government Edition)
Official, Multi-Page Bureau de Intelligence for Policy and Document Analysis.
"""

import streamlit as st
import pandas as pd
import os
import sys
from pathlib import Path

# Add project root to sys.path so absolute imports (core, services) work on Streamlit Cloud
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.config import (
    APP_NAME, VERSION, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, 
    SUCCESS_COLOR, TEXT_COLOR, BACKGROUND_COLOR, SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE
)
from services import pdf_service, url_service, preprocessing
from services.language_service import language_service
from services.ui_labels import get_label
from services.history_service import history_service
from services.pdf_export_service import pdf_export_service
from core.controller import route_task
from app.ui_styles import get_govt_css

# ── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=f"{APP_NAME} - Strategic Intelligence Division", 
    page_icon="🇮🇳", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Helper: shorthand for translated labels ─────────────────────────────────
def L(key, **kwargs):
    """Shorthand for get_label with currently selected language."""
    current_lang = st.session_state.get("user_lang", DEFAULT_LANGUAGE)
    return get_label(key, current_lang, **kwargs)

# ── Custom CSS Inject ────────────────────────────────────────────────────────
st.markdown(get_govt_css(
    PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, SUCCESS_COLOR, TEXT_COLOR, BACKGROUND_COLOR
), unsafe_allow_html=True)

# ── Sidebar: Navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f'<div style="text-align:center; padding:1rem;"><h1>🤖 {APP_NAME}</h1><p>{L("nav_about")}</p></div>', unsafe_allow_html=True)
    
    # 🕵️ Navigation Menu (Bureau Departments)
    NAV_KEYS = ["nav_dashboard", "nav_summarize", "nav_compare", "nav_bias", "nav_lang", "nav_history", "nav_about"]
    nav_labels = [L(k) for k in NAV_KEYS]
    
    selected_label = st.radio(
        L("language_selector") if "language_selector" in nav_labels else "Navigation / नेविगेशन",
        nav_labels,
        index=0,
        key="nav_radio"
    )
    current_page_key = NAV_KEYS[nav_labels.index(selected_label)]

    st.markdown("---")
    
    # 🌐 Persistent Language Selector (Always visible in sidebar)
    lang = st.selectbox(
        L("language_selector"),
        SUPPORTED_LANGUAGES,
        index=SUPPORTED_LANGUAGES.index(st.session_state.get("user_lang", DEFAULT_LANGUAGE)),
        key="lang_select"
    )
    st.session_state["user_lang"] = lang

    st.markdown(f'<div style="position:fixed; bottom:20px; font-size:0.8rem;">{L("footer")}</div>', unsafe_allow_html=True)

# ── Page Functions ────────────────────────────────────────────────────────────

def show_dashboard():
    """Dashboard Page - Official Welcome and Service Insights."""
    # 📸 Hero Banner with Text Overlay
    folders = ["assets", "assests"]
    exts = [".jpeg", ".jpg"]
    
    hero_path = None
    for f in folders:
        for e in exts:
            p = os.path.join(f, f"dashboard_hero{e}")
            if os.path.exists(p):
                hero_path = p
                break
        if hero_path: break
    
    if hero_path:
        base64_img = pdf_service.get_base64_image(hero_path)
        st.markdown(f"""
            <div class="hero-banner" style="background-image: url('data:image/jpeg;base64,{base64_img}');">
                <div class="hero-overlay"></div>
                <div class="hero-content">
                    <h1>{L("dash_hero_title")}</h1>
                    <p>{L("dash_hero_subtitle")}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="header-banner"><h1>{L("dash_hero_title")}</h1><p>{L("dash_hero_subtitle")}</p></div>', unsafe_allow_html=True)
    
    # 📊 Quick Statistics
    history = history_service.get_history()
    total_docs = len(history)
    summaries = len(history[history['Task'].str.contains('Summarize', na=False)])
    comparisons = len(history[history['Task'].str.contains('Compare', na=False)])
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(L("dash_total_analyses"), total_docs)
    with m2:
        st.metric(L("dash_policy_summaries"), summaries)
    with m3:
        st.metric(L("dash_manifesto_comparisons"), comparisons)

    st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("dash_mandate_title")}</div>', unsafe_allow_html=True)
    st.write(L("dash_mandate_text"))
    st.markdown('</div>', unsafe_allow_html=True)


def show_summarize():
    """Summarization Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("sum_page_title")}</h1><p>{L("sum_page_subtitle")}</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("pdf_source_header")}</div>', unsafe_allow_html=True)
        uf = st.file_uploader("", type=["pdf"], key="pdf_up")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("web_source_header")}</div>', unsafe_allow_html=True)
        url = st.text_input("", placeholder="https://...", key="url_in")
        st.markdown('</div>', unsafe_allow_html=True)

    doc_text, source_name = "", ""
    if uf:
        doc_text = pdf_service.extract_text(uf)
        source_name = uf.name
    elif url:
        try:
            doc_text = url_service.scrape_url(url)
            source_name = url
        except RuntimeError as e:
            st.error(f"⚠️ {e}")

    if doc_text:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(L("btn_summary"), use_container_width=True):
            execute_task("Summarize Document", doc_text, st.session_state["user_lang"], [source_name])

def show_compare():
    """Comparison Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("comp_page_title")}</h1><p>{L("comp_page_subtitle")}</p></div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("docs_to_compare")}</div>', unsafe_allow_html=True)
    
    docs, doc_labels = [], []
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(L("policy_a"))
        uf1 = st.file_uploader(L("upload_pdf"), type=["pdf"], key="p_up1")
        url1 = st.text_input(L("web_url"), placeholder="https://...", key="p_url1")
        text1, name1 = ("", "")
        if uf1: text1, name1 = pdf_service.extract_text(uf1), uf1.name
        elif url1: text1, name1 = url_service.scrape_url(url1), url1
        if text1: docs.append(text1); doc_labels.append(name1)

    with c2:
        st.subheader(L("policy_b"))
        uf2 = st.file_uploader(L("upload_pdf"), type=["pdf"], key="p_up2")
        url2 = st.text_input(L("web_url"), placeholder="https://...", key="p_url2")
        text2, name2 = ("", "")
        if uf2: text2, name2 = pdf_service.extract_text(uf2), uf2.name
        elif url2: text2, name2 = url_service.scrape_url(url2), url2
        if text2: docs.append(text2); doc_labels.append(name2)
    
    st.markdown('</div>', unsafe_allow_html=True)

    if len(docs) >= 2:
        if st.button(L("btn_compare"), use_container_width=True):
            execute_task("Compare Documents", docs, st.session_state["user_lang"], doc_labels)

def show_analyze():
    """Bias Analysis Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("bias_page_title")}</h1><p>{L("bias_page_subtitle")}</p></div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("task_analyze")}</div>', unsafe_allow_html=True)
    uf = st.file_uploader(L("upload_pdf"), type=["pdf"], key="bias_up")
    doc_text, source_name = "", ""
    if uf:
        doc_text = pdf_service.extract_text(uf)
        source_name = uf.name
    st.markdown('</div>', unsafe_allow_html=True)

    if doc_text:
        if st.button(L("btn_bias"), use_container_width=True):
            execute_task("Analyze Bias", doc_text, st.session_state["user_lang"], [source_name])

def show_history():
    """Service History Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("hist_page_title")}</h1><p>{L("hist_page_subtitle")}</p></div>', unsafe_allow_html=True)
    
    history = history_service.get_history()
    if history.empty:
        st.info(L("hist_empty"))
    else:
        st.dataframe(history, use_container_width=True, hide_index=True)
        
        c1, c2 = st.columns([1, 4])
        with c1:
            if st.button(L("btn_clear_ledger")):
                history_service.clear_history()
                st.rerun()

def show_language():
    """Language Settings Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("lang_page_title")}</h1><p>{L("lang_page_subtitle")}</p></div>', unsafe_allow_html=True)
    st.write(f"{L('lang_current_prefix')}: **{st.session_state['user_lang']}**")
    st.info("Translation is powered by Google Neural Translation Service.")

def show_about():
    """About Page."""
    st.markdown(f'<div class="header-banner"><h1>{L("about_page_title")}</h1><p>{L("about_page_subtitle")}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="govt-card">', unsafe_allow_html=True)
    st.write(f"**Version**: `{VERSION}`")
    st.write(f"**Core Model**: `BART-Large-CNN` & `BART-MNLI`")
    st.write(f"**Infrastructure**: Strategic Intelligence Division - Digital Bureau")
    st.write(f"**Language Coverage**: 6 Major Indian Languages")
    st.markdown('</div>', unsafe_allow_html=True)

# ── Helper: Task Execution Controller ─────────────────────────────────────────

def execute_task(task_label, payload, language, source_labels):
    """Executes the task and renders results with translated labels."""
    with st.spinner(L("processing")):
        if language_service.is_translation_needed(language):
            if isinstance(payload, list):
                payload = [language_service.translate_to_english(d, language) for d in payload]
            else:
                payload = language_service.translate_to_english(payload, language)

        res = route_task(task_label, payload, language=language, doc_labels=source_labels)

        if res["status"] == "success":
            st.success(L("metric_status_complete"))
            data, meta = res["data"], res["metadata"]

            if res["task"] == "summarize":
                st.subheader(L("tab_bullets"))
                for b in data["bullets"]:
                    st.markdown(f'<div class="result-item">• {b}</div>', unsafe_allow_html=True)
                
                with st.expander(L("tab_table")):
                    st.dataframe(pd.DataFrame(data["table_data"]), use_container_width=True)

                # ── PDF Download ──────────────────────────────────────────────
                import base64 as _b64
                from datetime import datetime as _dt
                _ts = _dt.now().strftime("%Y%m%d_%H%M%S")
                _src = source_labels[0] if source_labels else "document"
                try:
                    pdf_bytes = pdf_export_service.build(
                        bullets=data["bullets"],
                        table_data=data.get("table_data", []),
                        source_name=_src,
                        language=language,
                    )
                    _b64_pdf = _b64.b64encode(pdf_bytes).decode()
                    _fname   = f"genbot_summary_{_ts}.pdf"
                    _label   = L("btn_download_summary_pdf")
                    st.markdown(f"""
                        <a href="data:application/pdf;base64,{_b64_pdf}"
                           download="{_fname}"
                           style="display:block; width:100%; text-align:center;
                                  background:linear-gradient(135deg,#FF6B00,#e65c00);
                                  color:white !important; font-weight:700;
                                  font-size:0.95rem; padding:0.7rem 2rem;
                                  border-radius:10px; text-decoration:none;
                                  box-shadow:0 4px 14px rgba(255,107,0,0.45);
                                  margin-top:0.5rem; letter-spacing:0.3px;">
                            {_label}
                        </a>
                    """, unsafe_allow_html=True)
                except Exception as _pdf_err:
                    st.warning(f"PDF generation failed: {_pdf_err}")

            elif res["task"] == "compare":
                st.subheader(f"{L('similarity_score_label')}: {data.get('similarity_score')}%")
                st.info(data.get("interpretation"))
                for label in source_labels:
                    key = "unique_to_" + label.replace(' ', '_').replace('/', '_')
                    if key in data:
                        with st.expander(f"{L('unique_points_in', label=label)}"):
                            for p in data[key]:
                                st.markdown(f'<div class="result-item result-item-alt">• {p}</div>', unsafe_allow_html=True)

                # ── PDF Download ──────────────────────────────────────────────
                import base64 as _b64
                from datetime import datetime as _dt
                _ts = _dt.now().strftime("%Y%m%d_%H%M%S")
                try:
                    pdf_bytes = pdf_export_service.build_compare_pdf(
                        similarity_score=data.get("similarity_score", 0),
                        interpretation=data.get("interpretation", ""),
                        unique_points=data,
                        source_labels=source_labels,
                        language=language,
                    )
                    _b64_pdf = _b64.b64encode(pdf_bytes).decode()
                    _fname   = f"genbot_comparison_{_ts}.pdf"
                    _label   = L("btn_download_compare_pdf")
                    st.markdown(f"""
                        <a href="data:application/pdf;base64,{_b64_pdf}"
                           download="{_fname}"
                           style="display:block; width:100%; text-align:center;
                                  background:linear-gradient(135deg,#FF6B00,#e65c00);
                                  color:white !important; font-weight:700;
                                  font-size:0.95rem; padding:0.7rem 2rem;
                                  border-radius:10px; text-decoration:none;
                                  box-shadow:0 4px 14px rgba(255,107,0,0.45);
                                  margin-top:0.5rem; letter-spacing:0.3px;">
                            {_label}
                        </a>
                    """, unsafe_allow_html=True)
                except Exception as _pdf_err:
                    st.warning(f"PDF generation failed: {_pdf_err}")

            elif res["task"] == "analyze":
                scores_dict = data.get("all_scores", {})
                
                # Get the score for the predicted category
                pred_cat = data.get("predicted_category", "Unknown")
                pred_score = scores_dict.get(pred_cat, 0.0)
                
                st.markdown(f'<div class="govt-card"><div class="govt-card-header">{L("predicted_focus")}: <strong>{pred_cat}</strong></div>', unsafe_allow_html=True)
                st.progress(pred_score / 100.0 if pred_score > 1 else pred_score)
                st.metric(label="Highlight Confidence Score", value=f"{pred_score:.1f}%")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Display all scores in a clean sorted table
                st.subheader("Detailed Bureau Analysis (%)")
                if scores_dict:
                    # Convert to dataframe, sort descending
                    df_scores = pd.DataFrame(list(scores_dict.items()), columns=["Category", "Percentage"])
                    df_scores = df_scores.sort_values(by="Percentage", ascending=False).reset_index(drop=True)
                    df_scores["Percentage"] = df_scores["Percentage"].apply(lambda x: f"{x:.1f}%")
                    
                    st.dataframe(df_scores, use_container_width=True)
                else:
                    st.info("No detailed scores available.")

                # ── PDF Download ──────────────────────────────────────────────
                import base64 as _b64
                from datetime import datetime as _dt
                _ts = _dt.now().strftime("%Y%m%d_%H%M%S")
                _src = source_labels[0] if source_labels else "document"
                try:
                    pdf_bytes = pdf_export_service.build_analyze_pdf(
                        pred_cat=pred_cat,
                        pred_score=pred_score,
                        scores_dict=scores_dict,
                        source_name=_src,
                        language=language,
                    )
                    _b64_pdf = _b64.b64encode(pdf_bytes).decode()
                    _fname   = f"genbot_bias_analysis_{_ts}.pdf"
                    _label   = L("btn_download_bias_pdf")
                    st.markdown(f"""
                        <a href="data:application/pdf;base64,{_b64_pdf}"
                           download="{_fname}"
                           style="display:block; width:100%; text-align:center;
                                  background:linear-gradient(135deg,#FF6B00,#e65c00);
                                  color:white !important; font-weight:700;
                                  font-size:0.95rem; padding:0.7rem 2rem;
                                  border-radius:10px; text-decoration:none;
                                  box-shadow:0 4px 14px rgba(255,107,0,0.45);
                                  margin-top:0.5rem; letter-spacing:0.3px;">
                            {_label}
                        </a>
                    """, unsafe_allow_html=True)
                except Exception as _pdf_err:
                    st.warning(f"PDF generation failed: {_pdf_err}")
        else:
            st.error(f"❌ Bureau Error: {res['message']}")

# ── Router Logic ─────────────────────────────────────────────────────────────

if current_page_key == "nav_dashboard": show_dashboard()
elif current_page_key == "nav_summarize": show_summarize()
elif current_page_key == "nav_compare": show_compare()
elif current_page_key == "nav_bias": show_analyze()
elif current_page_key == "nav_lang": show_language()
elif current_page_key == "nav_history": show_history()
elif current_page_key == "nav_about": show_about()

st.markdown("---")
st.markdown(f'<p style="text-align:center; color:#6b7280; font-size:0.8rem;">{L("footer")}</p>', unsafe_allow_html=True)