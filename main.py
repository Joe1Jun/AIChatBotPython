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


MODEL_NAME = OllamaLLM(model="llama3.2")
Prompt = ChatPromptTemplate.from_template(template)

chain = Prompt | MODEL_NAME


         


def main():
    # Title of the page
    st.title("Local AI Chatbot")

    # Initialize conversation history
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Create a container for displaying the conversation
    conversation_container = st.container()

    # Add a user input box at the bottom
    user_input = st.text_input("Enter your question:", label_visibility="hidden")

    if user_input:
        with st.spinner("Generating response..."):
            try:
                # Prepare context
                context = "\n".join(st.session_state.conversation_history)
                # Generate response
                res = chain.invoke({"context": context, "question": user_input})
                response = res["response"] if isinstance(res, dict) and "response" in res else str(res)
                
                # Update conversation history
                st.session_state.conversation_history.append(f"User: {user_input}")
                st.session_state.conversation_history.append(f"ChatBot: {response}")
                
                
                

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    # Display the full conversation
    with conversation_container:
        for message in st.session_state.conversation_history:
            st.write(message)

if __name__ == "__main__":
    main()