import streamlit as st

def main():
    st.set_page_config(
        page_title="Qanda app",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title('Ask an interesting question')

    question = st.text_input('Enter a question')

    voice = st.checkbox('Enable voice')

    confirm_button = st.button('Get an answer')

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )

    if confirm_button:
        with st.spinner("Generating recipe..."):
            if question:
                generated_answer = 'This is the answer'

                st.markdown(
                    " ".join([
                        "<div>",
                        "<h2 class='font-title text-bold'>The answer:</h2>",
                        '<div style="padding: 30px;background-color: #B6C9B1; border-radius: 10px;">',
                        f'<p>{generated_answer}</p>',
                        "</div>",
                        "</div>"
                    ]),
                    unsafe_allow_html=True
                )

                if voice:
                    st.markdown(
                        " ".join([
                            "<div style='padding: 20px;background-color: #A7BFC7; border-radius: 10px;margin-top: 30px;'>",
                            '<p>Audio Coming soon...</p>',
                            "</div>"
                        ]),
                        unsafe_allow_html=True
                    )

main()