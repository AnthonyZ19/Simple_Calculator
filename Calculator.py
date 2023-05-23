symbols = ["/", "*", "+", "-"]
values = []
result = []
def addition(x,y):
    answer = int(x)+int(y)
    result.append(answer)
def subtraction(x,y):
    answer = int(x)-int(y)
    result.append(answer)
def multiplication(x,y):
    answer = int(x)*int(y)
    result.append(answer)
def division(x,y):
    try:
        answer = int(x)/int(y)
        result.append(answer)
    except ZeroDivisionError:
        print("Error")
letter = [ "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"]

def Program():
    print("use /,*,+ and - anything else will result in error")
    symbol = input("Operation/Operator: ")
    
    if symbol not in symbols:
        print("Use a valid/accepted operation, next time")
        quit()
        
    Firstnum = input("First number: ")
    Secondnum = input("Second number: ")
  
    try:
        values.append(int(Firstnum))
    except:
        print("Enter a number next time")
        quit()
    try:
        values.append(int(Secondnum))
    except:
        print("Enter a number next time")
        quit()
  
    problem = Firstnum + " " + symbol + " " + Secondnum
    print(problem)
    
    if symbol == "+":
        addition(values[0], values[1])
    elif symbol == "-":
        subtraction(values[0], values[1])
    elif symbol == "*":
        multiplication(values[0], values[1])
    elif symbol == "/":
        division(values[0], values[1])
    
    if result != []:
        print("Answer = " + str(result))
        print("Type 'yes' to go again or 'no' to quit")
        continuation = input()
        
        if continuation.lower() == "yes":
            Program()
        elif continuation.lower() == "no":
            quit()

print("This is a simple calculator")
print("Can only work with single digit numbers")

Program()
