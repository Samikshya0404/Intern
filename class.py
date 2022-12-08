class StudentReport:
    def __init__(self):
        self.__name=""
        self.__marks=[]
        self.__total=0
        self.__per=0
        self.__grade=""
        self.__subjectNo=[]
        self.__subjectName=[]

    def studentInfo(self):
        self.__name=input("Enter student name: ")
        self.__subjectNo=int(input("Enter the number of subject: "))
        # self.__subjectName=input("Enter the name of subejct:")
        # print("Enter marks of five subjects: ")
        for j in range(self.__subjectNo):
           self.__subjectName.append(input("Enter subject:"))

        for i in range(self.__subjectNo):
            self.__marks.append(int(input("Subject "+str(i+1)+": ")))
        
			
    def calTotal(self):
        for i in self.__marks:
            self.__total+=i
			
    def calPercentage(self):
        self.__per=self.__total/self.__subjectNo
		
    def calGrade(self):
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
			
    def showStudent(self):
        self.studentInfo()
        self.calTotal()
        self.calPercentage()
        self.calGrade()
        print(self.__name,"\t\t",self.__total,"\t\t",self.__per,"\t\t",self.__grade,"\t\t")


def main():
    s=StudentReport()
    s.showStudent()

if __name__=="__main__":
    main()