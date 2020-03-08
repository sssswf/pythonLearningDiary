class Student():
    school = "MIT"#属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):#方法
        print("Hi")
        return  None
tom = Student("tom",20)
print(tom.school)
