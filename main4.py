class student:
    def __init__(self,name="",age=0,gender="",city="",password=0):
        self.name=name
        self.age=age
        self.gender=gender
        self.city=city
        self.password=password
    def __str__(self):
        print("hello world")
        return f' hello my name is {self.name} and my age is {self.age} and my gender is {self.gender} and im living in {self.city}'
    def talk (self):
        return f' hello my name is {self.name}'
    def addCourse(self,Newcourse):
        return f'hello : {self.name} that have id number: {self.id} and you have add a {self.Newcourse}'
students=[]
while True:
    print("1__login") 
    print("2__register")
    print("3__exit")
    userchoice=int(input("enter your choice"))
    if userchoice==1:
        print("welcome to your login page ")
        while True:
            username=input("enter your name")
            password1=input("enter your password")
            for student in students:
                if student.name==username and student.password==password1:
                    
                    print("you have add your informations succsessfully")
                    print(student)
                    break
                else:
                    print("wrong password")
    elif userchoice==2:
        name=input("enter name")
        age=input("enter your age")
        gender=input("enter your gender")
        city=input("enter your city")
        password=input("enter your password")
        student1=student(name,age,gender,city,password)
        students.append(student)
        print(students)
    elif userchoice==3:
        break
        

        

    
          
     