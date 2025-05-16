import fitz
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import os

def parse_pdf(path, img_dir="images"):
    os.makedirs(img_dir, exist_ok=True)
    doc = fitz.open(path)
    text_chunks, snapshots = [], []
    for page in doc:
        text = page.get_text()
        img_path = os.path.join(img_dir, f"page_{page.number}.png")
        page.get_pixmap().save(img_path)
        text_chunks.append(text)
        snapshots.append(img_path)
    return text_chunks, snapshots

def build_vector_index(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, model, embeddings
