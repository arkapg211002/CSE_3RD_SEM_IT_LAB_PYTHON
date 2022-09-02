'''
Write a python Program to create grade calculator, creating a dictionary which consists of the student name, assignment result test results and their respective lab results.

Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.

10 % of marks scored from submission of Assignments

70 % of marks scored from Test

20 % of marks scored in Lab-Works

                Grade will be calculated according to :

score >= 90 : "A"

score >= 80 : "B"

score >= 70 : "C"

score >= 60 : "D"

 

Example input:

james = { "name":"James Potter",

          "assignment" : [82, 56, 44, 30],

          "test" : [80, 80],

          "lab" : [67.90, 78.72]

        }

Example output:

Average marks of James Potter is : 75.962

Letter Grade of James Potter is : C
'''
n=int(input("Enter the number of students: "))
for i in range(n):
        name=input("Enter the name of the student: ")
        assignment=[]
        test=[]
        lab=[]
        for j in range(4):
                assignment.append(int(input("Enter the assignment marks: ")))
        for j in range(2):
                test.append(int(input("Enter the test marks: ")))
        for j in range(2):
                lab.append(float(input("Enter the lab marks: ")))
        d={}
        d["name"]=name
        d["assignment"]=assignment
        d["test"]=test
        d["lab"]=lab
        print("The dictionary is: ",d)
        avg=(sum(assignment)/4*0.1)+(sum(test)/2*0.7)+(sum(lab)/2*0.2)
        print("The average marks of ",name," is: ",avg)
        if(avg>=90):
                print("The letter grade of ",name," is: A")
        elif(avg>=80):
                print("The letter grade of ",name," is: B")
        elif(avg>=70):

                print("The letter grade of ",name," is: C")
        else:
                print("The letter grade of ",name," is: D")
        print("\n")

