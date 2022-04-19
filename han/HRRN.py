
    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_processes = []
        process_data.sort(key=lambda x: x[1])
        '''
        함수 실행에 필요한 변수들을 정의해 주고, 프로세스를 도착시간으로 정렬을 합니다. 
        '''
        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            for j in range(len(process_data)):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    response_ratio = 0
                    response_ratio = float(((s_time - process_data[j][1]) + process_data[j][2]) / process_data[j][2])
                    '''
                    현재시간과 도착시간을 사용하여 프로세스의 대기시간을 구하고 이를 사용하여 프로세스의 response ratio를 구합니다.
                    '''
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], response_ratio])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                '''
                Response ratio를 구한 후에는 해당 프로세스에 response ratio와 arrive time, burst time을 큐에 담아줍니다.
                '''
                start_time.append(s_time)
                s_time = s_time + ready_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
                '''
                큐에 있는 값을 response ratio의 값으로 정렬을 해줍니다.
                정렬을 하고 난 후에는 현재 시간을 가장 response ratio가 높은 프로세스의 burst time만큼 추가시켜 줍니다.
                그리고 해당 프로세스를 queue에서 제거해 줍니다.
                '''
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + normal_queue[0][2]
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_processes.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(e_time)
                '''
                이는 예외를 처리하는 코드로서 만약 response ratio가 같거나 혹은 처음 시작했을 때 예외를 처리하기 위한 코드입니다.
                '''


