import math
import Task

class EDF:

    currentTime = 0
    Q = []
    Qready = []
    Tw = [0 for x in range(10000)]
    Tn = [0 for x in range(10000)]
    faults = [0 for x in range(10000)]
    currentTask = None

    def __init__(self, Q):
        self.Q = Q

    def GetEDTask(self, removeFromQ):
        timeBuf = 9999999
        newTime = 0
        taskwED = None
        for i in range(len(self.Qready)):
            newTime = self.Qready[i].GetDeadline()
            if(timeBuf > newTime):
                timeBuf = newTime
                taskwED = self.Qready[i]
        if(removeFromQ):
            self.Qready.remove(taskwED)
        return taskwED

    def ToReadyQueue(self):
        for i in range(len(self.Q)):
            if self.Q[i].GetCreationTime() == self.currentTime:
                self.Qready.append(self.Q[i])

    def CheckForDeadlines(self):
        flt = 0
        flti = []
        for i in range(len(self.Qready)):
            if self.Qready[i].GetDeadline() < self.currentTime :
                flt += 1
                flti.append(i)
        if (self.currentTime == 0):
            self.faults[self.currentTime] = flt
        else:
            self.faults[self.currentTime] = self.faults[self.currentTime - 1] + flt
        for i in range(len(flti)):
            del self.Qready[flti[i]]
            for j in range(i, len(flti)):
                flti[j] -= 1


    def Work(self):
        self.currentTime = 0
        timewait = 0
        for self.currentTime in range(10000):
            if self.currentTime != 0 :
                self.Tn[self.currentTime] = self.Tn[self.currentTime - 1]
            timewait = 0
            self.CheckForDeadlines()
            self.ToReadyQueue()
            if(self.currentTask != None and self.currentTask.GetExecutionTime() == 0):
                self.currentTask = None
            elif(self.currentTask != None and self.GetEDTask(False) != None):
                if(self.GetEDTask(False).GetExecutionTime() < self.currentTask.GetExecutionTime()):
                    self.Qready.append(self.currentTask)
                    self.currentTask = self.GetEDTask(True)
            elif(self.currentTask != None):
                self.currentTask.WorkedOn()
            if(self.GetEDTask(False) == None and self.currentTask == None):
                self.Tn[self.currentTime] += 1
                continue
            elif(self.currentTask == None):
                self.currentTask = self.GetEDTask(True)
            for task in self.Qready:
                task.Wait()
                timewait += 1
            self.Tw[self.currentTime] = timewait

    def GetWaitTimes(self):
        return self.Tw

    def GetFaults(self):
        return self.faults

    def GetProcessorFreeTime(self):
        return self.Tn



class RM:
    currentTime = 0
    Q = []
    Qready = []
    Tw = [0 for x in range(10000)]
    Tn = [0 for x in range(10000)]
    faults = [0 for x in range(10000)]
    currentTask = None

    def __init__(self, Q):
        self.Q = Q

    def GetEDTask(self, removeFromQ):
        timeBuf = 9999999
        newTime = 0
        taskwED = None
        for i in range(len(self.Qready)):
            newTime = self.Qready[i].GetDeadline()
            if (timeBuf > newTime):
                timeBuf = newTime
                taskwED = self.Qready[i]
        if (removeFromQ):
            self.Qready.remove(taskwED)
        return taskwED

    def ToReadyQueue(self):
        for i in range(len(self.Q)):
            if self.Q[i].GetCreationTime() == self.currentTime:
                self.Qready.append(self.Q[i])

    def CheckForDeadlines(self):
        flt = 0
        flti = []
        for i in range(len(self.Qready)):
            if self.Qready[i].GetDeadline() < self.currentTime:
                flt += 1
                flti.append(i)
        if (self.currentTime == 0):
            self.faults[self.currentTime] = flt
        else:
            self.faults[self.currentTime] = self.faults[self.currentTime - 1] + flt
        for i in range(len(flti)):
            del self.Qready[flti[i]]
            for j in range(i, len(flti)):
                flti[j] -= 1


    def Work(self):
        self.currentTime = 0
        timewait = 0
        for self.currentTime in range(10000):
            if self.currentTime != 0:
                self.Tn[self.currentTime] = self.Tn[self.currentTime - 1]
            timewait = 0
            self.CheckForDeadlines()
            self.ToReadyQueue()
            if (self.currentTask != None and self.currentTask.GetExecutionTime() == 0):
                self.currentTask = None
            elif (self.currentTask != None):
                self.currentTask.WorkedOn()
            if (self.GetEDTask(False) == None and self.currentTask == None):
                self.Tn[self.currentTime] += 1
                continue
            elif (self.currentTask == None):
                self.currentTask = self.GetEDTask(True)
            for task in self.Qready:
                task.Wait()
                timewait += 1
            self.Tw[self.currentTime] = timewait

    def GetWaitTimes(self):
        return self.Tw

    def GetFaults(self):
        return self.faults

    def GetProcessorFreeTime(self):
        return self.Tn

