import torch
import os
import argparse
import ollama
from rag import open_file, get_relevant_context, rewrite_query, ollama_chat, client
from upload import upload

YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

if __name__ == "__main__":

    print(NEON_GREEN + "Parsing command-line arguments..." + RESET_COLOR)
    parser = argparse.ArgumentParser(description="Ollama Chat")
    parser.add_argument("--model", default="llama3", help="Ollama model to use (default: llama3)")
    parser.add_argument("--rag", action="store_true", default=True, help="Start script with rag (enabled by default)")
    parser.add_argument("--no-rag", action="store_false", dest="rag", help="Start script with no rag")
    parser.add_argument("--temperature", type=float, default=0.1, help="Temperature used by Ollama (0-1, default: 0.1)")
    parser.add_argument("--drivefile", type=str, default="https://drive.google.com/file/d/1YWxsSgA0X0M1bI0W4-8VXIUoP10S57I8/view?usp=drive_link", help="Google Drive public file link (default : https://drive.google.com/file/d/1YWxsSgA0X0M1bI0W4-8VXIUoP10S57I8/view?usp=drive_link)")
    args = parser.parse_args()

    vault_content = []
    vault_embeddings = []

    if args.rag :
        upload(args.drivefile)
        if os.path.exists("vault.txt"):
            print(NEON_GREEN + "Loading vault content..." + RESET_COLOR)
            with open("vault.txt", "r", encoding='utf-8') as vault_file:
                vault_content = vault_file.readlines()
            print(NEON_GREEN + "Generating embeddings for the vault content..." + RESET_COLOR)
            for content in vault_content:
                response = ollama.embeddings(model='mxbai-embed-large', prompt=content)
                vault_embeddings.append(response["embedding"])
            print(NEON_GREEN + "Converting embeddings to tensor..." + RESET_COLOR)
        else:
            print(NEON_GREEN + "/!\\ No vault to embed" + RESET_COLOR)
    else :
        print(NEON_GREEN + "No rag" + RESET_COLOR)


    vault_embeddings_tensor = torch.tensor(vault_embeddings) 

    print(NEON_GREEN + "Starting conversation loop..." + RESET_COLOR)
    conversation_history = []
    system_message = "You are a helpful assistant that is an expert at extracting the most useful information from a given text. Also bring in extra relevant infromation to the user query from outside the given context."

    while True:
        user_input = input(YELLOW + "Ask a query about your documents (or type 'quit' to exit): " + RESET_COLOR)
        if user_input.lower() == 'quit':
            break
        
        response = ollama_chat(user_input, system_message, vault_embeddings_tensor, vault_content, args.model, conversation_history, args.temperature)
        print(NEON_GREEN + "Response: \n\n" + response + RESET_COLOR)
