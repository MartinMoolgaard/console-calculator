a = input("Write a number: ")
b = input("Write another number: ")
c = a+b
print(c)


c="13"
d=input("type 37 and press [enter]:")
e=37

cc=int(c)
dd=int(d)

print(c+d)
print(cc+dd)
print(cc+e)
print(c+e)

print(type(c))
print(type(d))
print(type(e))
print(type(cc))


# A simple calculator made as an introduction to programming

in1 = input("Write a number: ")
in2 = input("Write another number: ")
a = int(in1)
b = int(in2)
c = a+b
print(c)

# A simple calculator made as an introduction to programming
print("Calculate a + b:")
in1 = input("a=")
in2 = input("b=")
a = int(in1)
b = int(in2)
c = a+b
output = "{}+{}={}".format(a,b,c)
print(output)

# A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")
    a = int(in1)
    b = int(in2)
    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)


    # A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")
    break
    a = int(in1)
    b = int(in2)
    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)


    # A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")

    if in1 == "quit":
        break

    a = int(in1)
    b = int(in2)
    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)



    # A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")

    if in1 == "quit":
        break

    try:
        a = int(in1)
        b = int(in2)
    except ValueError: 
        print("Error: a or b was an invalid number")

    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)




    # A simple calculator made as an introduction to programming

while True:
    print("Calculate a + b:")
    in1 = input("a=")
    in2 = input("b=")

    if in1 == "quit":
        break

    try:
        a = int(in1)
        b = int(in2)
    except ValueError: 
        print("Error: a or b was an invalid number")
        continue

    c = a+b
    output = "{}+{}={}".format(a,b,c)
    print(output)
# Du er sku da smart mand















    
