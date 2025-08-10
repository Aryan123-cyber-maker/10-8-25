class Attendence:
    Teacher = "Mr brown"
    room = "Science block"
    Year = "Year 8"

    def __init__(self,name,age,birthday):
        self.name = name 
        self.age = age
        self.birthday = birthday

student_1 = Attendence("Aryan",13,"2011-11-23")
student_2 = Attendence("Riya",12,"2012-05-15")

print(student_1.name)
print(student_1.age)
print(student_1.birthday)
print(student_1.Teacher)
print(student_1.room)


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

rectange_1 = Rectangle(10, 5)
print(rectange_1.area())
print(rectange_1.perimeter())