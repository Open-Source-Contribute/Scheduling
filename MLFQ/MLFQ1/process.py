class  Process:
    def __init__(self,name,arrive_time,serve_time):
        self.name=name                              # Process Name
        self.arrive_time=arrive_time                # Arrival Time
        self.serve_time=serve_time                  # Time for Serving
        self.left_serve_time=serve_time             # Remaining Time for Serving
        self.finish_time=0                          # Completion Time
        self.cycling_time=0                         # Turnaround Time
        self.w_cycling_time=0                       # Turnaround time with rights