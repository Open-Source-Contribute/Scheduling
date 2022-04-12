"""
Shortest job remaining first
Please note arrival time and burst
Please use spaces to separate times entered.
"""
from __future__ import annotations

import pandas as pd


def calculate_waitingtime(
    arrival_time: list[int], burst_time: list[int], no_of_processes: int
) -> list[int]:
    """
    Arrival_time : 도착시간을 담은 리스트
    Burst_time : 수행시간
    No_of_processes : 프로세스의 개수
    ->list[int] : list를 반환합니다.
    즉 위 함수는 도착시간, 수행시간, 프로세스의 개수를 인자로 받아 각각의 대기시간에 대해 리스트에 저장하여 반환합니다.
    """
    remaining_time = [0] * no_of_processes
    waiting_time = [0] * no_of_processes
    for i in range(no_of_processes):
        remaining_time[i] = burst_time[i]
    complete = 0
    increment_time = 0
    minm = 999999999
    short = 0
    check = False
    # Process until all processes are completed
    while complete != no_of_processes:
        for j in range(no_of_processes):
            if arrival_time[j] <= increment_time:
                if remaining_time[j] > 0:
                    if remaining_time[j] < minm:
                        minm = remaining_time[j]
                        short = j
                        check = True
    """
    위 코드는 SJF의 필수부분 현재 도착한 프로그램 중에
    가장 짧은 burst time을 가지는 프로세스를 정하여
    수행시간을 구하는 코드이다.
    """
        if not check:
            increment_time += 1
            continue
        remaining_time[short] -= 1

        minm = remaining_time[short]
        if minm == 0:
            minm = 999999999

        if remaining_time[short] == 0:
            complete += 1
            check = False

            # Find finish time of current process
            finish_time = increment_time + 1

            # Calculate waiting time
            finar = finish_time - arrival_time[short]
            waiting_time[short] = finar - burst_time[short]

            if waiting_time[short] < 0:
                waiting_time[short] = 0
    """
    종료시간과 도착시간을 뺀 후에 그 값에
    각각의 수행시간을 빼게 되면, 각각의 대기 시간이 구해진다.
    """
        # Increment time
        increment_time += 1
    return waiting_time


def calculate_turnaroundtime(
    burst_time: list[int], no_of_processes: int, waiting_time: list[int]
) -> list[int]:

    turn_around_time = [0] * no_of_processes
    for i in range(no_of_processes):
        turn_around_time[i] = burst_time[i] + waiting_time[i]
    return turn_around_time
    """
    Burst_time : 프로세스 작동시간
    No_of_processes : 프로세스 갯수
    Wating_time : 프로세스 대기 시간
    종료시간을 알려주는 함수로서, 각 프로세스가 언제 종료되는지 리스트 값으로 반환해 준다.
    """

def calculate_average_times(
    waiting_time: list[int], turn_around_time: list[int], no_of_processes: int
) -> None:
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(no_of_processes):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
    print("Average waiting time = %.5f" % (total_waiting_time / no_of_processes))
    print("Average turn around time =", total_turn_around_time / no_of_processes)
    """
    각 리스트에 평균을 구하여 print함수로 사용자에게 결과값을 보여줍니다.
    """

if __name__ == "__main__":
    print("Enter how many process you want to analyze")
    no_of_processes = int(input())
    burst_time = [0] * no_of_processes
    arrival_time = [0] * no_of_processes
    processes = list(range(1, no_of_processes + 1))

    for i in range(no_of_processes):
        print("Enter the arrival time and burst time for process:--" + str(i + 1))
        arrival_time[i], burst_time[i] = map(int, input().split())

    waiting_time = calculate_waitingtime(arrival_time, burst_time, no_of_processes)

    bt = burst_time
    n = no_of_processes
    wt = waiting_time
    turn_around_time = calculate_turnaroundtime(bt, n, wt)

    calculate_average_times(waiting_time, turn_around_time, no_of_processes)

    fcfs = pd.DataFrame(
        list(zip(processes, burst_time, arrival_time, waiting_time, turn_around_time)),
        columns=[
            "Process",
            "BurstTime",
            "ArrivalTime",
            "WaitingTime",
            "TurnAroundTime",
        ],
    )

    # Printing the dataFrame
    pd.set_option("display.max_rows", fcfs.shape[0] + 1)
    print(fcfs)
