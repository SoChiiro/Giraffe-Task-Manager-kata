class Task:
    # Variables
    allTask = []
    idGlobal = 0
    
    # Constructor
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

    #Setting a task to 'done'
    def setTaskToDone(id):
        for task in Task.allTask:
            if task.id == id and task.status == "TODO":
                task.status = "DONE"
    
    #Setting a task to 'to do'
    def setTaskToDo(id):
        for task in Task.allTask:
            if task.id == id and task.status == "DONE":
                task.status = "TODO"
                
    #Print all tasks
    def printAllTasks():
        stringBuilder = ""
        for task in Task.allTask:
            statusString = ""
            if task.status == "TODO":
                statusString = "[ ]"
            else:
                statusString = "[x]"
            stringBuilder = stringBuilder + str(task.id) + " " + statusString + " " + task.description + "\n"
        print(stringBuilder)
        return stringBuilder

class InteractionLoop:

    # Parse user input
    def parse(userInput):
        operator = userInput.split(" ")[0]
        if operator == "+":
            Task.addTask(userInput.split(" ", 1)[1])
        elif operator == "-":
            Task.removeTask(int(userInput.split(" ")[1]))
        elif operator == "x":
            Task.setTaskToDone(int(userInput.split(" ")[1]))
        elif operator == "o":
            Task.setTaskToDo(int(userInput.split(" ")[1]))
        elif operator == "q":
            print("Bye!")
            exit()
        else:
            print("Invalid command")

    # Loop for user input
    def loop():
        userInput = input("Enter command: \n\t + <description> \n\t - <id> \n\t x <id> \n\t o <id> \n\t q \n")