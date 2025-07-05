class Student:

    def __init__(self,marks):
        self.marks = marks
        if not isinstance(marks, (int, float)):
            raise TypeError("Marks must be a number (int or float)")
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.marks = marks
        

    def showResults(self):
        if self.marks >90 :
            grade = "A"
        elif self.marks > 80:
            grade = "B"
        elif self.marks > 70:
            grade = "C"
        elif self.marks > 60:
            grade = "D"
        elif self.marks > 50:
            grade = "E"
        else:
            grade = "F"

        print(f"Marks: {self.marks}, Grade: {grade}")

student1 = Student(85)
student1.showResults()  # Marks: 85, Grade: B

student2 = Student("A+")  
# Raises TypeError: Marks must be a number

student3 = Student(110)  
# Raises ValueError: Marks must be between 0 and 100
