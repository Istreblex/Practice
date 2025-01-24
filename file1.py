import math

def f1(x):
    return math.sqrt(math.sin(x)**2 + math.cos(x)**4)

start = -3.4
end = 3.4
step = 0.33

print("Табулирование f1(x) = sqrt(sin²x + cos⁴x) на [-3.4; 3.4] с шагом 0.33:")
x = start
while x <= end:
    try:
        result = round(f1(x), 4)
        print(f"x = {round(x, 2):>5}, f1(x) = {result}")
    except ValueError:
        print(f"x = {round(x, 2):>5}, f1(x) не определена (подкоренное выражение < 0)")
    x += step