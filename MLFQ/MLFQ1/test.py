from process import Process
from queue import Queue
from MLFQ1 import MulitlevedFeedbackQueue
from round_robin import RR
'''
Test Code
'''    
if __name__=='__main__':
    # The Production Process
    process_list=[]
    processA=Process('A',0,4)
    processB=Process('B',1,3)
    processC=Process('C',2,4)
    processD=Process('D',3,2)
    processE=Process('E',4,4)
    process_list.append(processA),process_list.append(processB),process_list.append(processC)
    process_list.append(processD),process_list.append(processE)
    # Use RR Scheduling Algorithm, Time slice 1
    print('#################################################################')
    print('---------------------Round-Robin Scheduling----------------------')
    print('#################################################################')
    rr=RR(process_list,1)
    rr.scheduling()
    
    # Using MLFQ Algorithm
    print()
    print('#################################################################')
    print('--------------Multi-Level-Feedback-Queue Scheduling--------------')
    print('#################################################################')
    processA=Process('A',0,4)
    processB=Process('B',1,3)
    processC=Process('C',2,4)
    processD=Process('D',3,2)
    processE=Process('E',4,4)
    
    process_list0,process_list1,process_list2=[],[],[]
    process_list0.append(processA),process_list0.append(processB)
    process_list1.append(processC),process_list1.append(processD)
    process_list2.append(processE)
    
    # Queue
    queue_list=[]
    queue0=Queue(0,process_list0)
    queue1=Queue(1,process_list1)
    queue2=Queue(2,process_list2)
    queue_list.append(queue0),queue_list.append(queue1),queue_list.append(queue2)
    # Using MLFQ Scheduling, Time slice or the First Queue is 1
    mfq=MulitlevedFeedbackQueue(queue_list,1)
    mfq.scheduling()