from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    return loader.load()

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return text_splitter.split_documents(documents)

def generate_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    return embeddings

def create_faiss_vector_store(texts, embeddings):
    return FAISS.from_documents(texts, embeddings)

def save_vector_store(db, path):
    db.save_local(path)

def create_vector_db():
    documents = load_documents()
    texts = split_text(documents)
    embeddings = generate_embeddings()
    db = create_faiss_vector_store(texts, embeddings)
    save_vector_store(db, DB_FAISS_PATH)

if __name__ == "__main__":
    create_vector_db()
