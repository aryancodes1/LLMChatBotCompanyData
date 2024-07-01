from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import ollama
from langchain_community.document_loaders import PyMuPDFLoader

client = chromadb.Client()
collection = client.create_collection(name="docs")


def load_data(path, n):
    loader = PyMuPDFLoader(path)

    data = loader.load()

    list1 = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    text_splitter.split_documents(data)

    for i in range(len(data)):
        data_text = data[i].page_content
        data_text = data_text.replace("\n", "")
        list1.append(data_text)

    ##Storing Embedded Data

    for i, data in enumerate(list1):
        response = ollama.embeddings(model="mxbai-embed-large", prompt=data)
        embedding = response["embedding"]
        collection.add(ids=[str(i) + str(n)], embeddings=[embedding], documents=[data])
    print("Done")


load_data("Uber.pdf", "a")
load_data("Google.pdf", "b")
load_data("Tesla.pdf", "c")
