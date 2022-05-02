from collections import deque

class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.stop_time = arrival_time # end time point or finish time point
        self.burst_time = burst_time

        self.waiting_time = 0
        self.turn_around_time = 0

        self.complete = False

def print_process_info(p):
    print("process name: ", p.process_name,
        "\narrival time: ", p.arrival_time,
        "\nburst time: ", p.burst_time,
        "\nwaiting time: ", p.waiting_time,
        "\nturnaround time: ", p.turn_around_time)

def update_waiting_time(process, current_time):
    process.waiting_time += current_time - process.stop_time


def FCFS(queue, current_time):
    finished = deque(); # sequence of terminated process
    while (len(queue) != 0):
        cp = queue.popleft() # current process

        if (current_time < cp.arrival_time):
            current_time += cp.arrival_time

        update_waiting_time(cp, current_time)
        current_time += cp.burst_time
        cp.burst_time = 0
        cp.turn_around_time = current_time - cp.arrival_time
        cp.stop_time = current_time
        cp.complete = True

        finished.append(cp)
    return finished, current_time

def RR(queue, current_time, time_slice):
    finished = deque()
    for i in range(len(queue)):
        cp = queue.popleft() # current process

        if (current_time < cp.arrival_time):
            current_time += cp.arrival_time

        update_waiting_time(cp, current_time)
        if (cp.burst_time > time_slice):
            current_time += time_slice
            cp.burst_time -= time_slice
            cp.stop_time = current_time
            queue.append(cp)
        else:
            current_time += cp.burst_time
            cp.burst_time = 0
            cp.stop_time = current_time
            cp.turn_around_time = current_time - cp.arrival_time
            cp.complete = True
            finished.append(cp)

    return finished, queue, current_time

def MLFQ(queue, current_time):
    sequence = deque();

    finished, ready_queue, current_time = RR(queue, 0, 17)
    sequence.extend(finished);

    finished, ready_queue, current_time = RR(ready_queue, current_time, 25)
    sequence.extend(finished);

    finished, current_time = FCFS(ready_queue, current_time)
    sequence.extend(finished);

    return sequence, current_time

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
