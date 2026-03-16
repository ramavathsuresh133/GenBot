"""
main.py - GENBOT Streamlit Frontend (Metadata & Performance Edition)
"""

import streamlit as st
import pandas as pd
from core.config import APP_NAME, VERSION, THEME_GRADIENT, ACCENT_COLOR
from services import pdf_service, url_service, preprocessing
from core.controller import route_task

# ── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(page_title=f"{APP_NAME} v{VERSION}", page_icon="🤖", layout="wide")

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown(f"""
    <style>
    .stApp {{ background: {THEME_GRADIENT}; color: #e0e0ff; }}
    .title-banner {{ text-align: center; padding: 1.5rem; }}
    .title-banner h1 {{ color: {ACCENT_COLOR}; font-size: 3.5rem; margin: 0; font-weight: 800; }}
    .input-card {{ background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 16px; margin-bottom: 1.5rem; border: 1px solid rgba(167,139,250,0.2); }}
    .section-header {{ color: {ACCENT_COLOR}; font-weight: 700; margin-bottom: 0.8rem; font-size: 1.2rem; }}
    .bullet-item {{ background: rgba(96,165,250,0.1); border-left: 4px solid #60a5fa; padding: 1rem; margin-bottom: 0.8rem; border-radius: 8px; line-height: 1.6; }}
    .metadata-box {{ background: rgba(0,0,0,0.2); padding: 1rem; border-radius: 8px; font-family: monospace; font-size: 0.9rem; }}
    .doc-card {{ background: rgba(255,255,255,0.03); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(167,139,250,0.15); margin-bottom: 1rem; }}
    .doc-label {{ color: {ACCENT_COLOR}; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }}
    </style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown(f'<div class="title-banner"><h1>🤖 {APP_NAME}</h1><p>Modular Intelligence & Performance Dash v{VERSION}</p></div>', unsafe_allow_html=True)

# ── Task Selection ──────────────────────────────────────────────────────────
st.markdown('<div class="input-card"><div class="section-header">🎯 Select Agent Task</div>', unsafe_allow_html=True)
task = st.selectbox("", ["Summarize Document", "Compare Documents", "Analyze Bias"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# ── Helper: single document input card ──────────────────────────────────────
def get_doc_input(label, pdf_key, url_key):
    """Render one document input card supporting PDF or URL. Returns (text, source_label)."""
    st.markdown(f'<div class="doc-card"><div class="doc-label">{label}</div>', unsafe_allow_html=True)
    input_type = st.radio(
        "Input type", ["📄 PDF Upload", "🌐 Web URL"],
        horizontal=True, label_visibility="collapsed", key=f"type_{pdf_key}"
    )
    text, source = "", ""
    if input_type == "📄 PDF Upload":
        uf = st.file_uploader("", type=["pdf"], label_visibility="collapsed", key=pdf_key)
        if uf:
            text = pdf_service.extract_text(uf)
            source = uf.name
    else:
        url = st.text_input("", placeholder="https://...", label_visibility="collapsed", key=url_key)
        if url:
            try:
                text = url_service.scrape_url(url)
                source = url
            except RuntimeError as e:
                st.error(f"⚠️ {e}")
    st.markdown('</div>', unsafe_allow_html=True)
    return text, source

# ── Input Area ──────────────────────────────────────────────────────────────
docs, doc_labels, doc_text = [], [], ""

if task in ["Summarize Document", "Analyze Bias"]:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="input-card"><div class="section-header">📄 Upload PDF</div>', unsafe_allow_html=True)
        uf = st.file_uploader("", type=["pdf"], label_visibility="collapsed", key="pdf_up")
        if uf:
            doc_text = pdf_service.extract_text(uf)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="input-card"><div class="section-header">🌐 Web URL</div>', unsafe_allow_html=True)
        url = st.text_input("", placeholder="https://...", label_visibility="collapsed", key="url_in")
        if url:
            try:
                doc_text = url_service.scrape_url(url)
            except RuntimeError as e:
                st.error(f"⚠️ {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    token_len = len(doc_text.split()) if doc_text else 0
    if token_len > 100000:
        st.warning(f"⚠️ **Input too large ({token_len} tokens).** Truncated for performance optimization.")
        doc_text = " ".join(doc_text.split()[:100000])

    docs = [doc_text] if doc_text else []
    doc_labels = ["Document 1"]

elif task == "Compare Documents":
    st.markdown('<div class="input-card"><div class="section-header">📂 Documents to Compare</div>', unsafe_allow_html=True)
    st.caption("Provide 2 documents (required) + an optional third. Mix PDFs and URLs freely.")

    text1, src1 = get_doc_input("📘 Document 1 (Required)", "pdf_1", "url_1")
    text2, src2 = get_doc_input("📗 Document 2 (Required)", "pdf_2", "url_2")

    add_third = st.checkbox("➕ Add a third document (optional)")
    text3, src3 = "", ""
    if add_third:
        text3, src3 = get_doc_input("📙 Document 3 (Optional)", "pdf_3", "url_3")

    st.markdown('</div>', unsafe_allow_html=True)

    for text, src in [(text1, src1), (text2, src2), (text3, src3)]:
        if text.strip():
            docs.append(text)
            doc_labels.append(src if src else f"Document {len(docs)}")

    doc_text = docs[0] if docs else ""

# ── Execution ────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⚡ EXECUTE NEURAL AGENT", use_container_width=True):

    if task == "Compare Documents" and len(docs) < 2:
        st.warning("⚠️ Please provide at least 2 documents to compare.")
        st.stop()
    elif task != "Compare Documents" and not doc_text:
        st.warning("⚠️ Please provide a document or URL first.")
        st.stop()

    cleaned_docs = [preprocessing.clean_text(d) for d in docs]

    with st.spinner("🤖 Neural engine processing..."):
        payload = cleaned_docs if task == "Compare Documents" else cleaned_docs[0]
        res = route_task(task, payload, doc_labels=doc_labels)

        if res["status"] == "success":
            st.markdown("---")
            st.markdown(f"## 📊 {task} Results")

            data = res["data"]
            meta = res["metadata"]

            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Input Size", f"{meta['input_token_length']} tokens")
            with m2:
                st.metric("Execution Time", f"{meta['execution_time']}s")
            with m3:
                if res["task"] == "analyze":
                    st.metric("Confidence", f"{data['confidence']:.1%}")
                elif res["task"] == "compare":
                    st.metric("Similarity", f"{data.get('similarity_score', 'N/A')}%")
                else:
                    st.metric("Status", "Complete")

            # ── Results ─────────────────────────────────────────────────────
            if res["task"] == "summarize":
                t1, t2 = st.tabs(["💡 Summary Bullets", "📋 Structured Table"])
                with t1:
                    for b in data["bullets"]:
                        st.markdown(f'<div class="bullet-item">• {b}</div>', unsafe_allow_html=True)
                with t2:
                    df = pd.DataFrame(data["table_data"])
                    st.dataframe(df, use_container_width=True, hide_index=True)
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button("📥 Download CSV", csv, "genbot_summary.csv", "text/csv")

            elif res["task"] == "compare":
                st.markdown(f"### 🔗 Similarity Score: **{data.get('similarity_score', 'N/A')}%**")
                st.info(data.get("interpretation", ""))

                for label in doc_labels:
                    key = f"unique_to_{label.replace(' ', '_').replace('/', '_')}"
                    points = data.get(key, [])
                    if points:
                        with st.expander(f"📌 Unique points in: {label}"):
                            for p in points:
                                st.markdown(f'<div class="bullet-item">• {p}</div>', unsafe_allow_html=True)

                if "pairwise" in data:
                    st.markdown("### 📊 Pairwise Similarity Matrix")
                    df = pd.DataFrame(data["pairwise"])
                    st.dataframe(df, use_container_width=True)
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button("📥 Download CSV", csv, "genbot_comparison.csv", "text/csv")

            elif res["task"] == "analyze":
                st.markdown(f"### Predicted Focus: **{data['predicted_category']}**")
                st.bar_chart(data["all_scores"])

            with st.expander("🔍 View System Details & Metadata"):
                st.markdown('<div class="metadata-box">', unsafe_allow_html=True)
                st.write(f"**Model Engine:** `{meta['model_name']}`")
                st.write(f"**Execution Speed:** `{meta['execution_time']} seconds`")
                st.write(f"**Raw Token Count:** `{meta['input_token_length']}`")
                st.write(f"**Documents Processed:** `{len(docs)}`")
                st.write(f"**Environment:** `Modular v1.1`")
                st.markdown('</div>', unsafe_allow_html=True)

        elif res["status"] == "placeholder":
            st.info(f"🚧 {res['message']}")
        else:
            st.error(f"❌ Error: {res['message']}")

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<p style='text-align:center; color:#94a3b8;'>GENBOT Modular Intelligence · v1.1 Production Edition</p>", unsafe_allow_html=True)