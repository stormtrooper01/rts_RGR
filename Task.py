class Task:

    deadline = 0
    creationTime = 0
    executionTime = 0
    deadlineMultiplier = 0
    waitTime = 0

    def __init__(self, creationTime, executionTime):
        self.executionTime = int(executionTime)
        self.creationTime = int(creationTime)
        self.deadline = int(creationTime + executionTime * self.deadlineMultiplier)

    def GetTimeLimit(self):
        return (self.deadline + self.creationTime)

    def GetDeadline(self):
        return self.deadline

    def WorkedOn(self):
        self.executionTime = self.executionTime - 1

    def Wait(self):
        self.waitTime = self.waitTime + 1

    def GetExecutionTime(self):
        return self.executionTime

    def GetCreationTime(self):
        return self.creationTime
