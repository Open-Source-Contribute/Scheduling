from collections import deque

class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
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
  Queue1: RR(Round Robin, Time-Slice = 17)
  Queue2: RR(Round Robin, Time-Slice = 25)
  Queue3: FCFS(First Come, First Served)
  """
  def __init__(self, queue: list[Process], current_time: int) -> None:
        self.ready_queue = queue # unfinished process is in this ready_queue
        self.current_time = current_time # current time
        self.finish_queue = deque(); # finished process is in this sequence queue

  def calculate_waiting_time(self) -> list[int]:
      waiting_times = []
      for i in range(len(self.finish_queue)):
          waiting_times.append(self.finish_queue[i].waiting_time)
      return waiting_times

  def calculate_turnaround_time(self) -> list[int]:
      turn_around_times = []
      for i in range(len(self.finish_queue)):
          turn_around_times.append(self.finish_queue[i].turn_around_time)
      return turn_around_times

  def calculate_completion_time(self) -> list[int]:
      completion_times = []
      for i in range(len(self.finish_queue)):
          completion_times.append(self.finish_queue[i].stop_time)
      return completion_times

  def calculate_remaining_burst_time_of_ready_queue(self) -> list[int]:
      remaining_burst_times = []
      for i in range(len(self.ready_queue)):
          remaining_burst_times.append(self.ready_queue[i].burst_time)
      return remaining_burst_times

  def print_process_info_of_queue(self) -> None:
      """
      This method prints out information of terminated processes in finish_queue
      """
      print("###########sequence of processes finished###########")
      for i in range(len(self.finish_queue)):
        print(self.finish_queue[i].process_name, "(",
              "arrival time: ", self.finish_queue[i].arrival_time,
              ", waiting time: ", self.finish_queue[i].waiting_time,
              ", completion time: ", self.finish_queue[i].stop_time,
              ", turnaround time: ", self.finish_queue[i].turn_around_time,
              ", remaining burst time: ", self.finish_queue[i].burst_time,
              ")")

  def print_current_time(self) -> None:
      """
      This method prints out the current time
      """
      print("###########current time: ", self.current_time, "##########")

  def update_waiting_time(self, process: Process) -> None:
      """
      This method updates waiting times of unfinished processes
      """
      process.waiting_time += self.current_time - process.stop_time


  def FCFS(self, queue: list[Process]) -> list[Process]:
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

  def RR(self, ready_queue: list[Process], time_slice: int) -> list[Process]:
      """
      RR(Round Robin)
      RR will be applied to MLFQ's Queue1 and Queue2
      A process can't use CPU for time more than time-slice
      If the process consume CPU up to time-slice, it will go back to ready queue
      """
      finished = deque() # sequence deque of terminated process
      # just for 1 cycle and unfinished processes will go back to queue
      for i in range(len(ready_queue)):
          cp = ready_queue.popleft() # current process

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
              ready_queue.append(cp)
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
      return finished, ready_queue

  def MLFQ(self) -> list[Process]:
      """
      MLFQ
      Queue1, Queue2(Round Robin): This queue will send process that is not finished during 1 cycle with time-slice
      Queue3(FCFS): This queue will finish all remaining processes
      """
      # Queue1(RR)
      finished, self.ready_queue = self.RR(self.ready_queue, 17)
      # add finished process to sequence queue
      self.finish_queue.extend(finished);

      # Queue2(RR)
      finished, self.ready_queue = self.RR(self.ready_queue, 25)
      # add finished process to sequence queue
      self.finish_queue.extend(finished);

      # Queue3(FCFS)
      finished = self.FCFS(self.ready_queue)
      # add finished process to sequence queue
      self.finish_queue.extend(finished);

      return self.finish_queue

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
