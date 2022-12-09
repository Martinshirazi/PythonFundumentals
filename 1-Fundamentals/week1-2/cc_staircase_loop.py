#here is  an example of lambda function as call_back function:
#this higher_order function has aparmeter of a callback funtion
def a_function(callback):
    print(callback(3))

#This calls the higher_order function with a lambda function argument
a_function(lambda num : num ** 2) #this would print 9


def reverse(str):
   return str[::-1]
   

name = input("What is your name? ")
reverse(name)
print("Your name reversed is:", reverse(name))
