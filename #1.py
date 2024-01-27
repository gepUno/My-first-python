class Student:
    def __init__(self,name,age,studID):
        self.name = name
        self.age = age
        self.studID = studID
        print('Student Created')
        
    # def introduce(self):
    #     print(f"Hi i'm {self.name} and my age is {self.age}.")
        
    def information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"StudentID: {self.studID}")
        
        
 
name = input('Enter name: ').title().strip()
age = int(input('Enter age: '))
studID = int(input('Enter Student ID: '))

 
 
stud = Student(name,age,studID)
stud.information()




# studOne = Student('Gepulla',20,1554)
# studOne.introduce()
# studOne.information()

    
    
