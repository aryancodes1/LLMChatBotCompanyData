import streamlit as st
import ollama
from data_loading import collection,load_data
import os
import tempfile


def get_bot_response(user_input):

    prompt = user_input
    response = ollama.embeddings(prompt=prompt, model="mxbai-embed-large")
    results = collection.query(query_embeddings=[response["embedding"]], n_results=1)
    data = results["documents"][0][0]

    output = ollama.generate(
        model="llama3",
        prompt=f"Using this data: {data}. Respond to this prompt: {prompt}",

    )

    return output["response"]


def main():
    st.title("Chat Bot API")
    history = []
    # Input text box for user input
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

    if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)
        with open(path, "wb") as f:
                f.write(uploaded_file.getvalue())

    load_data(path,'a')

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

main()