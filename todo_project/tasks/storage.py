
import datetime as dt
import json
import pathlib

from todo_project.tasks.repository import TaskRepository
from todo_project.tasks.task import BaseTask, RepeatableTask, Task


class StorageRepository:
    path: str

    def __init__(self, path: str | None = None) -> None:
        if path is None:
            catalog = pathlib.Path(__file__)
            root_dir = catalog.parent.parent
            self.path = root_dir.joinpath("data/tasks.json")
        else:
            self.path = path

    def save_to_file(self, tasks: list[BaseTask]) -> None:

        result: list[dict] = []

        for task in tasks:
            dict_task = {
                "task_id": task.task_id,
                "type_of_task": task.type_of_task,
                "title": task.title,
                "deadline": task.deadline.isoformat(),
                "priority": task.priority,
                "_is_complete": task._is_complete
            }
            if task.type_of_task == "RepeatableTask":
                dict_task["repeat_period"] = task.repeat_period

            result.append(dict_task)


        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)

    def load_from_file(self, task_repo: TaskRepository) -> None:
        with open(self.path, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)
            
            task_repo.clear_tasks()

            for task in tasks_data:
                if task["type_of_task"] == "RepeatableTask":
                    load_task = RepeatableTask(
                        title=task["title"],
                        deadline=dt.datetime.fromisoformat(task["deadline"]),
                        priority=task["priority"],
                        repeat_period=task["repeat_period"]
                    )
                else:
                    load_task = Task(
                        title=task["title"],
                        deadline=dt.datetime.fromisoformat(task["deadline"]),
                        priority=task["priority"]
                    )
                if task["_is_complete"]:
                    load_task._is_complete = True

                task_repo.add_task(load_task)
        
            
        
