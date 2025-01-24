import math

def f3(x):
    return 5**(x - 1) + math.tan((x + 3)**2)


start = -3.4
end = 3.4
step = 0.33

print("Табулирование функции f3(x) = 5^(x-1) + tg((x+3)^2) на [-3.4; 3.4] с шагом 0.33:")
x = start
while x <= end:
    try:
        result = round(f3(x), 4)
        print(f"x = {round(x, 2):>5}, f3(x) = {result}")
    except:
        print(f"x = {round(x, 2):>5}, f3(x) не определена")
    x += step