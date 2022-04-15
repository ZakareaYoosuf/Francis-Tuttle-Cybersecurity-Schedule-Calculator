#Francis Tuttle Cybersecurity Grade Calculator by Zakarea Yoosuf

#Variable Declaration
gradeInput = 0
courseIndex = 0
loopBreaker = False
DECOR = "-------------------------------------------\n"


class Course:
#Initializes the course and assigns the attributes
    def __init__(self,name,hours,assignments):
        self.name=name
        self.hours=hours
        self.assignments=assignments
        self.days = self.hours/2.5
        self.grade = -1

#Adjusts the hours and assignments left within a partially completed course
    def adjustToCompletion(self,assignmentsCompleted):
        self.hours = self.hours * ((self.assignments - assignmentsCompleted)/self.assignments)
        self.assignments = self.assignments - assignmentsCompleted

#Changing amount of days required to complete the course
    def adjustDays(self,newDays):
        self.days = newDays
#Changing the grade of the course
    def adjustGrades(self,newGrades):
        self.grade = newGrades

#Defines, orders, and organizes courses into a list so that they may be referred to in an easy manner
courses = [
#Format: Course(name, hours, assignments)
    Course("Security Essentials Part 1", 25, 28),
    Course("Security Essentials Part 2", 50, 77),
    Course("Network Essentials", 75, 154),
    Course("IT Fundamentals", 90, 319),
    Course("Linux Essentials", 75, 137),
    Course("IOT No Python", 20, 81),
    Course("Python", 55, 84),
    Course("Network Security", 180, 608),
    Course("Ethical Hacking", 180, 422),
    Course("Cyber Forensics", 180, 569)
]
while True: 
#Collects and validates user input concerning the coursework a student has completed
    deb = False
    while not deb:
        for i in range(len(courses)): print(str(i+1) + ") " + courses[i].name)
        complete = input(DECOR + "Enter the latest course (or course number) being graded.\nIf you are done grading, enter \"quit\" without the quotation marks: ").upper()
        if complete == "QUIT":
            loopBreaker = True
            break
            
        for i in range(len(courses)):
            if courses[i].name.upper() == complete or complete == str(i+1):
                courseIndex = i
                deb = True
                break
    if loopBreaker: break

    deb = False
    while not deb:
        gradeInput = float(input("What is the student's grade in " + courses[courseIndex].name + "? "))
        if gradeInput > 100 or gradeInput < 0: continue 
        Course.adjustGrades(courses[courseIndex], gradeInput)
        deb = True

totalGrade = 0
coursesGraded = 0
totalHours = 0
for i in range(len(courses)):
    if courses[i].grade != -1:
        print(courses[i].name + ": \n  Grade: " + str(courses[i].grade) + "%\n  Hours: " + str(courses[i].hours))
        totalGrade += (courses[i].grade * courses[i].hours)
        coursesGraded += 1
        totalHours += courses[i].hours

print("The weighted final grade is a " + str(totalGrade/totalHours) +"%.")
