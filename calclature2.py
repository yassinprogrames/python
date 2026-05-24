def add(a,b):
    return(a + b)
def subt(a,b):
    return(a-b)
def multi(a,b):
    return(a*b)
def div(a,b):
    if b == 0:
        return("cant div by 0")
    else:
        return(a/b)
def power(a,b):
    return(a**b)
def remainder(a,b):
    return(a%b)
def calclature(a,b,op):
        
        if op=="+":
            return(add(a,b))
        elif op=="-":
            return(subt(a,b))
        elif op=="*":
            return(multi(a,b))
        elif op=="/":
            return(div(a,b))
        elif op == "p":
            return(power(a,b))
        elif op =="%":
            return(remainder(a,b))
while (True):
    result = calclature(int(input("what is the first num")),int(input("what is the second num")),
input("what si the op (+,-,*,p,%)"))
    print(result)      
    again= input("do you want to start again: ")

    if  again.lower() == "no":
        break    