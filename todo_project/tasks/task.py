
import datetime as dt
from typing import Protocol


class BaseTask(Protocol):
    title: str
    _is_complete: bool
    task_id: int

    def complete(self) -> None:
        ...


class Task:
    task_id: int
    type_of_task: str
    title: str
    deadline: dt.datetime
    priority: int
    _is_complete: bool

    def __init__(
        self, 
        title: str, 
        deadline: dt.datetime | None = None, 
        priority: int = 3) -> None:

        self.title = title
        self.priority = priority
        
        if deadline is None:
            self.deadline = dt.datetime.now().astimezone() + dt.timedelta(days=3)
        else:
            self.deadline = deadline

        self._is_complete = False
        self.task_id = 0
        self.type_of_task = "Task"
    
    def __str__(self):
        return f"{self.type_of_task}. Id = {self.task_id}, Title = {self.title}, Deadline = {self.deadline}, Priority = {self.priority}, Complete = {self._is_complete}"

    def complete(self) -> None:
        self._is_complete = True

class RepeatableTask:
    task_id: int
    type_of_task: str
    title: str
    deadline: dt.datetime
    priority: int
    _is_complete: bool
    repeat_period: int

    def __init__(
        self,
        title: str, 
        deadline: dt.datetime | None = None, 
        priority: int = 3, 
        repeat_period: int = 1) -> None:

        self.title = title
        self.priority = priority
        self.repeat_period = repeat_period
        
        if deadline is None:
            self.deadline = dt.datetime.now().astimezone() + dt.timedelta(days=3)
        else:
            self.deadline = deadline

        self._is_complete = False
        self.task_id = 0
        self.type_of_task = "RepeatableTask"

    def __str__(self):
        return f"{self.type_of_task}. Id = {self.task_id}, Title = {self.title}, Deadline = {self.deadline}, Priority = {self.priority}, Repeat period = {self.repeat_period}, Complete = {self._is_complete}"

    def complete(self) -> None:
        if self.repeat_period > 0:
            self.deadline = dt.datetime.now().astimezone() + dt.timedelta(days=self.repeat_period)
        else:
            self._is_complete = True

    def complete_without_repeat(self) -> None:
        self._is_complete = True
