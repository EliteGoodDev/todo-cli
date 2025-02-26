# TODO List CLI - Technical Documentation

## Overview

The TODO List CLI is a command-line tool that allows users to manage their tasks. It provides basic functionality for adding, viewing, completing, and deleting tasks. The application is designed with a modular architecture to allow for future extensions and different storage implementations.

## Architecture

The application follows a modular design with the following components:

### Models

Defines the data structures used in the application.

- `Task`: Represents a task with title, description, status, etc.

### Storage

Handles persistence of tasks.

- `StorageInterface`: Abstract interface for storage implementations.
- `JsonStorage`: Implementation that stores tasks in a JSON file.

### Application Logic

Contains the core business logic.

- `TodoApp`: Manages tasks and interacts with storage.

### CLI

Handles command-line interaction.

- `TodoCLI`: Parses commands and displays results.

## Extending the Application

### Adding a New Storage Implementation

To add a new storage implementation:

1. Create a new class that implements the `StorageInterface`.
2. Implement all required methods.
3. Update the `main.py` file to use your new storage implementation.

Example:

```python
from todo_cli.storage.storage_interface import StorageInterface

class MySQLStorage(StorageInterface):
    # Implement all required methods
    ...

# In main.py
storage = MySQLStorage()
```

### Adding New Features

To add new features:

1. Update the `TodoApp` class with new methods.
2. Add new commands to the `TodoCLI` class.
3. Update the documentation.

## Potential Future Enhancements

- Task priorities
- Due dates
- Categories/tags
- Search functionality
- Task filtering
- Interactive mode
