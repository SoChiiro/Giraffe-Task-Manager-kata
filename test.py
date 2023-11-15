from main import Task
def test_description_AddTask():
    Task.addTask("Test for adding task")
    assert Task.allTask[-1].description == "Test for adding task"

def test_id_AddTask():
    Task.addTask("test 2")
    assert Task.allTask[-1].id == 2

