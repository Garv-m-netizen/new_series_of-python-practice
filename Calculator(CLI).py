def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error: division by zero is not possible till now"
    return x/y
print("=== Simple Calculator ===")
print("Choose Operation")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. Division(-)")

op = input("Enter the operation you want to perform (+,-,*,/): ")
a = float(input("Enter the First number: "))
b = float(input("Enter the Second number: "))

if op=='+':
    result=add(a,b)
elif op =='-':
    result=sub(a,b)
elif op=='*':
    result=mul(a,b)
else:
    result=div(a,b)

print("Result: ",result)