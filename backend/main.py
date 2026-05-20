from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import negotiation
from rag.load_data import load_market_data

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    load_market_data()

app.include_router(negotiation.router)

@app.get("/")
def home():
    return {"message": "DealCraft AI & Procurement Server Running"}