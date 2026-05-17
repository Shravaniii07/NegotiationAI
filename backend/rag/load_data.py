from rag.retriever import add_documents

def load_market_data():

    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, "data", "marketing_insights.txt")
    with open(file_path, "r") as f:
        data = f.readlines()

    add_documents(data)