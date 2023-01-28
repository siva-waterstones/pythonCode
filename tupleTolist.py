#Tuple
A=(1,2,3,4,5)
print(A[1])

#Convert Tuple to a list
A1=list(A)
A1=(6,7,8,9,10)
print(A1[1])

#Convert list to a Tuple
A=tuple(A1)
print(A1[1])


user_details={'Name':'SivaAnanth','Age':43,'Sex':'Male','City':'Chennai','Country':'India'}
print(user_details['Name'])
print(user_details.values())
print(user_details.keys())
print(user_details.items())

for x in user_details.values():
    if x == "India":
        print('Your Location is India')
    else:
        print(user_details.values())

for x,y in user_details.items():
    print(x,y)

B1={1,2,3,"Siva","Ananth"}
X1=[1,2,1]

V1=set(X1)
print(V1)

# Functions
# 1. Define Function
# 2. Call Function
# 3. Parameter or Argument passing function
# 4. Return Function

def add(): #define function
    print(5+6)
add() #call function

def add1(x,y): #define function
    print(x+y)
add1(5,6) #call function + argument passing

def add2(x,y): #define function
    return x+y
z=add2(5,6) #call function + argument passing + return
print(z)









