import argparse
import sys
from typing import List, Optional

from todo_cli.app import TodoApp
from todo_cli.models.task import Task


class TodoCLI:
    def __init__(self, app: TodoApp):
        self.app = app

    def run(self):
        parser = argparse.ArgumentParser(description="TODO List Command Line Tool")
        subparsers = parser.add_subparsers(dest="command", help="Command to execute")

        # Add task command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("title", help="Task title")
        add_parser.add_argument("-d", "--description", help="Task description")

        # List tasks command
        subparsers.add_parser("list", help="List all tasks")

        # Complete task command
        complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
        complete_parser.add_argument("task_id", help="ID of the task to mark as completed")

        # Delete task command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("task_id", help="ID of the task to delete")

        args = parser.parse_args()

        if args.command == "add":
            self._add_task(args.title, args.description)
        elif args.command == "list":
            self._list_tasks()
        elif args.command == "complete":
            self._complete_task(args.task_id)
        elif args.command == "delete":
            self._delete_task(args.task_id)
        else:
            parser.print_help()

    def _add_task(self, title: str, description: Optional[str] = None):
        task = self.app.add_task(title, description)
        print(f"Task added with ID: {task.id}")

    def _list_tasks(self):
        tasks = self.app.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return

        self._print_tasks(tasks)

    def _complete_task(self, task_id: str):
        task = self.app.mark_task_completed(task_id)
        if task:
            print(f"Task '{task.title}' marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def _delete_task(self, task_id: str):
        success = self.app.delete_task(task_id)
        if success:
            print(f"Task with ID {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def _print_tasks(self, tasks: List[Task]):
        print("\nTODO List:")
        print("-" * 50)
        for task in tasks:
            status = "✓" if task.completed else "☐"
            print(f"{status} [{task.id[:8]}] {task.title}")
            if task.description:
                print(f"  {task.description}")
            print("-" * 50)
