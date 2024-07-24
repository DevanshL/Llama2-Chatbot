import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from langchain_community.llms import LlamaCpp
from llama_index.llms.llama_cpp.llama_utils import messages_to_prompt, completion_to_prompt
from langchain.schema import SystemMessage, HumanMessage, AIMessage

class CustomMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content

def init_page() -> None:
    st.set_page_config(page_title="Llama2 Chatbot")
    st.header("Llama2 Chatbot")
    st.sidebar.title("Options")

def select_llm() -> LlamaCpp:
    return LlamaCpp(
        model_path="llama-2-7b-chat.Q8_0.gguf",
        temperature=0.7,
        max_new_tokens=4000,
        context_window=4096,
        generate_kwargs={},
        model_kwargs={},
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )

def init_messages() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant. Reply your answer in markdown format.")
        ]

def convert_messages(messages):
    converted = []
    for message in messages:
        if isinstance(message, SystemMessage):
            converted.append(CustomMessage(role="system", content=message.content))
        elif isinstance(message, HumanMessage):
            converted.append(CustomMessage(role="user", content=message.content))
        elif isinstance(message, AIMessage):
            converted.append(CustomMessage(role="assistant", content=message.content))
    return converted

def get_answer(llm, messages) -> str:
    prompt_list = messages_to_prompt(convert_messages(messages))
    prompt_length = sum(len(token) for token in prompt_list)

    if prompt_length > llm.model_kwargs.get("context_window", 4096):
        raise ValueError(f"Requested tokens ({prompt_length}) exceed context window of {llm.model_kwargs.get('context_window', 4096)}")

    response = llm.generate([prompt_list])
    return response.generations[0][0].text

def main() -> None:
    init_page()
    llm = select_llm()
    init_messages()

    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant. Reply your answer in markdown format.")
        ]

    if user_input := st.chat_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        try:
            with st.spinner("Bot is typing ..."):
                answer = get_answer(llm, st.session_state.messages)
                print(answer)
            st.session_state.messages.append(AIMessage(content=answer))
        except ValueError as e:
            st.toast("Message limit reached. Please clear the conversation to continue.")
        except AssertionError as e:
            st.toast("Message limit reached. Please clear the conversation to continue.")

    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("user", avatar="👩‍🎨"):
                st.markdown(message.content)

if __name__ == "__main__":
    main()
