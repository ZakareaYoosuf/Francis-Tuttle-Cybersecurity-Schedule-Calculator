#Francis Tuttle Cybersecurity Schedule Calculator by Zakarea Yoosuf

#Variable Declaration
startIndex = 0
endIndex = 0
totalHours= 0
DECOR = "-------------------------------------------\n"


class Course:
#Initializes the course and assigns the attributes
    def __init__(self,name,hours,assignments):
        self.name=name
        self.hours=hours
        self.assignments=assignments
        self.days = self.hours/2.5

#Adjusts the hours and assignments left within a partially completed course
    def adjustToCompletion(self,assignmentsCompleted):
        self.hours = self.hours * ((self.assignments - assignmentsCompleted)/self.assignments)
        self.assignments = self.assignments - assignmentsCompleted

#Changing amount of days required to complete the course
    def adjustDays(self,newDays):
        self.days = newDays

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

#Collects and validates user input concerning the coursework a student has completed
deb = False
while not deb:
    for i in range(len(courses)): print(str(i+1) + ") " + courses[i].name)
    complete = input(DECOR + "Enter the latest course (or course number) you have fully completed\nIf you haven't yet completed a course, enter \"nothing\" or \"0\" without the quotation marks:  ").upper()
    if complete == "NOTHING" or complete == "0":break
    for i in range(len(courses)):
        if courses[i].name.upper() == complete or complete == str(i+1):
            startIndex = i+1 #represents the course a student should be working on
            deb = True
            break

#Since Cyber Forensics is the last course, completing it would signify completion of the program as a whole
if complete == courses[len(courses)-1].name.upper(): 
    print("You're Already done with the program!")
    quit()
#Collects and validates partial completion of a student's current course and adjusts for accordingly
while True:
    nextCourseCompleted = int(input(DECOR + "How many assignments have you completed in " + courses[startIndex].name + " (The next course)? 0 is a Valid answer!\nEnter: "))
    if nextCourseCompleted <= courses[startIndex].assignments:break
Course.adjustToCompletion(courses[startIndex],nextCourseCompleted)

#Collects and validates the goal course that the student wants to complete within a specific time frame
deb = False
while not deb:
    for i in range(len(courses)): print(str(i+1) + ") " + courses[i].name)
    complete = input(DECOR + "Enter the course (or course number) you want to have done by the end of the alloted time: ").upper()
    for i in range(len(courses)):
        if courses[i].name.upper() == complete or complete == str(i+1):
            endIndex = i+1
            deb = True
            break

#Collects and validates the aforementioned time frame (refer to line 66)
daysLeft = 0
while True:
    daysLeft = int(input(DECOR + "Enter the amount of school days alotted to this work: "))
    if daysLeft > 0:break

#Calculates and displays the proper guidelines for a student to complete their selected amount of work within a specific time frame
print(DECOR)
for i in range(startIndex,endIndex): totalHours+=courses[i].hours
for i in range(startIndex,endIndex):
    Course.adjustDays(courses[i], courses[i].hours/totalHours * daysLeft)
    print(courses[i].name + ": " + str(round(courses[i].assignments/courses[i].days,2)) + " assignments per day for " + str(round(courses[i].days,2)) + " days.")

