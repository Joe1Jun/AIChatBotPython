import ollama
import streamlit as st




MODEL_NAME = "llama3.2"


def main():
    #Title of the page
    st.title("Local AI Chatbot")
    user_input = st.text_input("Enter a question fot the chat bot")

    if user_input:
        with st.spinner("Generating response"):
          res = ollama.generate(model=MODEL_NAME , prompt=user_input)
          st.write(res["response"])

        
    else:
        st.error("No input") 


if __name__ == "__main__":
    main()
