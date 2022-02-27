#QUESTION1
print("Q-1")
def TowerOfHanoi(n , fromRod, toRod, middleRod):
	if n == 0:
		return
	TowerOfHanoi(n-1, fromRod, middleRod, toRod)
	print("Move disk",n,"from rod",fromRod,"to rod",toRod)
	TowerOfHanoi(n-1, middleRod, toRod, fromRod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")

#QUESTION2
print("Q-2")
from math import factorial, remainder
from tracemalloc import start
n=int(input("Enter the number of rows: "))

print("USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()
print("\n")

print("USING RECURSSIONS")

def pascal_triangle(n,original_length=n):
    if n == 0:
        return
    pascal_triangle(n-1,original_length)
    # spacing
    print('  '*(original_length-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #by Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")

#QUESTION 3
print("Q-3")
int1 =int(input("Enter first number: "))
int2=int(input("Enter second number: "))
Quotient = int1 // int2
Remainder = int1 % int2

#part (a)
print("(A) Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part (b)
print("(B)")
if (Quotient == 0):
    print("The quotient is zero")
if (Remainder == 0):
    print("The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("All the values are non zero")

#part (c)
c_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(c_list)):
    if c_list[i] > 4:
        result.append(c_list[i])
print(f"(C): Numbers that are greater than 4 are : {result}")

#part (d)
set_result = set(result)
print("(D): Set:",set_result)

#part (e)
#frozen Set is used to make the set immutable
immutable_Set = frozenset(set_result) 
print("(E): Immutable set:",immutable_Set)

#part (f)
print("(F): Hash value of the max value from the above set:", hash(max(immutable_Set)))
print("\n")

#QUESTION 4
print("Q-4")
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.roll=rollno
        print("Student details are here..")
    
    def StudentDetails(self):
        print(f"The name of the student is {self.name} and roll number is {self.roll}")

    def __del__(self):
        print("The object is destroyed")

name=input("Enter name: ")
roll_no=int(input(f"Enter roll no. of {name}: "))

details=Student(name,roll_no)
details.StudentDetails()
del details
print("\n")

#QUESTION 5
print("Q-5")
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def getInfo(self):
        print(f''' Name of the Employee: {self.name}
        Salary: {self.salary}''')

mehak=Employee("Mehak",40000)
ashok=Employee("Ashok",50000)
viren=Employee("Viren",60000)
mehak.getInfo()
ashok.getInfo()
viren.getInfo()

print("(a)")
print("****Updated salary of Mehak****")
mehak=Employee("Mehak",70000)
mehak.getInfo()
print("(b)")
print("The record of viren is deleted")
del viren
print("\n")
 
#QUESTION 6
print("Q-6")
#word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting the meaningful word with the exact same letters
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()

#defining the dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y or n): ")

    if ans == 'y':
        print("The friends pass the friendship test")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y or n")
        userinput()
userinput()