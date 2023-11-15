from main import Task
def test_description_AddTask():
    Task.addTask("Test for adding task")
    assert Task.allTask[-1].description == "Test for adding task"

def test_id_AddTask():
    Task.addTask("test 2")
    assert Task.allTask[-1].id == 2

def test_removeTask():
    Task.removeTask(1)
    assert Task.allTask[0].description == "test 2"
    assert Task.allTask[0].id == 2
    
def test_setTaskToDone():
    Task.setTaskToDone(2)
    assert Task.allTask[0].status == "DONE"
    
def test_setTaskToDo():
    Task.setTaskToDo(2)
    assert Task.allTask[0].status == "TODO"  
    