from typing import List, Optional

from todo_cli.models.task import Task
from todo_cli.storage.storage_interface import StorageInterface


class TodoApp:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task to the list"""
        task = Task(title=title, description=description)
        self.storage.save_task(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.storage.get_all_tasks()

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by ID"""
        return self.storage.get_task_by_id(task_id)

    def mark_task_completed(self, task_id: str) -> Optional[Task]:
        """Mark a task as completed"""
        task = self.storage.get_task_by_id(task_id)
        if task:
            task.mark_completed()
            self.storage.update_task(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        """Delete a task"""
        task = self.storage.get_task_by_id(task_id)
        if task:
            self.storage.delete_task(task_id)
            return True
        return False
