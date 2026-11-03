import json
import logging

from todo_project.tasks.repository import TaskRepository
from todo_project.tasks.storage import StorageRepository
from todo_project.tasks.task import RepeatableTask, Task
from todo_project.tasks.utils import convert_to_number

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p', 
        level="DEBUG")

    repo    = TaskRepository()
    storage = StorageRepository()

    print("""Welcome to CLI ToDO! Valid input:
        1 - create task, 
        2 - list of tasks, 
        3 - save to file, 
        4 - load from file, 
        5 - complete task, 
        6 - delete task, 
        7 - complete all tasks, 
        0 - exit.""")

    while True:
        print("Please, insert your command:")
        user_input = input()

        match user_input:
            case "0":
                print("Bye!")
                break
            case "1":
                title = input("Task title: ")

                if title == "":
                    print("title cannot be empty")
                    continue

                task_type = input("Task type (1 - basic, 2 - repeatable): ")
                priority = convert_to_number(value=input("Priority (0-3): "), name="priority", show_error=False)

                if priority is None:
                    print("cannot convert given priority number. priority set to default = 3")
                    priority = 3

                if task_type == "1" or task_type == "2":
                    if task_type == "1":
                        task = Task(title=title, priority=priority)
                    else:
                        repeat_period = convert_to_number(input("Repeat period: "), name="repeat_period", show_error=False)

                        if repeat_period is None:
                            print("cannot convert given repeat period number. repeat period set to default = 1")
                            repeat_period = 1

                        task = RepeatableTask(title=title,priority=priority,repeat_period=repeat_period)
                    try:
                        repo.add_task(task)
                        print("task was successfully added")
                    except ValueError as e:
                        logger.warning("error while adding task to list: %s", e)
                else:
                    print("Wrong task type")
            case "2":
                print(f"{"-" * 20}List of tasks{"-" * 20}")
                for task in repo.list_of_tasks():
                    print(task)
                    print("-" * 40)
            case "3":
                storage.save_to_file(repo.list_of_tasks())
                print("data is successfully saved")
            case "4":
                try:
                    storage.load_from_file(repo)
                    print("data is successfully loaded")
                except FileNotFoundError:
                    print("file for load data is not exists")
                except json.JSONDecodeError:
                    print("fail to decode file while loading")
            case "5":
                task_id = convert_to_number(value=input("Please, input an id of task: "), name="task_id")

                if task_id is None:
                    continue

                try:
                    repo.complete(task_id)
                    print("complete property was successfully set")
                except ValueError:
                    print("task with given id is not found")
            case "6":
                task_id = convert_to_number(value=input("Please, input an id of task: "), name="task_id")

                if task_id is None:
                    continue

                try:
                    repo.delete_task(task_id)
                    print("task was deleted successfully")
                except ValueError:
                    print("task with given id is not found")
            case "7":
                repo.complete_all_tasks()
                print("all tasks were successfully completed")
            case _:
                print("invalid operation")

