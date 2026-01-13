# print("Hello Python")
# name = input("Enter your name")
# age = int(input("Enter your age"))

# print("My name is", name, "and", "age is", age)

# # Make a sum with proper syntax
# a = int(input("Enter a value:  "))
# b = int(input("Enter a second value:  "))
# print(a+b)


# Check vote eligibility

# age = int(input("Enter your Age: "))

# if age<0:
#     print("Negative not allow")
# elif(age>=18):
#     print("You are eligible to Vote")
# else:
#     print("You are not eligible to vote")

# for i in range(5):
#     print(i)


# for i in range(1,5):
#     print(i)

# for i in range(1,10,1):
#     print(i)

# fruits = ['orange','apple','papaya']

# for data in fruits:
#     print(data)

# for index, data in enumerate(fruits):
#     print(index,data)

# count = 0

# while count<5:
#     print(count)
#     count += 1

# for n in range(5):
#     if n == 2:
#         continue
#     print(n)


# person = {"name": "Alex", "age": 30}

# for key, value in person.items():
#     print(key, value)


# for i in range(3):
#     for j in range(2):
#         print(i, j)


# # range() is a special generator object
# print(type(range(3)))  # <class 'range'>
# print(range(3))        # range(0, 3)

# # It's NOT a list
# print(isinstance(range(3), list))  # False

# range(1000000) doesn't create a million numbers in memory
# big_range = range(1000000)
# print(big_range)  # range(0, 1000000) - instant!

# If it were a list, this would use huge memory
# big_list = [0, 1, 2, 3, ..., 999999] ← This would be huge!


# squares = []

# for x in range(5):
#     squares.append(x * x)

# print(squares)

# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)


# try:
#     a = int(input("Enter number: "))
#     print(10 / a)
# except:
#     print("Something went wrong")

# Sum of a list
# a = [10,20,10,10]
# sum = 0
# for i in a:
#     sum = sum +i
# print(sum)


# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
 
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

