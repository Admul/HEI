numbers_list = input("Введите числа через запятую: ").replace(" ", "").split(",")
numbers_tuple = tuple(numbers_list)
print(f"Список: {numbers_list}")
print(f"Кортеж: {numbers_tuple}")