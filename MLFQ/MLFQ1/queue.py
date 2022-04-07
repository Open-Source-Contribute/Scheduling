class Queue:
    def __init__(self,level,process_list):
        self.level=level
        self.process_list=process_list
        self.q=0
       
    def size(self):
        return len(self.process_list)
    
    def get(self,index):
        return self.process_list[index]    

    def add(self,process):
        self.process_list.append(process)
        
    def delete(self,index):
        self.process_list.remove(self.process_list[index])