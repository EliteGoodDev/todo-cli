import json
import os
from typing import List, Optional

from todo_cli.models.task import Task
from todo_cli.storage.storage_interface import StorageInterface


class JsonStorage(StorageInterface):
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def _read_tasks(self) -> List[dict]:
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def _write_tasks(self, tasks: List[dict]):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=2)

    def save_task(self, task: Task) -> None:
        tasks = self._read_tasks()
        tasks.append(task.to_dict())
        self._write_tasks(tasks)

    def get_all_tasks(self) -> List[Task]:
        tasks_data = self._read_tasks()
        return [Task.from_dict(task_data) for task_data in tasks_data]

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        tasks_data = self._read_tasks()
        for task_data in tasks_data:
            if task_data["id"] == task_id:
                return Task.from_dict(task_data)
        return None

    def update_task(self, task: Task) -> None:
        tasks_data = self._read_tasks()
        for i, task_data in enumerate(tasks_data):
            if task_data["id"] == task.id:
                tasks_data[i] = task.to_dict()
                break
        self._write_tasks(tasks_data)

    def delete_task(self, task_id: str) -> None:
        tasks_data = self._read_tasks()
        tasks_data = [task for task in tasks_data if task["id"] != task_id]
        self._write_tasks(tasks_data)
