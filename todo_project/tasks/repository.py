from todo_project.tasks.task import BaseTask


class TaskRepository:
    _tasks_storage: list[BaseTask]
    _task_counter: int

    def __init__(self):
        self._tasks_storage = []
        self._task_counter = 0

    def add_task(self, task: BaseTask) -> None:
        if task not in self._tasks_storage:
            self._tasks_storage.append(task)
            task.task_id = self._task_counter
            self._task_counter += 1
        else:
            raise ValueError("chosen task already in storage")

    def delete_task(self, task_id: int) -> None:
        found_task = self.found_task_by_id(task_id)
        if found_task is not None:
            self._tasks_storage.remove(found_task)
        else:
            raise ValueError("chosen task in storage is not found")

    def complete(self, task_id: int) -> None:
        found_task = self.found_task_by_id(task_id)
        if found_task is not None:
            found_task.complete()
        else:
            raise ValueError("chosen task in storage is not found")

    def list_of_tasks(self) -> list[BaseTask]:
        return self._tasks_storage.copy()

    def complete_all_tasks(self) -> None:
        for task in self._tasks_storage:
            task.complete()

    def found_task_by_id(self, task_id: int) -> BaseTask | None:
        for task in self._tasks_storage:
            if task.task_id == task_id:
                return task
        return None

    def clear_tasks(self) -> None:
        self._task_counter = 0
        self._tasks_storage.clear()