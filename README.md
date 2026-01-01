# 🛡️ Omni-Insight: Multimodal PDF Intelligence

An AI-powered document analysis system that allows users to chat with PDFs—including complex charts, tables, and images—using the **Gemini 1.5 Flash** model.

## 🚀 Key Features
- **Multimodal Intelligence:** Leverages Gemini 1.5 Flash to "see" and interpret visual data within documents.
- **Persistent Memory:** Implemented `st.session_state` to maintain chat context across multiple user turns.
- **Professional Dashboard:** Built with Streamlit for a clean, user-friendly interface.

## 🛠️ Technical Challenges Overcome
- **Rate Limit Management:** Resolved `429 Resource Exhausted` errors by implementing smart model aliasing and dynamic cooling periods.
- **State Management:** Fixed `RuntimeError: Client Closed` by wrapping the GenAI client in a persistent session state to prevent connection drops during browser refreshes.

## 💻 Tech Stack
- **Language:** Python
- **AI Model:** Google Gemini 1.5 Flash (via `google-genai` SDK)
- **Frontend:** Streamlit
- **Environment:** Python Virtual Environment (venv)