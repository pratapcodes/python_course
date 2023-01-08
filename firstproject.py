#nested if
# num= 10
#  if num> 5:
#     print("Bigger than 5")
#  if num<=15:
#     print("Between 5 and 15")


#if elif
# letter="A"
# if letter=="B":
#     print("letter isB")
# elif letter=="C":
#     print("letter is c")
# elif letter=="A":
#       print("letter is A")
# else:
#       print("letter isn't A,B or C")



#nested loop
# for i in range(1,5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

"""Write a python which accepts the user's """

# firstname=input("enter first name:")
# lastname=input("enter last name:")
# print("Hello"+" "+ lastname+ " "+ firstname)

""" nested loops"""
# for i in range(1,5):
#     for j in range(i):
#         print(i,end=' ')
#     print()



#"""Write a programa to iterate the first 10 items and in each iterations print the sum of the current ans previous number """
# print ("printing current and previous number and their sum in a range(10)")
# previous_num=0
# #loop from 1 to 11
# for i in range(1,11):
#     x_sum=previous_num +i
#     print("current number",i ,"previous number",previous_num,"sum: ",x_sum)
#     previous_num = i


# def greetings():
#     print('Hello World!')
# greetings()
# print("printing outside of a function")

""" #function with two arguments
def add_numbers (num1,num2):
    sum=num1+num2
    print('sum:',sum)
add_numbers(2,4) """


""" function definition
def find_square(a):
    return a*a
square= find_square(10)
print(square)    """
    

""" #function definition
def get_square(num):
    return num*num
for i in[1,2,3]:
    #function call
    result=get_square (i)
print ('square of',i,'=',result) """



"""#program to find sum of multiple numbers
def find_sum(*numbers):
    result=0
    for num in numbers:
        result= result+num
        print("sum=",result)
    #function call with 3 arguments
find_sum(1,2,3)

    #function call with 2 arguments
find_sum(4,9)    """

"""def my_function(*fruits):
        print("The selected fruit is "+fruits[0])
my_function("apple","mango","orange")  """


"""def intro(**data):
    print("\n Data type of argument:",type (data))
    for key,value in data.items():
        print("\n{} is {}".format(key,value))
        
intro(Firstname="Prakash",Lastname="Thedi",Age=22, Phone=9847073556)

intro(Firstname="James",Lastname="Bond",Email="lunaticpratap@gmail.com",country="egg planet",Age=24, Phone=9864261692)   """





