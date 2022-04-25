from collections import deque
from queue import Queue

class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_times: int):
        self.process_name = process_name # 프로세스명
        self.arrival_time = arrival_time # 도착시간
        self.burst_times = burst_times # 수행시간
        
        self.waiting_time = 0 # 대기 시간 합
        self.turn_around_time = 0 # 소요 시간
        
        self.complete = False # 수행 완료 여부를 나타내는 Boolean 값
        
        
        
def FCFS(queue):
    sequence = []; # sequence of terminated process
    while (len(queue)):
        temp = queue.pop()
        print(temp)
    

def test():
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    
    queue = Queue([P1, P2, P3, P4])
    
    FCFS(queue)    

test()
# def completionTest(queue):
#     for i in range(queue):
#         if not queue[i].complete:
#             return False
#     return True
