import matplotlib.pyplot as plt
import random
import math
import Erlang as el
import Task
import SMO
import numpy

a = []
lam = 1
k = 2
E = el.ErlangDistribution(k, lam)

def GenerateQ():
    Q = []
    next = 0
    i = 0
    time = GenerateTime()
    while (i < 10000):
        i += E.GenerateNextInternal() * 8
        t = Task.Task(i, time)
        Q.append(t)
    return Q

def GenerateTime():
    rnd = random.random()
    if(rnd < 0.3):
        return random.randrange(7) + 40
    elif (rnd >= 0.3 and rnd < 0.6):
        return random.randrange(5) + 40
    elif (rnd >= 0.6 and rnd < 0.8):
        return random.randrange(3) + 40
    else:
        return random.randrange(2) + 40


if __name__ == "__main__":
    QuEDF = []
    QuRM = []
    SMOs = []
    RMs = []
    Tw = []
    Tww =[]
    Tn = []
    t = [x for x in range(10000)]
    faults = []
    faultschange = []
    Tnchange = []
    Twchange = []
    FullWaitTime = []

    for lam in numpy.arange(1, 20, 0.5):
        E.ChangeLambda(lam)
        temp = GenerateQ()
        QuEDF.append(temp)

    QuRM = QuEDF[:]

    for i in range(len(QuEDF)):
        SMOs.append(SMO.EDF(QuEDF[i]))
        RMs.append(SMO.RM(QuRM[i]))

    buf1 = []
    buf2 = []
    buf3 = []

    for i in SMOs:
        i.Work()
        buf1 = i.GetFaults()
        buf2 = i.GetWaitTimes()
        buf3 = i.GetProcessorFreeTime()
        faults.append(buf1[:])
        Tw.append(buf2[:])
        Tn.append(buf3[:])

    for i in range(len(SMOs)):
        faultschange.append(faults[i][9999])
        Tnchange.append(Tn[i][9999])

    time = 0
    for o in range(len(SMOs)):
        time = 0
        for i in range(10000):
            time += Tw[o][i]
        FullWaitTime.append(time)

    for i in range(len(SMOs)):
        Tww.append(FullWaitTime[i])

    plt.stem(Tnchange, linefmt='C0:', markerfmt='C0o', bottom=1.1, basefmt='black')
    plt.show()
    plt.stem(faultschange, linefmt='C2:', markerfmt='C2o', bottom=1.1, basefmt='black')
    plt.show()
    plt.stem(Tww, linefmt='C4:', markerfmt='C4o', bottom=1.1, basefmt='black')
    plt.show()

    buf1.clear()
    buf2.clear()
    buf3.clear()
    Tw.clear()
    Tn.clear()
    faults.clear()
    faultschange.clear()
    Tnchange.clear()
    Twchange.clear()
    Tww.clear()

    for i in RMs:
        i.Work()
        buf1 = i.GetFaults()
        buf2 = i.GetWaitTimes()
        buf3 = i.GetProcessorFreeTime()
        faults.append(buf1[:])
        Tw.append(buf2[:])
        Tn.append(buf3[:])

    for i in range(len(SMOs)):
        faultschange.append(faults[i][9999])
        Tnchange.append(Tn[i][9999])

    time = 0
    for o in range(len(SMOs)):
        time = 0
        for i in range(10000):
            time += Tw[o][i]
        FullWaitTime.append(time)

    for i in range(len(SMOs)):
        Tww.append(FullWaitTime[i])

    plt.stem(Tnchange, linefmt='C0:', markerfmt='C0o', bottom=1.1, basefmt='black')
    plt.show()
    plt.stem(faultschange, linefmt='C2:', markerfmt='C2o', bottom=1.1, basefmt='black')
    plt.show()
    plt.stem(Tww, linefmt='C4:', markerfmt='C4o', bottom=1.1, basefmt='black')
    plt.show()
