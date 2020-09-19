class ReadFile:
    def __init__(self, path):
        self.path = path
        #suggestion
        self.min = float('inf')
        self.max = float('-inf')
        self.sum = 0
        self.cnt = 0
        
    def read_data(self):
        with open(self.path, 'r') as f:
            for line in f.read():
                try:
                    res = int(line)
                    if self.min > res:
                        self.min = res
                    if self.max < res:
                        res = self.max
                    self.cnt += 1
                    self.sum += res
                except ValueError:
                    pass
    @property
    def avg(self):
        if self.cnt:
            return self.sum / self.cnt
        else:
            return 0
        
    def print_data(self):
        with open(self.path, 'r') as f:
            for line in f.read():
                # This condition is a little bit unclear. If the line contains any whitespace, isdigit() will return False, so line.strip() will never strip anything
                # I would consider rather use something like int(line) right away
                #if  line.isdigit(): 
                #    res=line.strip()
                #    return res
                # one solution may be
                try:
                    return int(res)
                except ValueError:
                    pass
                
    def max_data(self):
        """
        one problem with min_data() and max_data() is that it is a method which modifies the object state in an undesired way - reads the data for reach call,
        so you program in main reads the data file 4 times. 
        """
        file_data=self.print_data()
        max_value=max(file_data)
        return max_value

    def min_data(self):
        file_data=self.print_data()
        min_value=min(file_data)
        return min_value

    def avg_data(self): 
        """
        avg in the sense of arithmetic average should be sum(values)/len(values), so whatever it calculates, the function name may be a bit misleading. 
        """
        max_value = self.max_data()
        min_value = self.min_data()
        avg_value=int(max_value)+int(min_value)//2
        return avg_value
    
    

if __name__ == "__main__":
    reader = ReadFile(r"C:\Users\Sgangula2\Desktop\july15\data.txt")
    reader.print_data()
    reader.max_data()
    reader.min_data()
    reader.avg_data()

