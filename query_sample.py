import ollama
from data_loading import collection

prompt = (
    "What are the differences in the business of Tesla and Uber give 3 points for each?"
)

response = ollama.embeddings(prompt=prompt, model="mxbai-embed-large")
results = collection.query(query_embeddings=[response["embedding"]], n_results=1)
data = results["documents"][0][0]


output = ollama.generate(
    model="llama2", prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
)

print(output["response"])
