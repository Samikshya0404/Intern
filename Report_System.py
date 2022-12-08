# author: Samikshya Ghimire gsamikshy0@gmail.com

# n=int(input("Enter the number of students: ")) 
# sub=int(input("enter no of subject "))
# sum = 0.0
# sub_list = ["Chemistry", "Physics", "Maths","Computer","English"] 

# for i in range(n):
#     roll_no=int(input("Enter roll no: ")) 
#     name=input("Enter name: ") 
#     for i in range(len(sub_list)): 
#         try:
#             sub1=int(input(f"Enter marks in {sub_list[i]}: "))
#         except:
#             print("Invalid number")
#             sum += sub1
#     # to calculate average 
#     average=(sum)/len(sub_list)

#     #comparing average to calculate grade 
#     if average >= 90:
#         grade = 'A'
#     elif average >= 80 and average < 90:
#         grade = 'B'
#     elif average >= 70 and average < 80:
#         grade = 'C'
#     elif average >= 60 and average < 70:
#         grade = 'D'
#     else:
#         grade = 'E'

#     print ("Roll.no:", roll_no)
#     print ("Name:",name)
#     print ("Grade:", grade)

student_name=str(input("Enter your name: "))
subject=[]
marks=[]
sum = 0
sub_no=int(input("Enter no of subject: "))
# for i in range(sub_no):
#     sub=input("Enter subject:")
#     subject.append(sub)
for i in range(sub_no): 
        sub=input("Enter subject:")
        # subject.append(sub)
        for i in range(len(sub)): 
                sub1=int(input("Enter marks in respective subjects: "))
                marks.append(sub1)
                sum += sub1

        average = (sum)/(sub_no)

        if average >= 90:
                grade = 'A'
        elif average >= 80 and average < 90:
                grade = 'B'
        elif average >= 70 and average < 80:
                grade = 'C'
        elif average >= 60 and average < 70:
                grade = 'D'
        else:
                grade = 'E'

print("Subjects: ", subject)
print("Marks: ", marks)
print (student_name,"your grade is ",grade)
        