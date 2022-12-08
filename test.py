# # demo is the function name
# def demo(name, age):
#     # print value
#     print(name, age)

# # call function
# demo("Ben", 25)

# mark = []
# tot = 0
# print("Enter Number of Students: ")
# name = input()
# print("Enter the name of students " + str(name))
# for i in range(name):
#     mark.append(input())

# for i in range(name):
#     tot = tot + str(mark[i])

# # class Student:
# def getStudentDetails(self):
#         self.rollno=input("Enter Roll Number : ")
#         self.name = input("Enter Name : ")
#         self.physics =int(input("Enter Physics Marks : "))
#         self.chemistry = int(input("Enter Chemistry Marks : "))
#         self.maths = int(input("Enter Math Marks : "))

# def printResult(self):
#         self.percentage = (int)( (self.physics + self.chemistry + self.maths) / 300 * 100 ); 
#         print(self.rollno,self.name, self.percentage)
# getStudentDetails()
# printResult()
# print("Result : ")



# S1=Student()
# S1.getStudentDetails()

# print("Result : ")
# S1.printResult()

# S1.physics += 9

# print("result after adding grace marks...")
# S1.printResult()

# S2=Student()
# S2.getStudentDetails()

# print("Result : ")
# S2.printResult()

# S2.physics += 9

# print("result after adding grace marks...")
# S2.printResult()





# import collections, re
# n = int(input("Number of subjects: "))
# # item_order = collections.OrderedDict()
# for i in range(n):
#    sub_marks_list = input("Input Subject name : ")
#    subject_name = sub_marks_list[0]
#    item_price = int(sub_marks_list[1])
#    if subject_name not in item_order:
#        item_order[subject_name]=item_price
#    else:
#        item_order[subject_name]=item_order[subject_name]+item_price
           
# for i in item_order:
#    print(i+str(item_order[i]))





# mark = []
# tot = 0
# subjects = ["Physics", "Math", "English", "Computer"]
# student_name = input("Enter the name of student: ")
# students_num = input("Enter the number of students: ")
# subjects_num = input("Enter the number of students: ")
# print("The marks obtained in respective subjects:")
# for i in subjects:
#     mark.append(input())

# for i in subjects:
#     tot = tot + str(mark[i])
# for i in subjects:
#    sub_marks_list = input("Input Subject name : ")
#    subject_name = sub_marks_list[0]
# average= tot/4
#     # sub=int(input("Enter marks in : ", s))

#     # # to calculate average 
#     # average=(s)/5 
    
#     #comparing average to calculate grade 
# if average >= 90:
#         grade = 'A'
# elif average >= 80 and average < 90:
#         grade = 'B'
# elif average >= 70 and average < 80:
#         grade = 'C'
# elif average >= 60 and average < 70:
#         grade = 'D'
# else:
#         grade = 'E'
# print(student_name, grade)   

# marks_list = []
# subjects = ["English", "Math", "Science", "Social"]
# total_marks = 0
# student_name = input ("Enter the name of student: ")
# no_of_students = input( "Enter the number of students: ")
# no_of_subjects = input("Enter the number of subjects: ")
# print("The marks obtained in respective subjects: ")
# for i in subjects:
#      marks_list.append(input())
# for i in subjects:
#      total_marks = total_marks + int(marks_list[0])
# average = total_marks/3
# print("Average Marks:", total_marks/3 )
# if average >= 90:
#       print ("Hello! \n ",student_name ,"Your grade is A+")     
# elif average >= 80 and average < 90:
#      print ("Hello! \n ",student_name ,"Your grade is A")
# elif average >= 70 and average < 80:
#       print ("Hello! \n ",student_name ,"Your grade is B+")
# elif average >= 60 and average < 70:
#      print("Hello! \n ",student_name ,"Your grade is B")
# elif average >= 50 and average < 60:
#      print("Hello! \n ",student_name ,"Your grade is C+")
# elif average >= 40 and average < 50:
#      print("Hello! \n ",student_name ,"Your grade is C")
    
# elif average >= 25 and average < 40:
#       print("Hello! \n ",student_name ,"Your grade is D")
# elif average >= 1 and average < 25:
#      print("Hello! \n ",student_name ,"Your grade is E")
# else:
#      print("Invalid")  
#      while True:
#        if input("Would you like to continue? [yes/no]") != "y":
#          break

# class Student:
#    def __init__(self,name,subject):
#       self.name = name
#       self.subject = subject
# #    subject=0
# #    marks=0
# #    sum = 0

#       s1 = ("Samee", )
 
 
# total=subject_no*100

# for i in range(subject_no):
#     sub=input("Enter subject:")
#     subject.append(sub)

#     # mark=input("Enter marks: ")
#     # marks.append(mark)
    
    
# for j in range(subject_no):
#     mark=int(input("Enter marks in respective subjects: "))
#     marks.append(mark)
# try:
#     sum += mark
# except:
#     print("Error")
# average = (sum)/(subject_no)
# per = (sum/total)*100

# if average >= 90:
#     grade = 'A'
# elif average >= 80 and average < 90:
#     grade = 'B'
# elif average >= 70 and average < 80:
#     grade = 'C'
# elif average >= 60 and average < 70:
#     grade = 'D'
# else:
#     grade = 'E'
# print("Pecentage: ",per)
# print("Subjects: ", subject)
# print("Marks: ", marks)
# print (student_name,"your grade is ",grade)


class StudentReport:
    def __init__(self):
        self.__name = ""
        self.subjectName = ""
        self.subject = []
        self.__marks = []
        self.__total = 0
        self.__sum = 0
        self.__grade = ""
    
    def studentInfo(self):
        self.__name=input("Enter student name: ")
        self.__subject=input("Enter no of subject: ")
        
    def TotalMarks(self):
        
        # for i in (self.__subject):
        #     self.__total+= self.__subject*100
        # for j in range(self.__subject):
        #     self.__mark=int(input("Enter marks in respective subjects: "))
        #     self.__marks.append(self.__mark)
        #     self.__sum += self.__mark

    def Percentage(self):
        per = (self.__sum/self.__total)*100
        
    def Grade(self):
        if self.__per>=85:
            self.__grade="A+"
        elif self.__per>=75:
            self.__grade="A"
        elif self.__per>=65:
            self.__grade="B"
        elif self.__per>=55:
            self.__grade="C"
        elif self.__per>=50:
            self.__grade="D"
        else:
            self.__grade="F"

    def showStudentResult(self):
        self.studentInfo()
        self.TotalMarks()
        self.Percentage()
        self.Grade()
        print(self.__name,"\t\t",self.__total,"\t\t",self.__per,"\t\t",self.__grade)

def main():
    s=StudentReport()
    s.showStudentResult()

if __name__=="__main__":
    main()
