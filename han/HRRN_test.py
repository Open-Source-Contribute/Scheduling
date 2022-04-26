import numpy as np
class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int):
        self.process_name = process_name 
        self.arrival_time = arrival_time 
        self.burst_time = burst_time         
        self.waiting_time = 0 
        self.turn_around_time = 0 
    """
    프로세스 클래스
    """


          
def HRRN(process_list: list):
    act=process_list.copy()#현재 완료되지 않은 프로세스들의 리스트
    act.sort(key=lambda x: x.arrival_time)#도착 시간을 기반으로 정렬한다.
    current_time=0
    merge_turn_around_time=0
    merge_waiting_time=0
    """
    평균을 구하기 위한 변수들
    """
    while len(act)>0:
        if act[0].arrival_time>current_time:
            current_time=act[0].arrival_time
            """
            만약 전체 프로세스는 종료가 되지 않았는데 현재시간에 도착한 프로세스가 아무것도 없을 경우
            현재 완료되지 않은 프로세스 리스트에서 가장 도착시간이 빠른 함수로 현재시간 설정
            """
        response_ratio=-1
        loc=0
        for i in range(0, len(act)):
            if  act[i].arrival_time<current_time:#만약 현재 도착한 프로세스가 있다면
            temp=(act[i].burst_time+(current_time-act[i].arrival_time))/act[i].burst_time#response ratio 계산
            if response_ratio<temp:
                response_ratio=temp
                loc=i
        act[loc].waiting_time=current_time-act[loc].arrival_time#waiting time 계산
        current_time+=act[loc].burst_time#현재 시간에서 프로세스가 실행된 시간 만큼 더해준다.
        act[loc].turn_around_time=current_time-act[loc].arrival_time#turn around time 계산
        merge_turn_around_time+=act[loc].turn_around_time
        merge_waiting_time+=act[loc].waiting_time#평균을 위해 더해준다.
        act.pop(loc)#실행이 된다면 리스트에서 제외한다.
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

