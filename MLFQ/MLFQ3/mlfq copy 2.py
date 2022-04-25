from collections import deque
from queue import Queue

class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int):
        self.process_name = process_name # 프로세스명
        self.arrival_time = arrival_time # 도착시간
        self.burst_time = burst_time # 수행시간
        
        self.waiting_time = 0 # 대기 시간 합
        self.turn_around_time = 0 # 소요 시간
        
        self.complete = False # 수행 완료 여부를 나타내는 Boolean 값
        
def print_queue_info(p: Process):
    print("process name: ", p.process_name, 
          "\narrival time: ", p.arrival_time,
          "\nburst time: ", p.burst_time,
          "\nwaiting time: ", p.waiting_time, 
          "\nturnaround time: ", p.turn_around_time)
    
def update_waiting_time(queue, time):
    for i in range(queue.qsize()):
        p = queue.get()
        p.waiting_time += time
        queue.put(p)
    return queue
        
        
        
def FCFS(queue, current_time):
    sequence = []; # sequence of terminated process
    for i in range(queue.qsize()):
        current_process = queue.get();
        current_time += current_process.burst_time
        current_process.burst_time = 0;
        update_waiting_time(queue, current_process.burst_time)
        current_process.turn_around_time = current_time - current_process.arrival_time
        current_process.complete = True
        sequence.append(current_process)
        
    return sequence, current_time
    


def test():
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    
    queue = Queue()
    queue.put(P1)
    queue.put(P2)
    queue.put(P3)
    queue.put(P4)
    
    result, time = FCFS(queue, 0)    
    print_queue_info(result)
    print("current time: ", time)

test()
# def completionTest(queue):
#     for i in range(queue):
#         if not queue[i].complete:
#             return False
#     return True
