from mlfq_deque import Process, MLFQ
from collections import deque

def print_process_info_of_queue(queue):
    for i in range(len(queue)):
        print(queue[i].process_name, "(",
              "arrival time: ", queue[i].arrival_time,
              ", waiting time: ", queue[i].waiting_time,
              ", completion time: ", queue[i].stop_time,
              ", turnaround time: ", queue[i].turn_around_time,
              ", left burst time: ", queue[i].burst_time,
              ")")

def test():
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    
    queue = deque([P1, P2, P3, P4])
    
    sequence, current_time = MLFQ(queue, 0)
    
    print_process_info_of_queue(sequence);
    print("current time: ", current_time)

test()
