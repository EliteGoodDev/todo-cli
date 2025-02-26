from todo_cli.app import TodoApp
from todo_cli.cli import TodoCLI
from todo_cli.storage.json_storage import JsonStorage


def main():
    # Initialize storage
    storage = JsonStorage()
    
    # Initialize app with storage
    app = TodoApp(storage)
    
    # Initialize CLI with app
    cli = TodoCLI(app)
    
    # Run CLI
    cli.run()


if __name__ == "__main__":
    main()
