def is_year_leap(number):
    if number % 4 == 0:
        return True
    else:
        return False


num = int(input("Введите число: "))
result = is_year_leap(num)
print(f"Делится ли на четыре {num}? - {result}")