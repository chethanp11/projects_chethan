import streamlit as st
from main_promptgen import generate_optimal_prompt

def main():
    st.set_page_config(
        page_title="🧠 AI Prompt Optimizer",
        page_icon="🛠️",
        layout="centered"
    )

    # Custom styling
    st.markdown("""
        <style>
        .stTextArea textarea {
            font-size: 1.1rem !important;
        }
        .prompt-box {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 1rem;
            font-size: 1.05rem;
            white-space: pre-wrap;
            word-break: break-word;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛠️ Prompt Optimizer for AI Tool Builders")
    st.caption("Generate powerful, development-ready prompts from simple ideas.")

    st.markdown("#### 📝 Enter your instruction or error message")
    user_input = st.text_area(
        label="",
        placeholder="e.g., Build a Streamlit app that generates QR codes...",
        height=180
    )

    if st.button("🚀 Generate Optimized Prompt", use_container_width=True):
        if user_input.strip():
            with st.spinner("Optimizing your prompt..."):
                try:
                    optimized = generate_optimal_prompt(user_input)
                    st.success("✅ Prompt generated successfully!")

                    st.markdown("#### 🎯 Optimized Prompt")
                    with st.expander("Click to view optimized prompt", expanded=True):
                        st.markdown(f"<div class='prompt-box'>{optimized}</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"❌ An error occurred while generating the prompt:\n\n{e}")
        else:
            st.warning("⚠️ Please enter a valid instruction before submitting.")

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center;'>Built with ❤️ using OpenAI and Streamlit</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()