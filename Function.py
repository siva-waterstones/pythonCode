# def ab(userName,userAge,z):
#     user_details={'Name':userName,'Age':userAge,'Sex':z}
#     for x in user_details.values():
#         # print(user_details.values())
#         # print(user_details.keys())
#         return (user_details.values())
#
# userName=input("Please enter User Name ")
# userAge=int(input("Enter Age "))
# z1=ab(userName,userAge,"Male")
# print(z1)

'''# Oops
# 1. Class and Objects
# 2. Inheritance (Single, Multilevel and Multiple)
# 3. Polymorphism (Method Overriding)
# 4. Encapsulation (get, set)
# 5. Abstraction

Class and Objects
-----------------'''

class addition:
    z=20
    def add(self):
        a=10
        x=self.z+a
    def sub(self,x,y):
        ab=x-y
        return ab

obj=addition()
obj.add()
x = obj.sub(10,5)
print(x)

print("Calling from Function", obj.z)

#2. Inheritance (Single, Multilevel and Multiple)

class addition:
    z=20
    def add(self):
        a=10
        x=self.z+a
        print(x)

class subtraction(addition):
    def sub(self):
        a=10
        x=self.z-a
        print(x)
class division(subtraction):
    def div(self):
        e=100
        d=e/self.z
        print(d)

obj1=division()
obj1.sub()
obj1.add()
obj1.div()

# Multiple
class addition:
    z=20
    def add(self):
        a=10
        x=self.z+a
        print(x)

class subtraction():
    y=30
    def sub(self):
        a=10
        x=self.y-a
        print(x)
class division(addition,subtraction):
    def div(self):
        d=self.y/self.z
        print(d)

obj1=division()
obj1.sub()
obj1.add()
obj1.div()

# 3. Polymorphism (Method Overriding)
class addition:
    z=20
    def add(self):
        a=10
        x=self.z+a
        print(x)

class subtraction(addition):
    y=30
    def add(self):
        a=10
        x=self.y-a
        print(x)

obj=subtraction()
obj.add()

# 4. Encapsulation (get, set)

class division():
    __z=100 #Encapsulating the variable
    def get(self):
        e=100
        d=e/self.__z
        return d
    def set(self,y):
        self.__z=y
        print(self.__z)

obj2=division()
print(obj2.get())
obj2.set(200)

# 5. Abstraction
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def add(self):
        pass

class B(A):
    def add(self):
        print("hi")

obj3=B()
obj3.add()



