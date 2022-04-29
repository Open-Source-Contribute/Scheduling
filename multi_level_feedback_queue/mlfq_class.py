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
        
class MLFQ:
  """
  MLFQ(Multil Level Feedback Queue)
  Queue1 >>> RR(Round Robin, Time-Slice = 17)
  Queue2 >>> RR(Round Robin, Time-Slice = 25)
  Queue3 >>> FCFS(First Come, First Served)
  """
  def __init__(self, queue, current_time):
        self.queue = queue # unfinished process is in this queue
        self.current_time = current_time # current time
        self.sequence = deque(); # finished process is in this sequence queue
        
  def print_process_info_of_queue(self):
      """
      This method prints out information of terminated processes in sequence
      """
      print("###########sequence of processes finished###########")
      for i in range(len(self.sequence)):
        print(self.sequence[i].process_name, "(",
              "arrival time: ", self.sequence[i].arrival_time,
              ", waiting time: ", self.sequence[i].waiting_time,
              ", completion time: ", self.sequence[i].stop_time,
              ", turnaround time: ", self.sequence[i].turn_around_time,
              ", left burst time: ", self.sequence[i].burst_time,
              ")")    
        
  def print_current_time(self):
      """
      This method prints out the current time
      """
      print("###########current time: ", self.current_time, "##########")
    
  def update_waiting_time(self, process):
      """
      This method updates waiting times of unfinished processes
      """
      process.waiting_time += self.current_time - process.stop_time
          
          
  def FCFS(self, queue):
      """
      FCFS(First Come, First Served)
      FCFS will be applied to MLFQ's Queue3
      A first came process will be finished at first
      """
      finished = deque(); # sequence deque of terminated process
      while (len(queue) != 0):
        cp = queue.popleft() # current process
        
        # if the process' arrival time is later than current time, update current time
        if (self.current_time < cp.arrival_time):
            self.current_time += cp.arrival_time
        
        # update waiting time of unfinished processes
        self.update_waiting_time(cp)
        # update current time
        self.current_time += cp.burst_time 
        # finish the process and set the process' burst-time zero
        cp.burst_time = 0 
        # update the process' turnaround time because it is finished
        cp.turn_around_time = self.current_time - cp.arrival_time
        # set the finish time
        cp.stop_time = self.current_time
        cp.complete = True
        # add the process to queue that has finished queue
        finished.append(cp)
      # FCFS will finish all remaining processes
      return finished

  def RR(self, queue, time_slice):
      """
      RR(Round Robin)
      RR will be applied to MLFQ's Queue1 and Queue2
      A process can't use CPU for time more than time-slice
      If the process consume CPU up to time-slice, it will go back to ready queue
      """
      finished = deque() # sequence deque of terminated process
      # just for 1 cycle and unfinished processes will go back to queue
      for i in range(len(queue)): 
          cp = queue.popleft() # current process
          
          # if the process' arrival time is later than current time, update current time
          if (self.current_time < cp.arrival_time):
              self.current_time += cp.arrival_time
          
          # update waiting time of unfinished processes
          self.update_waiting_time(cp)
          # if the burst time of process is bigger than time-slice
          if (cp.burst_time > time_slice):
              # use CPU for only time-slice
              self.current_time += time_slice
              # update remaining burst time
              cp.burst_time -= time_slice
              # update end point time
              cp.stop_time = self.current_time
              # locate the process behind the queue because it is not finished
              queue.append(cp)
          else:
              # use CPU for remaining burst time
              self.current_time += cp.burst_time
              # set burst time 0 because the process is finished
              cp.burst_time = 0
              # set the finish time
              cp.stop_time = self.current_time
              # update the process' turnaround time because it is finished
              cp.turn_around_time = self.current_time - cp.arrival_time
              cp.complete = True
              # add the process to queue that has finished queue
              finished.append(cp)
      
      # return finished processes queue and remaining processes queue
      return finished, queue 

  def MLFQ(self):
      """
      MLFQ
      Queue1, Queue2(Round Robin)
      >>> This queue will send process that is not finished during 1 cycle with time-slice
      Queue3(FCFS)
      >>> This queue will finish all remaining processes
      """
      # Queue1(RR)
      finished, ready_queue = self.RR(self.queue, 17)
      # add finished process to sequence queue
      self.sequence.extend(finished);
      
      # Queue2(RR)
      finished, ready_queue = self.RR(ready_queue, 25)
      # add finished process to sequence queue
      self.sequence.extend(finished);
      
      # Queue3(FCFS)
      finished = self.FCFS(ready_queue)
      # add finished process to sequence queue
      self.sequence.extend(finished);   
      
      return self.sequence
  
if __name__ == "__main__":
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    
    queue = deque([P1, P2, P3, P4])
    
    mlfq = MLFQ(queue, 0)
    sequence = mlfq.MLFQ()
    mlfq.print_process_info_of_queue()
    mlfq.print_current_time()