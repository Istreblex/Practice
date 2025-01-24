import math
from file1 import f1
from file2 import f2
from file3 import f3

if __name__ == '__main__':
    start = -3.4
    end = 3.4
    step = 0.33

    print("Табулирование функции f3(x) = 5^(x-1) + tg((x+3)^2) на [-3.4; 3.4] с шагом 0.33:")
    x = start
    while x <= end:
        try:
            result = round(f3(x), 4)
            print(f"x = {round(x, 2):>5}, f3(x) = {result}")
        except ValueError:
            print(f"x = {round(x, 2):>5}, f3(x) не определена")
        x += step

    print("Табулирование f2(x) = ln(x+1) + √3*x на [-3.4; 3.4] с шагом 0.33:")
    x = start
    while x <= end:
        if x + 1 <= 0:
            print(f"x = {round(x, 2):>5}, f2(x) не определена (x+1 ≤ 0)")
        else:
            result = round(f2(x), 4)
            print(f"x = {round(x, 2):>5}, f2(x) = {result}")
        x += step

    print("Табулирование f1(x) = sqrt(sin²x + cos⁴x) на [-3.4; 3.4] с шагом 0.33:")
    x = start
    while x <= end:
        try:
            result = round(f1(x), 4)
            print(f"x = {round(x, 2):>5}, f1(x) = {result}")
        except ValueError:
            print(f"x = {round(x, 2):>5}, f1(x) не определена (подкоренное выражение < 0)")
        x += step
