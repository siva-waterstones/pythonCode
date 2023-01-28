# # String Functions
# 1. Concat
# 2. Split
# 3. slice
# 4. Replace
# 5. Uppercase
# 6. Lowercase
# 7. IndexOf
# 8. Modify
# 9. Format* XX
# 10.Join XX

str1="ABC"
str2="DEF"
str3="Hello, My name is Siva, I am 43 years old"

print(str1+str2)
print(str3.split(",",-1))
print(str3[2:6])
print(str3.replace("Siva","SivaAnanth"))
print(str3.upper())
print(str3.lower())
print(str3.index("Siva"))

str4="My Name is {fname}, age is {fage:.2f}".format(fname="Siva",fage=43)
print(str4)


