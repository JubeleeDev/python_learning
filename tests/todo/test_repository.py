
import pytest
from todo_project.tasks.repository import TaskRepository
from todo_project.tasks.task import RepeatableTask, Task


class TestRepository:

    def test_add_task_to_list(self, repo: TaskRepository):
        task = Task("test")
        repo.add_task(task)

        assert len(repo.list_of_tasks()) == 1
        
        first_element = repo.list_of_tasks()[0]
        assert first_element.task_id == 0

        repeatable_task = RepeatableTask("repeatable test")
        repo.add_task(repeatable_task)

        assert len(repo.list_of_tasks()) == 2

        second_element = repo.list_of_tasks()[1]
        assert second_element.task_id == 1

    def test_complete_base_task(self, repo: TaskRepository):
        task = Task("test")
        repo.add_task(task)

        repo.complete(0)

        first_element = repo.list_of_tasks()[0]
        assert first_element._is_complete

    def test_delete_task(self, repo: TaskRepository):
        with pytest.raises(ValueError):
            repo.delete_task(0)

        task = Task("test")
        repo.add_task(task)
        repo.delete_task(0)

        assert len(repo.list_of_tasks()) == 0
        

    def test_clear_tasks(self, repo: TaskRepository):
        task = Task("test")
        repo.add_task(task)

        assert len(repo.list_of_tasks()) != 0

        repo.clear_tasks()

        assert len(repo.list_of_tasks()) == 0
        assert repo._task_counter == 0

@pytest.fixture
def repo():
    return TaskRepository()