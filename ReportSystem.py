student_name=str(input("Enter your name: "))
subject=[]
marks=[]
sum = 0
try:
 subject_no=int(input("Enter no of subject: "))
except:
 print("error")
 
total=subject_no*100

for i in range(subject_no):
    sub=input("Enter subject:")
    subject.append(sub)

    # mark=input("Enter marks: ")
    # marks.append(mark)
    
    
for j in range(subject_no):
    mark=int(input("Enter marks in respective subjects: "))
    marks.append(mark)
try:
    sum += mark
except:
    print("Error")
average = (sum)/(subject_no)
per = (sum/total)*100

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
print("Pecentage: ",per)
print("Subjects: ", subject)
print("Marks: ", marks)
print (student_name,"your grade is ",grade)
