# LLM ChatBot CompanyData


# Content Engine
Welcome to the Content Engine project! This system is designed to analyze and compare multiple PDF documents, specifically focusing on Form 10-K filings of multinational companies. It leverages Retrieval Augmented Generation (RAG) techniques to retrieve, assess, and generate insights from these documents.

## Overview
The Content Engine is built to handle complex document comparisons and provide interactive insights through a chatbot interface. It utilizes advanced frameworks and technologies to ensure efficient document parsing, embedding generation, and contextual analysis.

## Setup
### Backend Framework
For the backend, I chose LangChain due to its flexibility in creating custom retrieval systems, which suited the project's needs well.

### Frontend Framework
The user interface is developed using Streamlit, enabling intuitive interaction and display of comparative insights.

### Vector Store
I opted to use Chromadb as the vector store for managing and querying document embeddings locally, ensuring fast and efficient retrieval operations.

### Embedding Model
To generate document embeddings from PDF content, I implemented a locally running embedding model. This approach maintains data privacy and eliminates dependency on external APIs.

### Local Language Model (LLM)
Integration of a local instance of a Large Language Model enhances the system's ability to provide contextual insights directly from the document content.

### Initialization
Provided Documents
The system is initialized with Form 10-K filings from three major companies:

Alphabet Inc.
Tesla, Inc.
Uber Technologies, Inc.
Development Details
Document Parsing
I developed a robust document parsing module to extract text and structure from PDF files accurately.

### Vector Generation
The embedding model generates embeddings for each document, representing their content in a vector space.

### Vector Store Integration
ChromaDb was configured to store and manage these document embeddings, facilitating efficient querying and comparison tasks.

### Query Engine Configuration
I set up a query engine to retrieve and compare documents based on their embeddings, enabling detailed analysis and highlighting differences.

### LLM Integration
The local Language Model is seamlessly integrated to provide contextual insights and answer complex queries about the documents.

### Chatbot Interface
I designed and implemented a user-friendly chatbot interface using Streamlit, allowing users to interact with the system, query information, and compare data across the documents.


## Outcome and Guidelines

The Content Engine architecture is designed to be scalable and modular, capable of handling additional documents and functionalities.
Using a locally running LLM (Ollama )and Chromadb for vector storage ensures data privacy and reduces reliance on external APIs.

## Interface LLM Results

![
](Result1.png)
![
](Result2.png)
![alt text](Result3.png)

