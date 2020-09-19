class ReadFile:
    def __init__(self, path):
        self.path = path
    def print_data(self):
        with open(self.path, 'r') as f:
            for line in f.read():
                if  line.isdigit():
                    res=line.strip()
                    return res
    def max_data(self):
        file_data=self.print_data()
        max_value=max(file_data)
        return max_value

    def min_data(self):
        file_data=self.print_data()
        min_value=min(file_data)
        return min_value

    def avg_data(self):
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

