
import streamlit as st
from handlers.python_handler import run_python_code
from handlers.java_handler import run_java_code
from handlers.cpp_handler import run_cpp_code
from handlers.js_handler import run_javascript_code
from utils.suggest import suggest_fix
from utils.feedback import save_feedback


st.title("🤖 AI CODE DEBUGGING CHATBOT")

language = st.selectbox("Choose a language", ["Python", "Java", "C++", "JavaScript"])
user_code = st.text_area("📝 Enter your code here:", height=300)

user_inputs = ""
if language == "Python":
    st.markdown("### ⌨ Provide external input (one per line)")
    user_inputs = st.text_area("Input for your code:", height=100)

if st.button("▶ Run Code"):
    if not user_code.strip():
        st.warning("Please enter some code.")
    else:
        if language == "Python":
            result = run_python_code(user_code, user_inputs)
        elif language == "Java":
            result = run_java_code(user_code)
        elif language == "C++":
            result = run_cpp_code(user_code)
        elif language == "JavaScript":
            result = run_javascript_code(user_code)
        else:
            result = "❌ Language not supported."

        st.markdown("### 🖨 Output")
        st.code(result, language="text")

        st.markdown("### 💡 Suggestions")
        for tip in suggest_fix(result, language, user_code):
            st.write(f"- {tip}")

        st.markdown("### 🙋 Feedback")
        feedback = st.text_area("Let us know your thoughts:")
        if st.button("Submit Feedback"):
            if feedback.strip():
                save_feedback(f"{language}: {feedback}")
                st.success("✅ Thanks for your feedback!")
            else:
                st.warning("⚠ Please enter feedback before submitting.")
