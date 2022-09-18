A = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
A1 = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
B = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
     "восемнадцать", "девятнадцать"]
C = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
D = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
D1 = ["тысяча", "тысячи", "тысяч"]


def number_to_words_converter(number: int):
    num1 = number // 1000
    num2 = (number // 100) % 10
    num3 = (number // 10) % 10
    num4 = number % 10
    print("Ваше число в текством виде: ", end='')
    if 0 < num1 < 10:  # Четёрыёхзначное число
        i = num1
        call1 = A1[i - 1]  # Вызывает из массива нужное название
        if i == 1:  # Функция определяет какое необходимо название
            call1 = call1 + " " + D1[0]
        elif 2 <= i <= 4:
            call1 = call1 + " " + D1[1]
        else:
            call1 = call1 + " " + D1[2]
    elif 10 <= num1 <= 100:
        i1 = num1 // 10
        i2 = num1 % 10
        call1 = C[i1 - 1] + " " + A1[i2 - 1]  # Вызывает из массива нужное название

        if i2 == 1:  # Функция определяет какое необходимо название
            call1 = call1 + " " + D1[0]
        elif 2 <= i2 <= 4:
            call1 = call1 + " " + D1[1]
        else:
            call1 = call1 + " " + D1[2]

    elif 100 <= num1 < 1000:
        i1 = num1 // 100
        i2 = (num1 % 100) // 10
        i3 = (num1 % 10) % 10
        call1 = D[i1 - 1] + " " + C[i2 - 1] + " " + A1[i3 - 1]  # Вызывает из массива нужное название

        if i3 == 1:  # Функция определяет какое необходимо название
            call1 = call1 + " " + D1[0]
        elif 2 <= i2 <= 4:
            call1 = call1 + " " + D1[1]
        else:
            call1 = call1 + " " + D1[2]
    else:
        call1 = ""
    if num2 != 0:  # Здесь и дальше такие же циклы, как и впервом примере
        i = num2
        call2 = D[i - 1]
    else:
        call2 = ""
    if num3 == 0:
        i = num4
        if num4 == 0:
            call5 = "рублей"
            print(call1, call2, call5)
        else:
            call3 = A[i - 1]
            if 5 <= i <= 9:
                call5 = "рублей"
            elif 2 <= i <= 4:
                call5 = "рубля"
            else:
                call5 = "рубль"
            print(call1, call2, call3, call5)
    elif num3 == 1:
        i = num4
        call3 = B[i - 1]
        print(call1, call2, call3, "рублей")
    else:
        i = num3
        call3 = C[i - 1]
        i = num4
        call4 = A[i - 1]
        if 5 <= i <= 9:
            call5 = "рублей"
        elif 2 <= i <= 4:
            call5 = "рубля"
        else:
            call5 = "рубль"
        print(call1, call2, call3, call4, call5)
    if (num4 != 0) and (num1 == 0) and (num2 == 0) and (num3 == 0):  # Если целая тысяча
        i = num4
        call4 = A[i - 1]
        Z = [5, 6, 7, 8, 9]
        Z1 = [2, 3, 4]
        if num4 == Z:
            call5 = "рублей"
        elif num4 == Z1:
            call5 = "рубля"
        else:
            call5 = "рубль"
        print(call4, call5)


numbs = [128, 1003, 256501]
print("Тестирование")
for numb in numbs:
    print("Число: " + str(numb))
    number_to_words_converter(numb)

num = input("Введите число: ")  # Ввод строки, а не числа для проверки входных данных

if num.isnumeric():
    number_to_words_converter(int(num))
else:
    print("Ошибка! Введены символы или буквы.")
