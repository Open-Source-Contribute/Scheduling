class Process:
    def __init__(self, name: str, arrive_time: float, serve_time: float):
        self.name = name
        self.arrive_time = arrive_time
        self.serve_time = serve_time
        self.left_serve_time = serve_time
        self.finish_time = 0
        self.cycling_time = 0
        self.turnaround_time = 0