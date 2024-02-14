students = []

A = int(input("How many student? : "))
for i in range(A):
  studentInformation = {
    "name" : input("Enter student name: "),
    "age" : int(input("Enter student age: ")), 
    "subjects" : []
  }
 
  B = int(input("How many subjects? : "))
  sum = 0

  for j in range(B):
    
      subject = input("Enter student subjects name: ")
      grade = int(input("Enter student grade: "))
      
      passing_status = grade >= 50

      studentInformation["subjects"].append({
         "name" : subject,
         "grade" : grade,
         "pass_status" : passing_status
      })

      sum += grade

  average_grade = sum / B

  studentInformation["average_grade"] = average_grade

  students.append(studentInformation)

print("--Student Information--")

for student in students:
    print("Student Name:", student["name"])
    print("Student Age:", student["age"])
    print("Subjects:")

    for subject in student["subjects"]:
       print("--Name: ",subject["name"])
       print("Garde: ",subject["grade"])
       print("Pass Status: ",subject["pass_status"])
    print("Average Grade: ",student["average_grade"])
    
    #subjectMarks = studentSubjects["grade"]

    #if subjectMarks >= 50:
      #bool=True
      #print("Congrats, you are passed this exam",bool)
    #else:
      #bool=False
      #print("Sorry, you are failed this exam",bool)
    #print("Boolean: True means pass or False means fail")


    #sum = sum + subjectMarks
  #print("TotalMarks: ",sum)

  #def avg():
    #average = sum / B
    #print("Average: ",average)
  #avg()

