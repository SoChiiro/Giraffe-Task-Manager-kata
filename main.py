class Task:
    allTask = []
    idGlobal = 0
    def __init__(self, description):
        self.description = description
        Task.idGlobal = Task.idGlobal + 1
        self.id = Task.idGlobal
        self.status = "TODO"
    
    # Adding a task to the list of tasks
    def addTask(description):
        Task.allTask.append(Task(description))

    # Removing a task from the list of tasks
    def removeTask(id):
        for task in Task.allTask:
            if task.id == id:
                Task.allTask.remove(task)

    #Setting a task to done
    def setTaskToDone(id):
        for task in Task.allTask:
            if task.id == id and task.status == "TODO":
                task.status = "DONE"
