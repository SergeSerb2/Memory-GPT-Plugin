import json

import quart
import quart_cors
from quart import request

import os
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import numpy as np
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
import os
from PyPDF2 import PdfReader
import pinecone as pc
import numpy as np

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/remember")
async def remember():
    request = await quart.request.get_json(force=True)
    raw_text = request["text"]

    text_splitter = CharacterTextSplitter(
        separator = '\n',
        chunk_size = 2500,
        chunk_overlap = 200,
        length_function = len,
    )

    texts = text_splitter.split_text(raw_text)

    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)  

    pineconeAPIKey = os.environ["PINECONE_API_KEY"]

    # Get the Pinecone Environment from the environment
    pineconeEnvironment = os.environ["PINECONE_ENVIRONMENT"]

    # Get the Pinecone Index from the environment
    pineconeIndex = os.environ["PINECONE_INDEX"]

    pc.init(api_key=pineconeAPIKey, environment=pineconeEnvironment)
    index = pc.Index(pineconeIndex)

    pinecone = Pinecone(index, embeddings.embed_query, "text")

    pinecone.add_texts(texts)

    return quart.Response(response='Added new information to the knowledge base', status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()