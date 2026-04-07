"""
ui_labels.py — Multilingual UI Label Translations for GENBOT
Contains all interface strings in 6 languages:
English, Hindi, Telugu, Tamil, Kannada, Malayalam.
"""

# ── UI Labels ─────────────────────────────────────────────────────────────────
# Each key maps to a dict of {language: translated_string}

UI_LABELS = {
    # ── App Header ────────────────────────────────────────────────────────────
    "app_subtitle": {
        "English":   "Modular Intelligence & Performance Dash",
        "Hindi":     "मॉड्यूलर इंटेलिजेंस और प्रदर्शन डैश",
        "Telugu":    "మాడ్యులర్ ఇంటెలిజెన్స్ & పెర్ఫార్మెన్స్ డ్యాష్",
        "Tamil":     "மாட்யூலர் இன்டெலிஜென்ஸ் & பெர்ஃபார்மன்ஸ் டாஷ்",
        "Kannada":   "ಮಾಡ್ಯುಲರ್ ಇಂಟೆಲಿಜೆನ್ಸ್ & ಪರ್ಫಾರ್ಮೆನ್ಸ್ ಡ್ಯಾಶ್",
        "Malayalam":  "മോഡ്യൂലർ ഇന്റലിജൻസ് & പെർഫോമൻസ് ഡാഷ്",
    },

    # ── Task Selection ────────────────────────────────────────────────────────
    "select_task": {
        "English":   "🎯 Select Agent Task",
        "Hindi":     "🎯 एजेंट कार्य चुनें",
        "Telugu":    "🎯 ఏజెంట్ టాస్క్ ఎంచుకోండి",
        "Tamil":     "🎯 ஏஜென்ட் டாஸ்க் தேர்ந்தெடுக்கவும்",
        "Kannada":   "🎯 ಏಜೆಂಟ್ ಕಾರ್ಯ ಆಯ್ಕೆಮಾಡಿ",
        "Malayalam":  "🎯 ഏജന്റ് ടാസ്ക് തിരഞ്ഞെടുക്കുക",
    },

    "task_summarize": {
        "English":   "Summarize Document",
        "Hindi":     "दस्तावेज़ सारांश",
        "Telugu":    "డాక్యుమెంట్ సారాంశం",
        "Tamil":     "ஆவணச் சுருக்கம்",
        "Kannada":   "ಡಾಕ್ಯುಮೆಂಟ್ ಸಾರಾಂಶ",
        "Malayalam":  "ഡോക്യുമെന്റ് സംഗ്രഹം",
    },

    "task_compare": {
        "English":   "Compare Documents",
        "Hindi":     "दस्तावेज़ तुलना",
        "Telugu":    "డాక్యుమెంట్లను పోల్చండి",
        "Tamil":     "ஆவணங்களை ஒப்பிடுக",
        "Kannada":   "ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಹೋಲಿಸಿ",
        "Malayalam":  "ഡോക്യുമെന്റുകൾ താരതമ്യം ചെയ്യുക",
    },

    "task_analyze": {
        "English":   "Analyze Bias",
        "Hindi":     "पूर्वाग्रह विश्लेषण",
        "Telugu":    "పక్షపాత విశ్లేషణ",
        "Tamil":     "சார்பு பகுப்பாய்வு",
        "Kannada":   "ಪಕ್ಷಪಾತ ವಿಶ್ಲೇಷಣೆ",
        "Malayalam":  "പക്ഷപാത വിശകലനം",
    },

    # ── Input Section ─────────────────────────────────────────────────────────
    "upload_pdf": {
        "English":   "📄 Upload PDF",
        "Hindi":     "📄 PDF अपलोड करें",
        "Telugu":    "📄 PDF అప్‌లోడ్ చేయండి",
        "Tamil":     "📄 PDF பதிவேற்றம்",
        "Kannada":   "📄 PDF ಅಪ್‌ಲೋಡ್ ಮಾಡಿ",
        "Malayalam":  "📄 PDF അപ്‌ലോഡ് ചെയ്യുക",
    },

    "web_url": {
        "English":   "🌐 Web URL",
        "Hindi":     "🌐 वेब URL",
        "Telugu":    "🌐 వెబ్ URL",
        "Tamil":     "🌐 వెబ్ URL",
        "Kannada":   "🌐 వెಬ್ URL",
        "Malayalam":  "🌐 వెబ్ URL",
    },

    "docs_to_compare": {
        "English":   "📂 Documents to Compare",
        "Hindi":     "📂 तुलना के लिए दस्तावेज़",
        "Telugu":    "📂 పోల్చడానికి డాక్యుమెంట్లు",
        "Tamil":     "📂 ஒப்பிட ஆவணங்கள்",
        "Kannada":   "📂 ಹೋಲಿಸಲು ಡಾಕ್ಯುಮೆಂಟ್ಗಳು",
        "Malayalam":  "📂 താരതമ്യം ചെയ്യാൻ ഡോക്യുമെൻ്റുകൾ",
    },

    "doc_compare_hint": {
        "English":   "Provide 2 documents (required) + an optional third. Mix PDFs and URLs freely.",
        "Hindi":     "2 दस्तावेज़ (आवश्यक) + एक वैकल्पिक तीसरा। PDF और URL को मिलाएं।",
        "Telugu":    "2 డాక్యుమెంట్లు (తప్పనిసరి) + ఐచ్ఛిక మూడవది. PDF మరియు URLలను కలపండి.",
        "Tamil":     "2 ஆவணங்கள் (கட்டாயம்) + விருப்பமான மூன்றாவது. PDF மற்றும் URLகளை కలக்கவும்.",
        "Kannada":   "2 ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು (ಅಗತ್ಯ) + ಐಚ್ಛಿಕ ಮೂರನೆಯದು. PDF ಮತ್ತು URLಗಳನ್ನು ಮಿಕ್ಸ್ ಮಾಡಿ.",
        "Malayalam":  "2 ഡോക്യുമെൻ്റുകൾ (ആവശ്യം) + ഒരു ഓപ്ഷണൽ മൂന്നാമത്തേത്. PDF, URL കൾ ചേർക്കാം.",
    },

    "doc1_required": {
        "English":   "📘 Document 1 (Required)",
        "Hindi":     "📘 दस्तावेज़ 1 (आवश्यक)",
        "Telugu":    "📘 డాక్యుమెంట్ 1 (తప్పనిసరి)",
        "Tamil":     "📘 ஆவணம் 1 (கட்டாயம்)",
        "Kannada":   "📘 ಡಾಕ್ಯುಮೆಂಟ್ 1 (ಅಗತ್ಯ)",
        "Malayalam":  "📘 ഡോക്യുമെൻ്റ് 1 (ആവശ്യം)",
    },

    "doc2_required": {
        "English":   "📗 Document 2 (Required)",
        "Hindi":     "📗 दस्तावेज़ 2 (आवश्यक)",
        "Telugu":    "📗 డాక్యుమెంట్ 2 (తప్పనిసరి)",
        "Tamil":     "📗 ஆவணம் 2 (கட்டாயம்)",
        "Kannada":   "📗 ಡಾಕ್ಯುಮೆಂಟ್ 2 (ಅಗತ್ಯ)",
        "Malayalam":  "📗 ഡോക്യുമെൻ്റ് 2 (ആവശ്യം)",
    },

    "doc3_optional": {
        "English":   "📙 Document 3 (Optional)",
        "Hindi":     "📙 दस्तावेज़ 3 (वैकल्पिक)",
        "Telugu":    "📙 డాక్యుమెంట్ 3 (ఐచ్ఛికం)",
        "Tamil":     "📙 ஆவணம் 3 (விருப்பம்)",
        "Kannada":   "📙 ಡಾಕ್ಯುಮೆಂಟ್ 3 (ಐಚ್ಛಿಕ)",
        "Malayalam":  "📙 ഡോക്യുമെൻ്റ് 3 (ഓപ്ഷണൽ)",
    },

    "add_third_doc": {
        "English":   "➕ Add a third document (optional)",
        "Hindi":     "➕ तीसरा दस्तावेज़ जोड़ें (वैकल्पिक)",
        "Telugu":    "➕ మూడవ డాక్యుమెంట్ జోడించండి (ఐచ్ఛికం)",
        "Tamil":     "➕ மூன்றாவது ஆவணத்தைச் சேர்க்கவும் (விருப்பம்)",
        "Kannada":   "➕ ಮೂರನೇ ಡಾಕ್ಯುಮೆಂಟ್ ಸೇರಿಸಿ (ಐಚ್ಛಿಕ)",
        "Malayalam":  "➕ മൂന്നാമത്തെ ഡോക്യുമെൻ്റ് ചേർക്കുക (ഓപ്ഷണൽ)",
    },

    "input_type_pdf": {
        "English":   "📄 PDF Upload",
        "Hindi":     "📄 PDF अपलोड",
        "Telugu":    "📄 PDF అప్‌లోడ్",
        "Tamil":     "📄 PDF பதிவேற்றம்",
        "Kannada":   "📄 PDF ಅಪ್‌ಲೋಡ್",
        "Malayalam":  "📄 PDF അപ്‌ലോഡ്",
    },

    "input_type_url": {
        "English":   "🌐 Web URL",
        "Hindi":     "🌐 वेब URL",
        "Telugu":    "🌐 వెబ్ URL",
        "Tamil":     "🌐 வெப் URL",
        "Kannada":   "🌐 ವೆಬ್ URL",
        "Malayalam":  "🌐 വെബ് URL",
    },

    # ── Execution ─────────────────────────────────────────────────────────────
    "execute_button": {
        "English":   "⚡ EXECUTE NEURAL AGENT",
        "Hindi":     "⚡ न्यूरल एजेंट चलाएं",
        "Telugu":    "⚡ న్యూరల్ ఏజెంట్ అమలు చేయండి",
        "Tamil":     "⚡ நியூரல் ஏஜென்ட் இயக்கவும்",
        "Kannada":   "⚡ ನ್ಯೂರಲ್ ಏಜೆಂಟ್ ಎಕ್ಸಿಕ್ಯೂಟ್ ಮಾಡಿ",
        "Malayalam":  "⚡ ന്യൂറൽ ഏജന്റ് എക്സിക്യൂട്ട് ചെയ്യുക",
    },

    "processing": {
        "English":   "🤖 Neural engine processing...",
        "Hindi":     "🤖 न्यूरल इंजन प्रोसेसिंग...",
        "Telugu":    "🤖 న్యూరల్ ఇంజిన్ ప్రాసెసింగ్...",
        "Tamil":     "🤖 நியூரல் இன்ஜின் செயலாக்கம்...",
        "Kannada":   "🤖 ನ್ಯೂರಲ್ ಎಂಜಿನ್ ಪ್ರೊಸೆಸಿಂಗ್...",
        "Malayalam":  "🤖 ന്യൂറൽ എഞ്ചിൻ പ്രോസസ്സിംഗ്...",
    },

    "translating_input": {
        "English":   "🌐 Translating input to English...",
        "Hindi":     "🌐 इनपुट को अंग्रेज़ी में अनुवाद कर रहे हैं...",
        "Telugu":    "🌐 ఇన్‌పుట్‌ను ఆంగ్లంలోకి అనువదిస్తోంది...",
        "Tamil":     "🌐 உள்ளீட்டை ஆங்கிலத்தில் மொழிபெயர்க்கிறது...",
        "Kannada":   "🌐 ಇನ್‌ಪುಟ್ ಅನ್ನು ಇಂಗ್ಲಿಷ್‌ಗೆ ಅನುವಾದಿಸಲಾಗುತ್ತಿದೆ...",
        "Malayalam":  "🌐 ഇൻപുട്ട് ഇംഗ്ലീഷിലേക്ക് വിവർത്തനം ചെയ്യുന്നു...",
    },

    "translating_output": {
        "English":   "🌐 Translating results...",
        "Hindi":     "🌐 परिणाम अनुवाद कर रहे हैं...",
        "Telugu":    "🌐 ఫలితాలను అనువదిస్తోంది...",
        "Tamil":     "🌐 முடிவுகளை மொழிபெயர்க்கிறது...",
        "Kannada":   "🌐 ಫಲಿತಾಂಶಗಳನ್ನು ಅನುವಾದಿಸಲಾಗುತ್ತಿದೆ...",
        "Malayalam":  "🌐 ഫലങ്ങൾ വിവർത്തനം ചെയ്യുന്നു...",
    },

    # ── Warnings / Errors ─────────────────────────────────────────────────────
    "warn_min_docs": {
        "English":   "⚠️ Please provide at least 2 documents to compare.",
        "Hindi":     "⚠️ कृपया तुलना के लिए कम से कम 2 दस्तावेज़ प्रदान करें।",
        "Telugu":    "⚠️ దయచేసి పోల్చడానికి కనీసం 2 డాక్యుమెంట్లు అందించండి.",
        "Tamil":     "⚠️ ஒப்பிட குறைந்தது 2 ஆவணங்களை வழங்கவும்.",
        "Kannada":   "⚠️ ಹೋಲಿಸಲು ಕನಿಷ್ಠ 2 ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಒದಗಿಸಿ.",
        "Malayalam":  "⚠️ താരതമ്യം ചെയ്യാൻ കുറഞ്ഞത് 2 ഡോക്യുമെന്റുകൾ നൽകുക.",
    },

    "warn_no_doc": {
        "English":   "⚠️ Please provide a document or URL first.",
        "Hindi":     "⚠️ कृपया पहले एक दस्तावेज़ या URL प्रदान करें।",
        "Telugu":    "⚠️ దయచేసి ముందుగా డాక్యుమెంట్ లేదా URL అందించండి.",
        "Tamil":     "⚠️ முதலில் ஒரு ஆவணம் அல்லது URL வழங்கவும்.",
        "Kannada":   "⚠️ దయవిಟ್ಟು మొದಲು ಡಾಕ್ಯುಮೆಂಟ್ ಅಥವಾ URL ಒದಗಿಸಿ.",
        "Malayalam":  "⚠️ ആദ്യം ഒരു ഡോക്യുമെന്റ് അല്ലെങ്കിൽ URL നൽകുക.",
    },

    "warn_too_large": {
        "English":   "⚠️ **Input too large ({tokens} tokens).** Truncated for performance.",
        "Hindi":     "⚠️ **इनपुट बहुत बड़ा ({tokens} टोकन).** प्रदर्शन के लिए छोटा किया गया।",
        "Telugu":    "⚠️ **ఇన్‌పుట్ చాలా పెద్దది ({tokens} టోకెన్లు).** పనితీరు కోసం కత్తిరించబడింది.",
        "Tamil":     "⚠️ **உள்ளீடு மிகப் பெரியது ({tokens} டோக்கன்கள்).** செயல்திறனுக்காக வெட்டப்பட்டது.",
        "Kannada":   "⚠️ **ಇನ್‌ಪುಟ್ ತುಂಬಾ ದೊಡ್ಡದು ({tokens} ಟೋಕನ್‌ಗಳು).** ಕಾರ್ಯಕ್ಷಮತೆಗಾಗಿ ಕತ್ತರಿಸಲಾಗಿದೆ.",
        "Malayalam":  "⚠️ **ഇൻപുട്ട് വളരെ വലുതാണ് ({tokens} ടോക്കണുകൾ).** പ്രകടനത്തിനായി ചുരുക്കി.",
    },

    # ── Results ───────────────────────────────────────────────────────────────
    "results_title": {
        "English":   "📊 {task} Results",
        "Hindi":     "📊 {task} परिणाम",
        "Telugu":    "📊 {task} ఫలితాలు",
        "Tamil":     "📊 {task} முடிவுகள்",
        "Kannada":   "📊 {task} ಫಲಿತಾಂಶಗಳು",
        "Malayalam":  "📊 {task} ഫലങ്ങൾ",
    },

    "metric_input_size": {
        "English":   "Input Size",
        "Hindi":     "इनपुट आकार",
        "Telugu":    "ఇన్‌పుట్ పరిమాణం",
        "Tamil":     "உள்ளீடு அளவு",
        "Kannada":   "ಇನ್‌ಪುಟ್ ಗಾತ್ರ",
        "Malayalam":  "ഇൻപുട്ട് വലിപ്പം",
    },

    "metric_exec_time": {
        "English":   "Execution Time",
        "Hindi":     "निष्पादन समय",
        "Telugu":    "అమలు సమయం",
        "Tamil":     "செயலாக்க நேரம்",
        "Kannada":   "ಕಾರ್ಯಗತ ಸಮಯ",
        "Malayalam":  "എക്സിക്യൂഷൻ സമയം",
    },

    "metric_confidence": {
        "English":   "Confidence",
        "Hindi":     "विश्वास स्तर",
        "Telugu":    "నమ్మకం",
        "Tamil":     "நம்பகத்தன்மை",
        "Kannada":   "ವಿಶ್ವಾಸ",
        "Malayalam":  "വിശ്വാസ്യത",
    },

    "metric_similarity": {
        "English":   "Similarity",
        "Hindi":     "समानता",
        "Telugu":    "సారూప్యత",
        "Tamil":     "ஒற்றுமை",
        "Kannada":   "ಸಮಾನತೆ",
        "Malayalam":  "സാമ്യത",
    },

    "metric_status_complete": {
        "English":   "Complete",
        "Hindi":     "पूर्ण",
        "Telugu":    "పూర్తయింది",
        "Tamil":     "முடிந்தது",
        "Kannada":   "ಪೂರ್ಣ",
        "Malayalam":  "പൂർത്തിയായി",
    },

    "tab_bullets": {
        "English":   "💡 Summary Bullets",
        "Hindi":     "💡 सारांश बिंदु",
        "Telugu":    "💡 సారాంశ బుల్లెట్లు",
        "Tamil":     "💡 சுருக்க புள்ளிகள்",
        "Kannada":   "💡 ಸಾರಾಂಶ ಬುಲೆಟ್‌ಗಳು",
        "Malayalam":  "💡 സംഗ്രഹ ബുള്ളറ്റുകൾ",
    },

    "tab_table": {
        "English":   "📋 Structured Table",
        "Hindi":     "📋 संरचित तालिका",
        "Telugu":    "📋 నిర్మాణాత్మక పట్టిక",
        "Tamil":     "📋 கட்டமைக்கப்பட்ட அட்டவணை",
        "Kannada":   "📋 ರಚನಾತ್ಮಕ ಕೋಷ್ಟಕ",
        "Malayalam":  "📋 ഘടനാപരമായ പട്ടിക",
    },

    "download_csv": {
        "English":   "📥 Download CSV",
        "Hindi":     "📥 CSV डाउनलोड करें",
        "Telugu":    "📥 CSV డౌన్‌లోడ్ చేయండి",
        "Tamil":     "📥 CSV பதிவிறக்கம்",
        "Kannada":   "📥 CSV ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "Malayalam":  "📥 CSV ഡൗൺലോഡ് ചെയ്യുക",
    },

    "similarity_score_label": {
        "English":   "🔗 Similarity Score",
        "Hindi":     "🔗 समानता स्कोर",
        "Telugu":    "🔗 సారూప్యత స్కోర్",
        "Tamil":     "🔗 ஒற்றுமை மதிப்பெண்",
        "Kannada":   "🔗 ಸಮಾನತೆ ಸ್ಕೋರ್",
        "Malayalam":  "🔗 സാമ്യത സ്കോർ",
    },

    "unique_points_in": {
        "English":   "📌 Unique points in: {label}",
        "Hindi":     "📌 अनूठे बिंदु: {label}",
        "Telugu":    "📌 ప్రత్యేక అంశాలు: {label}",
        "Tamil":     "📌 தனித்துவ புள்ளிகள்: {label}",
        "Kannada":   "📌 ವಿಶಿಷ್ಟ ಅಂಶಗಳು: {label}",
        "Malayalam":  "📌 അതുല്യ പോയിന്റുകൾ: {label}",
    },

    "pairwise_matrix": {
        "English":   "📊 Pairwise Similarity Matrix",
        "Hindi":     "📊 जोड़ीवार समानता मैट्रिक्स",
        "Telugu":    "📊 జతల సారూప్యత మ్యాట్రిక్స్",
        "Tamil":     "📊 இணை ஒற்றுமை மேட்ரிக்ஸ்",
        "Kannada":   "📊 ಜೋಡಿ ಸಮಾನತೆ ಮ್ಯಾಟ್ರಿಕ್ಸ್",
        "Malayalam":  "📊 ജോഡി സാമ്യത മാട്രിക്സ്",
    },

    "predicted_focus": {
        "English":   "Predicted Focus",
        "Hindi":     "अनुमानित फोकस",
        "Telugu":    "అంచనా వేసిన దృష్టి",
        "Tamil":     "கணிக்கப்பட்ட கவனம்",
        "Kannada":   "ಊಹಿಸಲಾದ ಗಮನ",
        "Malayalam":  "പ്രവചിച്ച ഫോക്കസ്",
    },

    "system_details": {
        "English":   "🔍 View System Details & Metadata",
        "Hindi":     "🔍 सिस्टम विवरण और मेटाडेटा देखें",
        "Telugu":    "🔍 సిస్టమ్ వివరాలు & మెటాడేటా చూడండి",
        "Tamil":     "🔍 கணினி விவரங்கள் & மெட்டாடேட்டா பார்க்க",
        "Kannada":   "🔍 ಸಿಸ್ಟಮ್ ವಿವರಗಳು & ಮೆಟಾಡೇಟಾ ನೋಡಿ",
        "Malayalam":  "🔍 സിസ്റ്റം വിശദാംശങ്ങൾ & മെറ്റാഡേറ്റ കാണുക",
    },

    # ── Sidebar ───────────────────────────────────────────────────────────────
    "language_selector": {
        "English":   "🌐 Interface Language",
        "Hindi":     "🌐 इंटरफ़ेस भाषा",
        "Telugu":    "🌐 ఇంటర్ఫేస్ భాష",
        "Tamil":     "🌐 இடைமுக மொழி",
        "Kannada":   "🌐 ಇಂಟರ್ಫೇಸ್ ಭಾಷೆ",
        "Malayalam":  "🌐 ഇന്റർഫേസ് ഭാഷ",
    },

    "language_note": {
        "English":   "Documents in {lang} will be automatically translated for processing.",
        "Hindi":     "{lang} में दस्तावेज़ स्वचालित रूप से प्रोसेसिंग के लिए अनुवादित होंगे।",
        "Telugu":    "{lang} లో డాక్యుమెంట్లు ప్రాసెసింగ్ కోసం స్వయంచాలకంగా అనువదించబడతాయి.",
        "Tamil":     "{lang} ஆவணங்கள் செயலாக்கத்திற்காக தானாகவே மொழிபெயர்க்கப்படும்.",
        "Kannada":   "{lang} ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು ಪ್ರೊಸೆಸಿಂಗ್‌ಗಾಗಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಿಸಲ್ಪಡುತ್ತವೆ.",
        "Malayalam":  "{lang} ഡോക്യുമെന്റുകൾ പ്രോസസ്സിംഗിനായി സ്വയമേവ വിവർത്തനം ചെയ്യപ്പെടും.",
    },

    # ── Footer ────────────────────────────────────────────────────────────────
    "footer": {
        "English":   "GENBOT Modular Intelligence · v1.1 Production Edition",
        "Hindi":     "GENBOT मॉड्यूलर इंटेलिजेंस · v1.1 प्रोडक्शन",
        "Telugu":    "GENBOT మాడ్యులర్ ఇంటెలిజెన్స్ · v1.1 ప్రొడక్షన్",
        "Tamil":     "GENBOT மாட்யூலர் இன்டெலிஜென்ஸ் · v1.1 புரொடக்ஷன்",
        "Kannada":   "GENBOT ಮಾಡ್ಯುಲರ್ ಇಂಟೆಲಿಜೆನ್ಸ್ · v1.1 ಪ್ರೊಡಕ್ಷನ್",
        "Malayalam":  "GENBOT മോഡ്യൂലർ ഇന്റലിജൻസ് · v1.1 പ്രൊഡക്ഷൻ",
    },

    # ── Sidebar Navigation ──────────────────────────────────────────────────
    "nav_dashboard": {
        "English":   "🏠 Dashboard",
        "Hindi":     "🏠 डैशबोर्ड",
        "Telugu":    "🏠 డ్యాష్‌బోర్డ్",
        "Tamil":     "🏠 டாஷ்போர்டு",
        "Kannada":   "🏠 ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "Malayalam":  "🏠 ഡാഷ്‌ബോർഡ്",
    },
    "nav_summarize": {
        "English":   "📄 Summarize Document",
        "Hindi":     "📄 दस्तावेज़ सारांश",
        "Telugu":    "📄 డాక్యుమెంట్ సారాంశం",
        "Tamil":     "📄 ஆவண சுருக்கம்",
        "Kannada":   "📄 ಡಾಕ್ಯುಮೆಂಟ್ ಸಾರಾಂಶ",
        "Malayalam":  "📄 ഡോക്യുമെന്റ് സംഗ്രഹം",
    },
    "nav_compare": {
        "English":   "⚖️ Compare Manifestos",
        "Hindi":     "⚖️ घोषणापत्र तुलना",
        "Telugu":    "⚖️ మేనిఫెస్టోలను పోల్చండి",
        "Tamil":     "⚖️ தேர்தல் அறிக்கைகளை ஒப்பிடுக",
        "Sentence":  "⚖️ ప్రణాళికలను హోలించి",
        "Kannada":   "⚖️ ಪ್ರಣಾಳಿಕೆಗಳನ್ನು ಹೋಲಿಸಿ",
        "Malayalam":  "⚖️ മാനിഫെസ്റ്റോകൾ താരതമ്യം ചെയ്യുക",
    },
    "nav_bias": {
        "English":   "🔍 Bias Detection",
        "Hindi":     "🔍 पूर्वाग्रह पहचान",
        "Telugu":    "🔍 పక్షపాత గుర్తింపు",
        "Tamil":     "🔍 சார்பு கண்டறிதல்",
        "Kannada":   "🔍 ಪಕ್ಷಪಾತ ಪತ್ತೆಹಚ್ಚುವಿಕೆ",
        "Malayalam":  "🔍 പക്ഷപാതം കണ്ടെത്തൽ",
    },
    "nav_lang": {
        "English":   "🌐 Language Setting",
        "Hindi":     "🌐 भाषा सेटिंग",
        "Telugu":    "🌐 భాష సెట్టింగ్",
        "Tamil":     "🌐 மொழி அமைப்பு",
        "Kannada":   "🌐 ಭಾಷಾ ಸೆಟ್ಟಿಂಗ್",
        "Malayalam":  "🌐 ഭാഷാ ക്രമീകരണം",
    },
    "nav_history": {
        "English":   "📊 Service History",
        "Hindi":     "📊 सेवा इतिहास",
        "Telugu":    "📊 సర్వీస్ హిస్టరీ",
        "Tamil":     "📊 சேவை வரலாறு",
        "Kannada":   "📊 ಸೇವಾ ಇತಿಹಾಸ",
        "Malayalam":  "📊 സേവന ചരിത്രം",
    },
    "nav_about": {
        "English":   "ℹ️ About Portal",
        "Hindi":     "ℹ️ पोर्टल के बारे में",
        "Telugu":    "ℹ️ పోర్టల్ గురించి",
        "Tamil":     "ℹ️ போர்டல் பற்றி",
        "Kannada":   "ℹ️ ಪೋರ್ಟಲ್ ಬಗ್ಗೆ",
        "Malayalam":  "ℹ️ പോർട്ടലിനെക്കുറിച്ച്",
    },

    # ── Dashboard Content ────────────────────────────────────────────────────
    "dash_hero_title": {
        "English":   "Strategic Intelligence Portal",
        "Hindi":     "रणनीतिक खुफिया पोर्टल",
        "Telugu":    "వ్యూహాత్మక ఇంటెలిజెన్స్ పోర్టల్",
        "Tamil":     "மூலோபாய நுண்ணறிவு போர்டல்",
        "Kannada":   "ಕಾರ್ಯತಂತ್ರದ ಬುದ್ಧಿವಂತಿಕೆ ಪೋರ್ಟಲ್",
        "Malayalam":  "സ്ട്രാറ്റജിക് ഇൻ്റലിജൻസ് പോർട്ടൽ",
    },
    "dash_hero_subtitle": {
        "English":   "National Strategic Document Analysis & Policy Insights Portal",
        "Hindi":     "राष्ट्रीय रणनीतिक दस्तावेज़ विश्लेषण और नीति अंतर्दृष्टि पोर्टल",
        "Telugu":    "జాతీయ వ్యూహాత్మక పత్ర విశ్లేషణ & పాలసీ అంతర్దృష్తుల పోర్టల్",
        "Tamil":     "தேசிய மூலோபாய ஆவண பகுப்பாய்வு மற்றும் கொள்கை நுண்ணறிவு போர்டல்",
        "Kannada":   "ರಾಷ್ಟ್ರೀಯ ಕಾರ್ಯತಂತ್ರದ ದಾಖಲೆ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ನೀತಿ ಒಳನೋಟಗಳ ಪೋರ್ಟಲ್",
        "Malayalam":  "ദേശീയ സ്ട്രാറ്റജിക് ഡോക്യുമെന്റ് വിശകലനവും പോളിസി ഇൻസൈറ്റുകളും",
    },
    "dash_total_analyses": {
        "English":   "Total Analyses Processed",
        "Hindi":     "कुल प्रसंस्कृत विश्लेषण",
        "Telugu":    "మొత్తం విశ్లేషణలు",
        "Tamil":     "மொத்த பகுப்பாய்வுகள்",
        "Kannada":   "ಒಟ್ಟು ವಿಶ್ಲೇಷಣೆಗಳು",
        "Malayalam":  "ആകെ വിശകലനങ്ങൾ",
    },
    "dash_policy_summaries": {
        "English":   "Active Policy Summaries",
        "Hindi":     "सक्रिय नीति सारांश",
        "Telugu":    "పాలసీ సారాంశాలు",
        "Tamil":     "கொள்கை சுருக்கங்கள்",
        "Kannada":   "ನೀತಿ ಸಾರಾಂಶಗಳು",
        "Malayalam":  "പോളിസി സംഗ്രഹങ്ങൾ",
    },
    "dash_manifesto_comparisons": {
        "English":   "Manifesto Comparisons",
        "Hindi":     "घोषणापत्र तुलना",
        "Telugu":    "మేనిఫెస్టో పోలికలు",
        "Tamil":     "தேர்தல் அறிக்கை ஒப்பீடுகள்",
        "Kannada":   "ಪ್ರಣಾಳಿಕೆ ಹೋಲಿಕೆಗಳು",
        "Malayalam":  "മാനിഫെസ്റ്റോ താരതമ്യങ്ങൾ",
    },
    "dash_mandate_title": {
        "English":   "📋 Division Mandate",
        "Hindi":     "📋 विभाग का जनादेश",
        "Telugu":    "📋 విభాగాదేశం",
        "Tamil":     "📋 பிரிவு ஆணை",
        "Kannada":   "📋 ವಿಭಾಗದ ಆದೇಶ",
        "Malayalam":  "📋 ഡിവിഷൻ മാൻഡേറ്റ്",
    },
    "dash_mandate_text": {
        "English":   "The **GENBOT Strategic Intelligence Division** is designed to provide high-speed, multi-lingual document intelligence for policy makers. Our current capabilities include deep neural summarization, pairwise policy comparison, and zero-shot bias detection across Indian languages.",
        "Hindi":     "**GENBOT रणनीतिक खुफिया विभाग** नीति निर्माताओं के लिए उच्च गति, बहुभाषी दस्तावेज़ खुफिया प्रदान करने के लिए डिज़ाइन किया गया है। हमारी वर्तमान क्षमताओं में गहरी तंत्रिका सारांश, जोड़ीवार नीति तुलना और भारतीय भाषाओं में शून्य-शॉट पूर्वाग्रह पहचान शामिल है।",
        "Telugu":    "**GENBOT వ్యూహాత్మక ఇంటెలిజెన్స్ విభాగం** విధాన నిర్ణేతల కోసం హై-స్పీడ్, బహుభాషా డాక్యుమెంట్ ఇంటెలిజెన్స్‌ను అందించడానికి రూపొందించబడింది. మా ప్రస్తుత సామర్థ్యాలలో లోతైన న్యూరల్ సారాంశం, జతల పాలసీ పోలిక మరియు భారతీయ భాషలలో పక్షపాత గుర్తింపు ఉన్నాయి.",
        "Tamil":     "**GENBOT மூலோபாய நுண்ணறிவுப் பிரிவு** கொள்கை வகுப்பாளர்களுக்காக அதிவேக, பல மொழி ஆவண நுண்ணறிவை வழங்க வடிவமைக்கப்பட்டுள்ளது. எங்களது தற்போதைய திறன்களில் ஆழ்ந்த நியூரல் சுருக்கம், கொள்கை ஒப்பீடு மற்றும் இந்திய மொழிகளில் சார்பு கண்டறிதல் ஆகியவை அடங்கும்.",
        "Kannada":   "**GENBOT ಕಾರ್ಯತಂತ್ರದ ಬುದ್ಧಿವಂತಿಕೆ ವಿಭಾಗವು** ನೀತಿ ನಿರೂಪಕರಿಗೆ ಹೈ-ಸ್ಪೀಡ್, ಬಹು-ಭಾಷಾ ದಾಖಲೆ ಬುದ್ಧಿವಂತಿಕೆಯನ್ನು ಒದಗಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. ನಮ್ಮ ಪ್ರಸ್ತುತ ಸಾಮರ್ಥ್ಯಗಳು ಆಳವಾದ ನರ ಸಾರಾಂಶ, ಜೋಡಿ ನೀತಿ ಹೋಲಿಕೆ ಮತ್ತು ಪಕ್ಷಪಾತ ಪತ್ತೆಹಚ್ಚುವಿಕೆಯನ್ನು ಒಳಗೊಂಡಿವೆ.",
        "Malayalam":  "**GENBOT സ്ട്രാറ്റജിക് ഇൻ്റലിജൻസ് ഡിവിഷൻ** പോളിസി മേക്കർമാർക്കായി അതിവേഗത്തിലുള്ള ബഹുഭാഷാ ഡോക്യുമെന്റേഷൻ ഇൻ്റലിജൻസ് നൽകുന്നതിനായിട്ടാണ് രൂപകൽപ്പന ചെയ്തിരിക്കുന്നത്. നിലവിലെ കഴിവുകളിൽ ന്യൂറൽ സമ്മറൈസേഷൻ, പോളിസി താരതമ്യം, പക്ഷപാതം കണ്ടെത്തൽ എന്നിവ ഉൾപ്പെടുന്നു.",
    },

    # ── Bureau Page Labels ───────────────────────────────────────────────────
    "sum_page_title": {
        "English":   "📄 Document Summarization",
        "Hindi":     "📄 दस्तावेज़ सारांश",
        "Telugu":    "📄 డాక్యుమెంట్ సారాంశం",
        "Tamil":     "📄 ஆவண சுருக்கம்",
        "Kannada":   "📄 ಡಾಕ್ಯುಮೆಂಟ್ ಸಾರಾಂಶ",
        "Malayalam":  "📄 ഡോക്യുമെന്റ് സംഗ്രഹം",
    },
    "sum_page_subtitle": {
        "English":   "Official Bureau for Summarizing Strategic Documents",
        "Hindi":     "रणनीतिक दस्तावेजों के सारांश के लिए आधिकारिक ब्यूरो",
        "Telugu":    "వ్యూహాత్మక పత్రాల సారాంశం కోసం అధికారిక బ్యూరో",
        "Tamil":     "மூலோபாய ஆவணங்களைச் சுருக்க அதிகாரப்பூர்வப் பிரிவு",
        "Kannada":   "ಕಾರ್ಯತಂತ್ರದ ದಾಖಲೆಗಳನ್ನು ಸಂಕ್ಷಿಪ್ತಗೊಳಿಸಲು ಅಧಿಕೃತ ಬ್ಯೂರೋ",
        "Malayalam":  "സ്ട്രാറ്റജിക് ഡോക്യുമെന്റുകൾ സംഗ്രഹിക്കുന്നതിനുള്ള ഔദ്യോഗിക ബ്യൂറോ",
    },
    "pdf_source_header": {
        "English":   "📤 PDF Source",
        "Hindi":     "📤 PDF स्रोत",
        "Telugu":    "📤 PDF మూలం",
        "Tamil":     "📤 PDF ஆதாரம்",
        "Kannada":   "📤 PDF ಮೂಲ",
        "Malayalam":  "📤 PDF സോഴ്സ്",
    },
    "web_source_header": {
        "English":   "🔗 Web Intelligence (URL)",
        "Hindi":     "🔗 वेब इंटेलिजेंस (URL)",
        "Telugu":    "🔗 వెబ్ ఇంటెలిజెన్స్ (URL)",
        "Tamil":     "🔗 వెబ్ நுண்ணறிவு (URL)",
        "Kannada":   "🔗 వెಬ್ ಇಂಟೆಲಿಜೆನ್ಸ್ (URL)",
        "Malayalam":  "🔗 వెബ് ഇൻ്റലിജൻസ് (URL)",
    },
    "btn_summary": {
        "English":   "🚀 Process Bureau Summary",
        "Hindi":     "🚀 ब्यूरो सारांश संसाधित करें",
        "Telugu":    "🚀 బ్యూరో సారాంశం ప్రాసెస్ చేయండి",
        "Tamil":     "🚀 பிரிவு சுருக்கத்தைச் செயல்படுத்தவும்",
        "Kannada":   "🚀 ಬ್ಯೂರೋ సారాంశాన్ని ప్రక్రయెగెూళెసి",
        "Malayalam":  "🚀 ബ്യൂറോ സംഗ്രഹം പ്രോസസ്സ് ചെയ്യുക",
    },
    "comp_page_title": {
        "English":   "⚖️ Compare Manifestos",
        "Hindi":     "⚖️ घोषणापत्र तुलना",
        "Telugu":    "⚖️ మేనిఫెస్టోలను పోల్చండి",
        "Tamil":     "⚖️ தேர்தல் அறிக்கைகளை ஒப்பிடுக",
        "Kannada":   "⚖️ ಪ್ರಣಾಳಿಕೆಗಳನ್ನು ಹೋಲಿಸಿ",
        "Malayalam":  "⚖️ മാനിഫెസ്റ്റോകൾ താരതമ്യം ചെയ്യുക",
    },
    "comp_page_subtitle": {
        "English":   "Cross-Policy Analysis Bureau",
        "Hindi":     "क्रॉस-पॉलिसी विश्लेषण ब्यूरो",
        "Telugu":    "క్రాస్-పాలసీ విశ్లేషణ బ్యూరో",
        "Tamil":     "கொள்கை பகுப்பாய்வு பிரிவு",
        "Kannada":   "ನೀತಿ ವಿಶ್ಲೇಷಣಾ ಬ್ಯೂರೋ",
        "Malayalam":  "ക്രോസ്-പോളിസി അനാലിസിസ് ബ്യൂറോ",
    },
    "btn_compare": {
        "English":   "⚖️ Run Comparative Bureau Analysis",
        "Hindi":     "⚖️ तुलनात्मक ब्यूरो विश्लेषण चलाएं",
        "Telugu":    "⚖️ తులనాత్మక విశ్లేషణ అమలు చేయండి",
        "Tamil":     "⚖️ ஒப்பீட்டு பகுாய்வு இயக்கவும்",
        "Kannada":   "⚖️ ತುಲನಾತ್ಮಕ ವಿಶ್ಲೇಷಣೆ ನಡೆಸಿ",
        "Malayalam":  "⚖️ താരതമ്യ വിശകലനം നടത്തുക",
    },
    "policy_a": {
        "English":   "Policy A",
        "Hindi":     "नीति A",
        "Telugu":    "పాలసీ A",
        "Tamil":     "கொள்கை A",
        "Kannada":   "ನೀತಿ A",
        "Malayalam":  "പോളിസി A",
    },
    "policy_b": {
        "English":   "Policy B",
        "Hindi":     "नीति B",
        "Telugu":    "పాలసీ B",
        "Tamil":     "கொள்கை B",
        "Kannada":   "ನೀತಿ B",
        "Malayalam":  "പോളിസി B",
    },
    "bias_page_title": {
        "English":   "🔍 Bias Detection",
        "Hindi":     "🔍 पूर्वाग्रह पहचान",
        "Telugu":    "🔍 పక్షపాత గుర్తింపు",
        "Tamil":     "🔍 சார்பு கண்டறிதல்",
        "Kannada":   "🔍 ಪಕ್ಷಪಾತ ಪತ್ತೆಹಚ್ಚುವಿಕೆ",
        "Malayalam":  "🔍 പക്ഷപാതം കണ്ടെത്തൽ",
    },
    "bias_page_subtitle": {
        "English":   "Intelligence Bureau for Political & Ideological Analysis",
        "Hindi":     "राजनीतिक और वैचारिक विश्लेषण के लिए खुफिया ब्यूरो",
        "Telugu":    "రాజకీయ & సైద్ధాంతిక విశ్లేషణ కోసం ఇంటెలిజెన్స్ బ్యూరో",
        "Tamil":     "அரசியல் மற்றும் கருத்தியல் பகுப்பாய்வு பிரிவு",
        "Kannada":   "ರಾಷ್ಟ್ರೀಯ ಕಾರ್ಯತಂತ್ರದ ದಾಖಲೆ ವಿಶ್ಲೇಷಣೆ ಮತ್ತು ನೀತಿ ಒಳನೋಟಗಳ ಪೋರ್ಟಲ್",
        "Malayalam":  "രാഷ്ട്രീയ-ആദർശ വിശകലനത്തിനുള്ള ഇൻ്റലിജൻസ് బ్యూరో",
    },
    "btn_bias": {
        "English":   "⚖️ Detect Bias / Focus",
        "Hindi":     "⚖️ पूर्वाग्रह / फोकस पहचानें",
        "Telugu":    "🔍 పక్షపాతం / దృష్టిని గుర్తించండి",
        "Tamil":     "🔍 சார்பு / கவனத்தை கண்டறி",
        "Kannada":   "🔍 ಪಕ್ಷಪಾತ / ಗಮನ ಪತ್ತೆಹಚ್ಚಿ",
        "Malayalam":  "🔍 പക്ഷപാതം / ഫോക്കസ് കണ്ടെത്തുക",
    },
    "hist_page_title": {
        "English":   "📊 Service Ledger",
        "Hindi":     "📊 सेवा इतिहास लेजर",
        "Telugu":    "📊 సర్వీస్ లెడ్జర్",
        "Tamil":     "📊 சேவை பதிவேடு",
        "Kannada":   "📊 ಸೇವಾ ಲೆಡ್ಜರ್",
        "Malayalam":  "📊 സേവന ലെഡ്ജർ",
    },
    "hist_page_subtitle": {
        "English":   "Persistent Audit Trail for Documentation Tasks",
        "Hindi":     "प्रलेखन कार्यों के लिए ऑडिट ट्रेल",
        "Telugu":    "డాక్యుమెంటేషన్ టాస్క్‌ల కోసం ఆడిట్ ట్రైల్",
        "Tamil":     "ஆவணப் பணிகளுக்கான தணிக்கைத் தடம்",
        "Kannada":   "ದಾಖಲಾತಿ ಕಾರ್ಯಗಳಿಗಾಗಿ ಆಡಿಟ್ ಟ್ರಯಲ್",
        "Malayalam":  "ഡോക്യുമെന്റേഷൻ ടാസ്ക്കുകൾക്കായുള്ള ഓഡിറ്റ് ട്രയൽ",
    },
    "hist_empty": {
        "English":   "🏢 Bureau history is currently empty. Process documents to log activity.",
        "Hindi":     "🏢 ब्यूरो इतिहास वर्तमान में खाली है। गतिविधि लॉग करने के लिए दस्तावेज़ संसाधित करें।",
        "Telugu":    "🏢 బ్యూరో చరిత్ర ప్రస్తుతం ఖాళీగా ఉంది. కార్యాచరణను లాగ్ చేయడానికి డాక్యుమెంట్‌లను ప్రాసెస్ చేయండి.",
        "Tamil":     "🏢 பிரிவு வரலாறு காலியாக உள்ளது. செயல்பாட்டை பதிவு செய்ய ஆவணங்களைச் செயல்படுத்தவும்.",
        "Kannada":   "🏢 ಬ್ಯೂರೋ ಇತಿಹಾಸವು ಪ್ರಸ್ತುತ ಖಾಲಿಯಿದೆ. ಚಟುವಟಿಕೆಯನ್ನು ದಾಖಲಿಸಲು ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ.",
        "Malayalam":  "🏢 ബ്യൂറോ ഹിസ്റ്ററി നിലവിൽ ശൂന്യമാണ്. ആക്റ്റീവിറ്റി ലോഗ് ചെയ്യാൻ ഡോക്യുമെന്റുകൾ പ്രോസസ്സ് ചെയ്യുക.",
    },
    "btn_clear_ledger": {
        "English":   "🗑️ Clear Bureau Ledger",
        "Hindi":     "🗑️ ब्यूरो लेजर साफ़ करें",
        "Telugu":    "🗑️ బ్యూరో లెడ్జర్ క్లియర్ చేయండి",
        "Tamil":     "🗑️ பதிவேட்டை அழிக்கவும்",
        "Kannada":   "🗑️ ಬ್ಯೂರೋ ಲೆಡ್ಜರ್ ತೆರವುಗೊಳಿಸಿ",
        "Malayalam":  "🗑️ ബ്യൂറോ ലെഡ്ജർ മായ്ക്കുക",
    },
    "lang_page_title": {
        "English":   "🌐 Language Bureau",
        "Hindi":     "🌐 भाषा ब्यूरो",
        "Telugu":    "🌐 భాషా బ్యూరో",
        "Tamil":     "🌐 மொழிப் பிரிவு",
        "Kannada":   "🌐 భాషా బ్యూರೋ",
        "Malayalam":  "🌐 ഭാഷാ బ్యూరో",
    },
    "lang_page_subtitle": {
        "English":   "Multilingual Configuration Center",
        "Hindi":     "बहुभाषी कॉन्फ़िगरेशन केंद्र",
        "Telugu":    "బహుభాషా కాన్ఫిగరేషన్ సెంటర్",
        "Tamil":     "பல்மொழி கட்டமைப்பு மையம்",
        "Kannada":   "ಬಹುಭಾಷಾ ಕಾನ್ಫಿಗರೇಶನ್ ಸೆಂಟರ್",
        "Malayalam":  "ബഹുഭാഷാ കോൺഫിഗറേഷൻ സെന്റർ",
    },
    "lang_current_prefix": {
        "English":   "Current language set to",
        "Hindi":     "वर्तमान भाषा सेट है",
        "Telugu":    "ప్రస్తుత భాష",
        "Tamil":     "தற்போதைய மொழி",
        "Kannada":   "ಪ್ರస్తుತ ಭಾಷೆ",
        "Malayalam":  "നിലവിലെ ഭാഷ",
    },
    "about_page_title": {
        "English":   "ℹ️ Bureau Information",
        "Hindi":     "ℹ️ ब्यूरो जानकारी",
        "Telugu":    "ℹ️ బ్యూరో సమాచారం",
        "Tamil":     "ℹ️ பிரிவு தகவல்",
        "Kannada":   "ℹ️ ಬ್ಯೂರೋ ಮಾಹಿತಿ",
        "Malayalam":  "ℹ️ ബ്യൂറോ വിവരങ്ങൾ",
    },
    "about_page_subtitle": {
        "English":   "Strategic Intelligence Division - Official Portal Info",
        "Hindi":     "रणनीतिक खुफिया विभाग - आधिकारिक पोर्टल जानकारी",
        "Telugu":    "వ్యూహాత్మక ఇంటెలిజెన్స్ విభాగం - అధికారిక పోర్టల్ సమాచారం",
        "Tamil":     "மூலோபாய நுண்ணறிவு பிரிவு - அதிகாரப்பூர்வ போர்டல் தகவல்",
        "Kannada":   "ಕಾರ್ಯತಂತ್ರದ ಬುದ್ಧಿವಂತಿಕೆ ವಿಭಾಗ - ಅಧಿಕೃತ ಪೋರ್ಟಲ್ ಮಾಹಿತಿ",
        "Malayalam":  "സ്ട്രാറ്റജിക് ഇൻ്റലിജൻസ് ഡിവിഷൻ - ഔദ്യോഗിക വിവരങ്ങൾ",
    },
}


def get_label(key: str, language: str = "English", **kwargs) -> str:
    """
    Get a translated UI label.

    Args:
        key:      Label key from UI_LABELS.
        language: Target language name.
        **kwargs: Format variables (e.g. task="Summarize", tokens=1000).

    Returns:
        Translated string, with fallback to English if not found.
    """
    label_dict = UI_LABELS.get(key, {})
    text = label_dict.get(language, label_dict.get("English", key))

    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass  # return unformatted if format args don't match

    return text
