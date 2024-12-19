import sys
import os
import argparse
from http_method import perform_request
from auth import get_auth_headers

# Add the parent directory to sys.path for module lookup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rest_api_cli.config import load_config


def handle_cli_mode(args):
    """Handle the command-line interface (CLI) mode."""
    if args.use_config:
        config = load_config()  # Load settings from config file
        args.url = config.get('url', args.url)
        args.auth = config.get('auth', args.auth)
        args.method = config.get('method', args.method)
        args.data = config.get('data', args.data)
    
    if args.url and args.auth and args.method:
        headers = get_auth_headers(args.auth)
        response = perform_request(args.method, args.url, headers, args.data)
        print(response.text)
    else:
        print("Please provide all required arguments: url, auth, method.")

def interactive_mode():
    """Handle the interactive mode."""
    print("Interactive mode: Type 'exit' to quit.")
    
    while True:
        # Get user input
        url = input("Enter URL: ")
        if url.lower() == 'exit':
            break
        
        auth = input("Enter authentication (username:password or token): ")
        if auth.lower() == 'exit':
            break
        
        method = input("Enter HTTP method (GET, POST, PUT, DELETE, PATCH): ").upper()
        if method.lower() == 'exit':
            break
        
        data = input("Enter data (JSON format for POST/PUT/PATCH, or leave empty): ")
        if data.lower() == 'exit':
            break

        headers = get_auth_headers(auth)
        response = perform_request(method, url, headers, data)
        print(f"\nResponse Code: {response.status_code}")
        print(f"Response Body: {response.text}\n")

def main():
    """Main function to handle CLI or interactive mode."""
    parser = argparse.ArgumentParser(description="REST API CLI Tool")
    
    # Arguments for CLI mode
    parser.add_argument("--url", help="API URL")
    parser.add_argument("--auth", help="Authentication (username:password or token)")
    parser.add_argument("--method", help="HTTP method (GET, POST, PUT, DELETE, PATCH)")
    parser.add_argument("--data", help="Payload data (for POST, PUT, PATCH)")
    
    # Choose the mode: CLI or Interactive
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    
    # Use config from file
    parser.add_argument("--use-config", action="store_true", help="Load settings from config file")
    
    args = parser.parse_args()

    if args.interactive:
        # Run in interactive mode if the flag is set
        interactive_mode()
    else:
        # Otherwise, run in CLI mode
        handle_cli_mode(args)

if __name__ == "__main__":
    main()
