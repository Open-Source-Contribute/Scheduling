from collections import deque


class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        self.process_name = process_name  # process name
        self.arrival_time = arrival_time  # arrival time of the process
        # completion time of finished process or last interrupted time
        self.stop_time = arrival_time
        self.burst_time = burst_time  # remaining burst time
        self.waiting_time = 0  # total time of the process wait in ready queue
        self.turnaround_time = 0  # time from arrival time to completion time
        self.complete = False


class MLFQ:
    """
    MLFQ(Multi Level Feedback Queue)
    Queue(0): RR(Round Robin, time_slice = time_slices[0])
    Queue(1): RR(Round Robin, time_slice = time_slices[1])
    ...
    Queue(number_of_queues - 2):
        RR(Round Robin, time_slice = time_slices[number_of_queues - 2])
    Queue(number_of_queue - 1):
        FCFS(First Come, First Served)
    """
    def __init__(
        self,
        number_of_queues: int,
        time_slices: int,
        queue: list[Process],
        current_time: int
    ) -> None:
        # total number of mlfq's queues
        self.number_of_queues = number_of_queues
        # time slice of queues that round robin algorithm applied
        self.time_slices = time_slices
        # unfinished process is in this ready_queue
        self.ready_queue = queue
        # current time
        self.current_time = current_time
        # finished process is in this sequence queue
        self.finish_queue = deque()

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        """
        This method returns the sequence of finished processes
        """
        sequence = []
        for i in range(len(self.finish_queue)):
            sequence.append(self.finish_queue[i].process_name)
        return sequence

    def calculate_waiting_time(queue: list[Process]) -> list[int]:
        """
        This method calculates waiting time of processes
        """
        waiting_times = []
        for i in range(len(queue)):
            waiting_times.append(queue[i].waiting_time)
        return waiting_times

    def calculate_turnaround_time(queue: list[Process]) -> list[int]:
        """
        This method calculates turnaround time of processes
        """
        turnaround_times = []
        for i in range(len(queue)):
            turnaround_times.append(queue[i].turnaround_time)
        return turnaround_times

    def calculate_completion_time(queue: list[Process]) -> list[int]:
        """
        This method calculates completion time of processes
        """
        completion_times = []
        for i in range(len(queue)):
            completion_times.append(queue[i].stop_time)
        return completion_times

    def calculate_remaining_burst_time_of_ready_queue(
        queue: list[Process]
    ) -> list[int]:
        """
        This method calculate remaining burst time of processes
        """
        remaining_burst_times = []
        for i in range(len(queue)):
            remaining_burst_times.append(queue[i].burst_time)
        return remaining_burst_times

    def update_waiting_time(self, process: Process) -> None:
        """
        This method updates waiting times of unfinished processes
        """
        process.waiting_time += self.current_time - process.stop_time

    def FCFS(self, ready_queue: list[Process]) -> list[Process]:
        """
        FCFS(First Come, First Served)
        FCFS will be applied to MLFQ's last queue
        A first came process will be finished at first
        """
        finished = deque()  # sequence deque of finished process
        while (len(ready_queue) != 0):
            cp = ready_queue.popleft()  # current process

            # if process's arrival time is later than current time, update current time
            if (self.current_time < cp.arrival_time):
                self.current_time += cp.arrival_time

            # update waiting time of current process
            self.update_waiting_time(cp)
            # update current time
            self.current_time += cp.burst_time
            # finish the process and set the process's burst-time 0
            cp.burst_time = 0
            # set the process's turnaround time because it is finished
            cp.turnaround_time = self.current_time - cp.arrival_time
            # set the completion time
            cp.stop_time = self.current_time
            cp.complete = True
            # add the process to queue that has finished queue
            finished.append(cp)
        # FCFS will finish all remaining processes
        return finished

    def RR(self, ready_queue: list[Process], time_slice: int) -> list[Process]:
        """
        RR(Round Robin)
        RR will be applied to MLFQ's all queues except last queue
        All processes can't use CPU for time more than time_slice
        If the process consume CPU up to time_slice, it will go back to ready queue
        """
        finished = deque()  # sequence deque of terminated process
        # just for 1 cycle and unfinished processes will go back to queue
        for i in range(len(ready_queue)):
            cp = ready_queue.popleft()  # current process

            # if process's arrival time is later than current time, update current time
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
                cp.turnaround_time = self.current_time - cp.arrival_time
                cp.complete = True
                # add the process to queue that has finished queue
                finished.append(cp)

        # return finished processes queue and remaining processes queue
        return finished, ready_queue

    def MLFQ(self) -> list[Process]:
        for i in range(self.number_of_queues - 1):
            finished, self.ready_queue = self.RR(self.ready_queue, self.time_slices[i])
            self.finish_queue.extend(finished)

        finished = self.FCFS(self.ready_queue)
        self.finish_queue.extend(finished)

        return self.finish_queue


if __name__ == "__main__":
    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)

    queue = deque([P1, P2, P3, P4])
    number_of_queues = 3
    time_slices = [17, 25]

    if (len(time_slices) != number_of_queues - 1):
        exit()

    mlfq = MLFQ(number_of_queues, time_slices, queue, 0)
    finish_queue = mlfq.MLFQ()
    print(
        " process name\t\t: ",
        f"[{P1.process_name}, {P2.process_name}, ",
        f"{P3.process_name}, {P4.process_name}]")

    print(f" waiting time\t\t: {MLFQ.calculate_waiting_time([P1, P2, P3, P4])}")
    print(f" completion time\t: {MLFQ.calculate_completion_time([P1, P2, P3, P4])}")
    print(f" turn around time\t: {MLFQ.calculate_turnaround_time([P1, P2, P3, P4])}")

    print(f" sequnece of finished process: {mlfq.calculate_sequence_of_finish_queue()}")
