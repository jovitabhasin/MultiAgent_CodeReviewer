import streamlit as st

from graph import graph

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Multi-Agent AI Code Reviewer")
st.markdown(
    """
Review your source code using multiple AI agents.

Agents Used:
- 🐞 Bug Detector
- ⚡ Complexity Analyzer
- 🎨 Style Reviewer
- 🔒 Security Analyzer
- 📋 Aggregator
"""
)

# -------------------------
# Input
# -------------------------

uploaded_file = st.file_uploader(
    "Upload a source code file",
    type=["py", "cpp", "c", "java", "js", "ts"]
)

code = ""

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
else:
    code = st.text_area(
        "Or paste your code here",
        height=350,
        placeholder="Paste your code..."
    )

# -------------------------
# Review Button
# -------------------------

if st.button("🚀 Review Code", use_container_width=True):

    if not code.strip():
        st.error("Please upload or paste some code.")
        st.stop()

    with st.spinner("Running AI agents..."):

        initial_state = {
            "code": code,
            "language": "",
            "bug_report": "",
            "complexity_report": "",
            "style_report": "",
            "security_report": "",
            "final_report": "",
        }

        result = graph.invoke(initial_state)

    st.success("Review Complete!")

    st.markdown("---")

    st.markdown(result["final_report"])

    st.download_button(
        label="📥 Download Report",
        data=result["final_report"],
        file_name="code_review.md",
        mime="text/markdown",
    )