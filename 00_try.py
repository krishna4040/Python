class student:
    id = int()
    name = str()
    def __init__(self , id , name) -> None:
        self.name = name
        self.id = id;
    def printdata(self):
        print(f"ID of student is: {self.id}")
        print(f"Name of student is: {self.name}")
        

l = [4,3,2,1]
a = sorted(l)

s01 = student(1,"krishna")
s01.printdata()