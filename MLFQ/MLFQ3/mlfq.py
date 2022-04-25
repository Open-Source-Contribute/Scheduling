from collections import deque

class Process:
    def __init__(self, burst_times, process_name):
        self.burst_times = burst_times
        self.process_name = process_name
        self.waiting_time = 0
        self.turn_around_time = 0
        self.response_time = -1
        self.i = 0
        self.length = len(burst_times)
        self.complete = False
        

def main():

    p1 = Process([5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4], 'p1')
    p2 = Process([4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8], 'p2')
    p3 = Process([8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6], 'p3')
    p4 = Process([3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3], 'p4')
    p5 = Process([16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4], 'p5')
    p6 = Process([11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8], 'p6')
    p7 = Process([14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10], 'p7')
    p8 = Process([4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6], 'p8')

    waiting = [] 
    ready_queue = deque([p1,p2,p3,p4,p5,p6,p7,p8])
    #test(ready_queue)
    #term = FCFS(ready_queue, waiting)
    #term = SJF(ready_queue, waiting)
    term = MLFQ(ready_queue, waiting)
    print_results(term)
    for process in term:
        print("process: ", process.process_name)
        print("waiting time: ", process.waiting_time)
        print("turn around time: ", process.turn_around_time)
        print("response time :", process.response_time)



def print_results(terminated):
    avg_wt = 0
    avg_tat = 0
    avg_rt = 0
    
    for process in terminated:
        avg_wt += process.waiting_time
        avg_tat += process.turn_around_time
        avg_rt += process.response_time
    avg_wt = avg_wt/len(terminated)
    avg_tat = avg_tat/len(terminated)
    avg_rt = avg_rt/len(terminated)
    print("Average waiting time:", avg_wt)
    print("Average turn-around time:", avg_tat)
    print("Average response time:", avg_rt)
    


    
def add_to_ready(ready_queue, process):
    temp = list(ready_queue)
    temp.append(process)
    temp.sort(key=lambda p: p.burst_times[p.i])
    #return deque(temp) #temp is sorted
    ready_queue.clear()
    ready_queue.extend(temp)


def sjf_update_waiting(waiting_queue, ready_queue, burst):   
    if(len(waiting_queue) is not 0):
        j = len(waiting_queue)-1
        while j >= 0:
            waiting_queue[j].burst_times[waiting_queue[j].i] -= burst 
            waiting_queue[j].waiting_time += burst
            if(waiting_queue[j].burst_times[waiting_queue[j].i]<= 0): #done waiting
                waiting_queue[j].waiting_time += waiting_queue[j].burst_times[waiting_queue[j].i]  
                waiting_queue[j].i+= 1
                add_to_ready(ready_queue, waiting_queue.pop())
                #ready_queue.append(waiting_queue.pop())
                j=len(waiting_queue)-1
            else:
                j -= 1
def update_waiting(waiting_queue, ready_queue, burst):
    
    if(len(waiting_queue) is not 0):
        j = len(waiting_queue)-1
        while j >= 0:
            waiting_queue[j].burst_times[waiting_queue[j].i] -= burst 
            waiting_queue[j].waiting_time += burst
            if(waiting_queue[j].burst_times[waiting_queue[j].i]<= 0): #done waiting
                #waiting_queue[j].waiting_time += abs(waiting_queue[j].burst_times[waiting_queue[j].i])  
                waiting_queue[j].waiting_time += waiting_queue[j].burst_times[waiting_queue[j].i]  
                waiting_queue[j].i+= 1
                ready_queue.append(waiting_queue.pop())
                j=len(waiting_queue)-1
            else:
                j -= 1

            
def add_to_waiting(waiting_queue, newProcess): 
    waiting_queue.append(newProcess)
    waiting_queue.sort(key=lambda p: p.burst_times[p.i], reverse=True)
            
            
def completionTest(ready_queue, waiting_queue):
    if len(ready_queue) == 0 and len(waiting_queue) == 0:
        return False
    return True

def view_ready(ready_queue):
    print("_________ready queue__________")
    for process in ready_queue:
        print(process.process_name)
    print('END')
    
def view_waiting(waiting_queue):
    if waiting_queue == []:
        print("waiting is empty")
        
    print("____________waiting__________")
    for process in waiting_queue:
        print("process:", process.process_name)
        print("burst time:", process.burst_times)
        print("time left in waiting:", process.burst_times[process.i])
    print("END")

              
def FCFS(ready_queue, waiting_queue,time=0):
    terminated = []
    # 모든 프로세스들이 끝날때까지 실행
    while(completionTest(ready_queue, waiting_queue)):
        # ready_queue에 프로세스가 없을 때(수행할 프로세스가 없을 때)
        if len(ready_queue) == 0:
            time+=1 # 시간 증가
            update_waiting(waiting_queue, ready_queue, 1) # waiting_time(대기시간 1 증가)
        else:
            # 수행할 프로세스가 있을 때
            process = ready_queue.popleft()  
            
            # 해당 프로세스가 수행 완료 되었는지 판단
            if not process.complete:
                # response time을 현재 시간으로 수정
                if(process.response_time == -1):
                    process.response_time = time
                        
                
                time += process.burst_times[process.i] # 수행 시간 만큼 현재 시간을 증가
                cpu_util += process.burst_times[process.i]

                update_waiting(waiting_queue, ready_queue, process.burst_times[process.i]) # waiting_time(대기시간을 수행시간만큼 증가)
                process.i += 1 # 프로세스의 다음 burst로 이동
                        
                # 한 프로세스의 모든 burst들을 끝냈을 때
                if(process.i >= process.length): 
                    process.complete = True # 완료됐다고 표시
                    process.turn_around_time = time # 소요시간을 현재 시간으로 설정
                    terminated.append(process) # 완료된 프로세스 목록에 저장
                else:
                    add_to_waiting(waiting_queue, process) # waiting_time 업데이트
                    
    print("total time:", time) # 총 소요시간 체크
    
    return terminated

def SJF(ready_queue, waiting_queue):
    time=0
    cpu_util = 0
    add_to_ready(ready_queue, ready_queue.pop())
    terminated = []
    while(completionTest(ready_queue, waiting_queue)):
        if len(ready_queue) == 0:
            time+=1
            sjf_update_waiting(waiting_queue, ready_queue, 1)
        else:
            process = ready_queue.popleft()    
            
            if not process.complete:
                #update process
                if(process.response_time == -1):
                    process.response_time = time
                #print(process.i)           
                
                time += process.burst_times[process.i] # a burst
                cpu_util += process.burst_times[process.i]


                sjf_update_waiting(waiting_queue, ready_queue, process.burst_times[process.i])
                process.i += 1
                        
                
                if(process.i >= process.length): 
                    process.complete = True
                    process.turn_around_time = time 
                    terminated.append(process)
                    #print("process: ", process.i, process.turn_around_time)
                    #that there are no more bursts to compute=>finished
                else:
                    
                    #idle_time += process.burst_times[process.i]
                    add_to_waiting(waiting_queue, process)
                    view_ready(ready_queue)  
                    view_waiting(waiting_queue)
    print("total time:", time)
    cpu_util_percent = (cpu_util/time)*100
    print("cpu utilization %: ", cpu_util_percent)
  
    
    return terminated

def round_robin(ready_queue, waiting_queue, quantum_time, time=0, cpu_util=0):
    terminated = [] # 완료된 프로세스 목록
    next_ready = deque()
    next_waiting = []
    while(len(ready_queue) != 0 or len(waiting_queue) != 0):
        process = ready_queue.popleft() # ready_queue에서 가장 앞에 있는 프로세스 수행
        
        # 프로세스가 종료되지 않았다면
        if not process.complete:
            # 프로세스의 response time을 업데이트
            if(process.response_time == -1):
                process.response_time = time
            # 프로세스의 남은 수행시간이 time slice(기준 시간)보다 큰 경우
            if(process.burst_times[process.i] > quantum_time):
                process.burst_times[process.i] -= quantum_time # 남은 수행 시간에서 time slice(기준 시간)만큼 차감
                time += quantum_time # 시간을 time slice(기준 시간)만큼 업데이트
                cpu_util += quantum_time # cpu_util 업데이트
                ready_queue.append(process) # 다시 ready_queue의 맨 뒤로 프로세스를 보냄
                update_waiting(waiting_queue, ready_queue, quantum_time) # 남은 수행 시간 및 대기 시간 업데이트
                update_waiting(next_waiting, next_ready, quantum_time) # 남은 수행 시간 및 대기 시간 업데이트
            else:
                # 프로세스의 남은 수행시간이 time slcie(기준 시간)보다 작은 경우, time slice 안에 프로세스가 수행 완료되는 경우
                time += process.burst_times[process.i]  # 남은 수행시간만큼 시간 업데이트
                cpu_util += process.burst_times[process.i] # cpu_util 업데이트
                update_waiting(waiting_queue, ready_queue, process.burst_times[process.i]) # 남은 수행 시간 및 대기 시간 업데이트
                update_waiting(next_waiting, next_ready, process.burst_times[process.i]) # 남은 수행 시간 및 대기 시간 업데이트
                process.i += 1 # 프로세스의 일부분 수행 시간이 종료됐으므로 해당 프로세스의 다음 부분 작업으로 포인터 이동
                    
            
                if(process.i >= process.length): # 프로세스의 모든 작업이 수행이 완료되면
                    process.complete = True # 완료됐다고 저장
                    process.turn_around_time = time  # 소요시간 저장
                    terminated.append(process) # 완료된 항목에 현재 프로세스 저장
                else: # 아직 프로세스의 작업이 남아있을 경우
                    add_to_waiting(next_waiting, process) # waiting_queue에 프로세스 삽입
                    view_ready(ready_queue)   # 결과 확인용 출력
                    view_waiting(waiting_queue) # 결과 확인용 출력
    
    return (next_waiting, next_ready, time, cpu_util) 
    # MLFQ는 Time Slice만큼 CPU를 차지하고 난 후 큐의 위치가 변경(우선순위가 변경)되기 때문에 
    # waiting_queue(이전 큐에서 Time Slice를 다 쓰고 내려온 프로세스들) => next_waiting(현재 큐에서 Time Slice를 다 쓰고 내리는 프로세스들)
    # 위의 로직을 위해 해당 프로세스들의 목록을 return해준다.

def MLFQ(ready_queue, waiting_queue):
    waiting_queue, ready_queue, time, cpu_util = round_robin(ready_queue,waiting_queue, 5, 0)
    waiting_queue, ready_queue, time, cpu_util = round_robin(ready_queue,waiting_queue, 10, time)
    return FCFS(ready_queue, waiting_queue, time, cpu_util)


if __name__=='__main__':
    main()