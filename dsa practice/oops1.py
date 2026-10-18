class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum = 0
        for values in self.marks:
            sum+=values
        print(self.name,"your avg marks are:",sum/3)
s1=Student("karan",[56,6,84])
s1.get_avg()
        