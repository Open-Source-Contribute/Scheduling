class RR:
    def __init__(self,process_list,q):
        self.process_list=process_list
        self.q=q
    def scheduling(self):
        self.process_list.sort(key=lambda x:x.arrive_time) # sort by arrival time
        len_queue=len(self.process_list) # length of process queue
        index=int(0)  # indexes
        q=self.q      # time slice
        running_time=int(0) # time alreadt running
        
        # Scheduling Loop
        while(True):
            # The current process
            current_process=self.process_list[index%len_queue]
            # Determine whether the current process has been completed
            if current_process.left_serve_time>0: 
                # Calculate the completion time
                # The service time is greater than or equal to the time slice, then the completion time is + Time slice time The process is not over yet
                # The service time is less than the time slice, then the completion time is added to the original time of service
                if current_process.left_serve_time>=q:
                    running_time+=q
                    #print(current_process.name,running_time,index)
                    current_process.left_serve_time-=q
                    
                else :
                    #print('%s The service time is less than the current time slice '%current_process.name)
                    running_time+=current_process.left_serve_time
                    current_process.left_serve_time=0
            
            
            # Completed
            if current_process.left_serve_time==0:
                # Calculate the completion time
                current_process.finish_time=running_time
                # Calculate turnaround time
                current_process.cycling_time=current_process.finish_time-current_process.arrive_time
                # Calculate turnaround time with rights
                current_process.w_cycling_time=float(current_process.cycling_time)/current_process.serve_time
                # Print
                # print('%s (completed process , The details are as follows) ：'%current_process.name)
                print(' Process name ：%s , Completion time ： %d , Turnaround time ：%d , Turnaround time with rights ： %.2f'%(current_process.name,current_process.finish_time,current_process.cycling_time,current_process.w_cycling_time))
                # Eject
                self.process_list.remove(current_process)
                len_queue=len(self.process_list)
                # After a process has completed its task, index Go back first, Then add,  To keep pointing to the next process that needs to be scheduled
                index-=1
            # index Regular increase
            index+=1     
            
            # If ther is no process in the queue, execution is complete
            if len(self.process_list)==0:
                break
            
            # change index, avoid it because index Greater than len, This leads to an error in taking the mold
            if index>=len(self.process_list):
                index=index%len_queue