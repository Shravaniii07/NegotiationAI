from rag.retriever import add_documents

def load_market_data():

    with open("../data/marketing_insights.txt", "r") as f:
        data = f.readlines()

    add_documents(data)