from main import Task
def test_AddTask():
    Task.addTask("Test for adding task")
    assert Task.allTask[-1].description == "Test for adding task"
    print("Task after:",Task.allTask[-1].description)

