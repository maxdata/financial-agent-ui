import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes

from .chain import create_graph
from .chat_types import ChatInputType


def start():
    app = FastAPI(
        title="Gen UI Backend",
        version="1.0",
        description="A simple api server using Langchain's Runnable interfaces",
    )

    # Configure CORS
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    graph = create_graph()
    runnable = graph.with_types(input_type=ChatInputType, output_type=dict)
    
    add_routes(app, runnable, path="/chat", playground_type="default")
    return app  # Return the app instead of running it

# Add this line at the end of the file
app = start()
