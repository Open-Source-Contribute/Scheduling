

def calcultate_turn_around_time(
    arrival_time: list, burst_time: list, no_of_process: int
) -> list:
    current_time = 0
    finished_process_count = 0
    finished_process = [0] * no_of_process
    turn_around_time = [0] * no_of_process
    sorted_arrival_time = arrival_time.copy()
    sorted_arrival_time.sort()
    while no_of_process > finished_process_count:
        if sorted_arrival_time[0] > current_time:
            current_time = sorted_arrival_time[0]
        response_ratio = -1
        loc = 0
        temp = 0
        for i in range(0, no_of_process):
            if finished_process[i] == 0 and arrival_time[i] <= current_time:
                temp = (burst_time[i] + (current_time - arrival_time[i])) /\
                    burst_time[i]
            if response_ratio < temp:
                response_ratio = temp
                loc = i
        turn_around_time[loc] = current_time + burst_time[loc] - arrival_time[loc]
        current_time += burst_time[loc]
        finished_process[loc] = 1
        finished_process_count += 1
        sorted_arrival_time.remove(arrival_time[loc])

    return turn_around_time


def calculate_waiting_time(
    turn_around_time: list, burst_time: list, no_of_process: int
) -> list:
    waiting_time = [0] * no_of_process
    for i in range(0, no_of_process):
        waiting_time[i] = turn_around_time[i] - burst_time[i]
    return waiting_time


def calcuate_average_time(
    waiting_time: list, turn_around_time: list, no_of_process: int
) -> None:
    merge_waiting_time = 0
    merge_turn_around_time = 0
    for i in range(0, no_of_process):
        merge_waiting_time += waiting_time[i]
        merge_turn_around_time += turn_around_time[i]

    print("average waiting time :", merge_waiting_time / no_of_process)
    print("average turn around time :", merge_turn_around_time / no_of_process)
