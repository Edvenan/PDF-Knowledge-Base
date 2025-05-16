import gradio as gr
import numpy as np
import requests
from utils import parse_pdf, build_vector_index

texts, images = parse_pdf("data/example.pdf")
index, embedder, embeddings = build_vector_index(texts)

def query_system(q):
    q_embed = embedder.encode([q])
    D, I = index.search(np.array(q_embed), k=3)
    context = "\n".join([texts[i] for i in I[0]])
    response = requests.post(
        "http://deepseek:8000/v1/completions",
        headers={"Content-Type": "application/json"},
        json={
            "prompt": f"Based on the following context:\n{context}\n\nAnswer:\n",
            "max_tokens": 300,
            "temperature": 0.7
        }
    )
    answer = response.json()["choices"][0]["text"]
    return answer, [images[i] for i in I[0]]

iface = gr.Interface(
    fn=query_system,
    inputs="text",
    outputs=["text", gr.Gallery(label="PDF Snapshots").style(grid=3)]
)

iface.launch(server_name="0.0.0.0", server_port=7860)
