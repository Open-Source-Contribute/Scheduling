from process import Process

class Queue:
    def __init__ (self, level: int, process_list: list[Process]) -> None:
        self.level = level
        self.process_list = process_list
        self.q = 0 
    
    def size(self) -> int:
        return len(self.process_list)
    
    def get(self, index: int) -> Process:
        return self.process_list[index]
    
    def add(self, process: Process) -> None:
        self.process_list.append(process)
        
    def delete(self, index: int):
        self.process_list.remove(self.process_list[index])
    
    