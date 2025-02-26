from abc import ABC, abstractmethod
from typing import List, Optional

from todo_cli.models.task import Task


class StorageInterface(ABC):
    @abstractmethod
    def save_task(self, task: Task) -> None:
        """Save a task to storage"""
        pass

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks from storage"""
        pass

    @abstractmethod
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """Get a task by its ID"""
        pass

    @abstractmethod
    def update_task(self, task: Task) -> None:
        """Update an existing task"""
        pass

    @abstractmethod
    def delete_task(self, task_id: str) -> None:
        """Delete a task by its ID"""
        pass
