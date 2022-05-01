import numpy as np
class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turn_around_time = 0




def HRRN(process_list: list):
    act=process_list.copy()
    act.sort(key=lambda x: x.arrival_time)
    current_time=0
    merge_turn_around_time=0
    merge_waiting_time=0

    while len(act)>0:
        if act[0].arrival_time>current_time:
            current_time=act[0].arrival_time

        response_ratio=-1
        loc=0
        for i in range(0, len(act)):
            if  act[i].arrival_time<current_time:
            temp=(act[i].burst_time+(current_time-act[i].arrival_time))/act[i].burst_timeSs
            if response_ratio<temp:
                response_ratio=temp
                loc=i
        act[loc].waiting_time=current_time-act[loc].arrival_time
        current_time+=act[loc].burst_time
        act[loc].turn_around_time=current_time-act[loc].arrival_time#
        merge_turn_around_time+=act[loc].turn_around_time
        merge_waiting_time+=act[loc].waiting_time
        act.pop(loc)
    for i in range(0, len(process_list)):
        print(process_list[i].process_name, " arrival time :", process_list[i].arrival_time," burst time :", process_list[i].burst_time," waiting time :", process_list[i].waiting_time," turn around time :", process_list[i].turn_around_time)

    print("average waiting time :", merge_turn_around_time/len(process_list))
    print("average turn around time :", merge_waiting_time/len(process_list))

if __name__ == "__main__":

    p1=Process("p1", 0, 53)
    p2=Process("p2", 3, 10)
    p3=Process("p3", 5, 13)
    p4=Process("p4", 7, 150)

    process_list=[p1, p2, p3, p4]
    HRRN(process_list)
