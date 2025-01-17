import ollama
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
   Answer the question below.

   Here is the conversation history: {context}

   Question: {question}

   Answer:
"""

MODEL_NAME = OllamaLLM(model="llam3.2")
Prompt = ChatPromptTemplate.from_template(template)

chain = Prompt | MODEL_NAME



def main():
    #Title of the page
    st.title("Local AI Chatbot")
    user_input = st.text_input("Enter a question fot the chat bot")

    if user_input:
        with st.spinner("Generating response"):
          res = chain.invoke({"context":" " , "question":user_input })
          st.write(res["response"])

        
    else:
        st.error("No input") 


if __name__ == "__main__":
    main()
