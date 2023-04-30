# Memory-GPT Plugin

The Memory-GPT Plugin is a ChatGPT extension that allows ChatGPT to store new information on its own. This plugin currently only works with the Pinecone datastore.

## Demo

[Link Text](https://twitter.com/SerbinenkoSerge/status/1652791807481372672)

## Getting Started

1. Set the required environment variables:

```
export DATASTORE=pinecone
export BEARER_TOKEN=<your_bearer_token>
export OPENAI_API_KEY=<your_openai_api_key>
export PINECONE_API_KEY=<your_pinecone_api_key>
export PINECONE_ENVIRONMENT=<your_pinecone_environment>
export PINECONE_INDEX=<your_pinecone_index>
```


2. Install the required packages using the `requirements.txt` file.

3. Start the `main.py` file to run the Memory-GPT Plugin. You can find it at `localhost:5003`.

**Note**: This plugin is designed to be used in combination with the `chatgpt-retrieval-plugin` and, ideally, the `google-search-plugin` to enable ChatGPT to find new information and save it.

## Dependencies

- Pinecone datastore
- chatgpt-retrieval-plugin
- (Optional) google-search-plugin
