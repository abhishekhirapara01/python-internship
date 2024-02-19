
class Student:
    def __init__(self,name):
      self.studentname = name
      self.studentgrades = []

    def add_grade(self,grade):
      if not (0 <= grade <= 100):
        raise ValueError("Grade must beetween 0 to 100")
      self.studentgrades.append(grade)

    def calculate_average(self):
      if not self.studentgrades:
        raise ValueError("No grades")
      return sum(self.studentgrades) / len(self.studentgrades)

try:
  a = Student("Abhishek hirapara")
  a.add_grade(0)
  a.add_grade(500)
  a.add_grade(500)
  average_grade = a.calculate_average()
  print("Average grade is: ",average_grade)
except ValueError:
  print("Error")
