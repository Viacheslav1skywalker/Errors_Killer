import os

# Проверяем, существует ли файл
if os.path.exists("несуществующий_файл.txt"):
    with open("несуществующий_файл.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print("Файл не существует")

def outer_function():
    global x
    x = 10

    def inner_function():
        global x
        x += 5
        print(f"Внутри внутренней функции: {x}")

    inner_function()
    print(f"Внутри внешней функции: {x}")

    return x

x = outer_function()
