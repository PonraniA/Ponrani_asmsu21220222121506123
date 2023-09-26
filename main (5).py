
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
    # Sort time list of students in descending order of cgpa
    sorted_students = sorted(student_list, 
                            key=lambda student: student.cgpa,
                            reverse=True)
 # Syntax - lambda arg:exp   
    return sorted_students


 # Example usage:
students = [
    Student("Shree", "A123", 9.9),
    Student("Sarah", "A124", 7.8),
    Student("Clara", "A125", 8.6),
    Student("Prabu", "A126", 9.8)
       ]
  
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))