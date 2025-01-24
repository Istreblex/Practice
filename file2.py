import math

def f2(x):
    return math.log(x + 1) + math.sqrt(3) * x

start = -3.4
end = 3.4
step = 0.33

print("Табулирование f2(x) = ln(x+1) + √3*x на [-3.4; 3.4] с шагом 0.33:")
x = start
while x <= end:
    if x + 1 <= 0:
        print(f"x = {round(x, 2):>5}, f2(x) не определена (x+1 ≤ 0)")
    else:
        result = round(f2(x), 4)
        print(f"x = {round(x, 2):>5}, f2(x) = {result}")
    x += step