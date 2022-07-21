
x = int(input("Enter an interger: "))
ans = 0

while ans**3 < abs(x):
    ans += 1

if ans**3 != abs(x):
    print(f"{x}, is not perfect cube")
else:
    if x < 0:
        ans = -ans
    print(f"perfect cube is {ans}")
    


