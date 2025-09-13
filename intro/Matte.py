
def add(x, y):
    return x+y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def subtrakt(x, y):
    return x-y

print("Du ska välja 2 nummer du skulle vilha använda. Sjriv det första nu.")
number = input()
number = int(number)

print ("Och nu väljer du andra")
number_2 = input()
number_2 = int(number_2)

print("Will du använda Addition, Multiplikation, Subtraktion eller Division?")

word = input()

if word == "Addition":
    result = add(number, number_2)
    print(result)

elif word == "Subtraktion":
    result = subtrakt(number, number_2) 
    print (result)

elif word == "Division":
    result = divide(number, number_2)
    print (result)

elif word == "Multiplikation":
    result = multiply(number, number_2)
    print(result)