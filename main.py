idGlobal = 0
class Task:
    allTask = []
    def __init__(self, description,idGlobal=idGlobal):
        self.description = description
        idGlobal = idGlobal + 1
        self.id = idGlobal
        self.status = "TODO"
    
    def addTask(description):
        Task.allTask.append(Task(description))

