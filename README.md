# TODO List CLI

A simple command-line tool for managing your TODO list.

## Installation

Clone the repository

```bash
git clone https://github.com/elitegooddev/todo-cli.git
```

```bash
cd todo-cli
```

Install the package

```bash
pip install -e .
```

## Usage

### Add a task

```bash
todo add "Task title" -d "Task description"
```

### List all tasks

```bash
todo list
```

### Mark a task as completed

```bash
todo complete <task_id>
```

### Delete a task

```bash
todo delete <task_id>
```

## Technical Documentation

For more detailed information about the architecture and how to extend the application, please refer to the [Technical Documentation](docs/technical_documentation.md).
