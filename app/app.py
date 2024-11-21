import torch
import os
import argparse
import ollama
from rag import open_file, get_relevant_context, rewrite_query, ollama_chat, client

YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

if __name__ == "__main__":

    print(NEON_GREEN + "Parsing command-line arguments..." + RESET_COLOR)
    parser = argparse.ArgumentParser(description="Ollama Chat")
    parser.add_argument("--model", default="llama3", help="Ollama model to use (default: llama3)")
    args = parser.parse_args()

    print(NEON_GREEN + "Loading vault content..." + RESET_COLOR)
    vault_content = []
    if os.path.exists("vault.txt"):
        with open("vault.txt", "r", encoding='utf-8') as vault_file:
            vault_content = vault_file.readlines()

    print(NEON_GREEN + "Generating embeddings for the vault content..." + RESET_COLOR)
    vault_embeddings = []
    for content in vault_content:
        response = ollama.embeddings(model='mxbai-embed-large', prompt=content)
        vault_embeddings.append(response["embedding"])

    print(NEON_GREEN + "Converting embeddings to tensor..." + RESET_COLOR)
    vault_embeddings_tensor = torch.tensor(vault_embeddings) 

    print(NEON_GREEN + "Starting conversation loop..." + RESET_COLOR)
    conversation_history = []
    system_message = "You are a helpful assistant that is an expert at extracting the most useful information from a given text. Also bring in extra relevant infromation to the user query from outside the given context."

    while True:
        user_input = input(YELLOW + "Ask a query about your documents (or type 'quit' to exit): " + RESET_COLOR)
        if user_input.lower() == 'quit':
            break
        
        response = ollama_chat(user_input, system_message, vault_embeddings_tensor, vault_content, args.model, conversation_history)
        print(NEON_GREEN + "Response: \n\n" + response + RESET_COLOR)
