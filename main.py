import os, platform
import sys
from multiprocessing import Process
from datetime import datetime
from time import sleep

def callProcessNumber(loopNumber, delay, processTime):

    platformOs = platform.system()
    print(platformOs.capitalize() + " (PADRE) -> PID:", os.getpid(), '\n');

    for idx in range(loopNumber):
        print("Llamando al", str(idx + 1) + "º proceso.")
        if platformOs == "Windows":
            process = Process(target=hijo);
            process.start();
            message(process.pid, datetime.now());
            process.join(processTime);
            
        elif platformOs == "Linux":
            newPid = os.fork();
            if newPid == 0:
                hijo(processTime);
            if newPid != 0:
                message(newPid, datetime.now());
        else:
            print('No se ejecutar procesos en tu OS.')
            break;
        sleep(delay)
    
def padre(customNumber, delay, processTime):
    callProcessNumber(customNumber, delay, processTime);
    print('\nTerminada la llamada de procesos');
    print('\n\tRealizados:', customNumber);
    print('\n\tTiempo total:', (delay * customNumber) + (processTime + customNumber), 'seg.')

def message(pId, timeStamp):
    str_timeStamp = timeStamp.strftime("%H:%M:%S")
    print("Iniciando el proceso:", pId, "a las:", str_timeStamp)

def hijo(time=3):
    processId = str(os.getpid());
    print('\n > Iniciando el proceso con PID: ' + processId);
    sleep(time);
    print(' ** Terminando el proceso con PID: ' + processId + " ** \n")
    sys.exit(0);

if __name__ == "__main__":
    padre(10, 10, 3);