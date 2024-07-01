import streamlit as st
import ollama
from data_loading import collection

def get_bot_response(user_input):

    prompt = user_input
    response = ollama.embeddings(prompt=prompt, model="mxbai-embed-large")
    results = collection.query(query_embeddings=[response["embedding"]], n_results=1)
    data = results["documents"][0][0]

    output = ollama.generate(
        model="llama2",
        prompt=f"Using this data: {data}. Respond to this prompt: {prompt}",
    )

    return output["response"]


def main():
    st.title("Chat Bot API")
    history = []
    # Input text box for user input
    user_input = st.text_input("Enter your message:")

    if st.button("Send"):
        if user_input:
            # Get chatbot response
            bot_response = get_bot_response(user_input)
            
            # Append input and output to history
            history.append({"input": user_input, "output": bot_response})

            # Display bot response
            st.text_area("Bot's Response:", value=bot_response, height=100)

    # Display history
    st.header("Chat History")
    for idx, entry in enumerate(history[::-1]):  # Show most recent at the top
        st.text(f"Input {idx + 1}: {entry['input']}")
        st.text(f"Output {idx + 1}: {entry['output']}")
        st.markdown("---")

if __name__ == "__main__":
    main()