# PEP 8
some_str = "Hello my friends" # Одинаково воспринимается интерпретатором  # str()
some_str2 = 'Hello world' # Одинаково воспринимается интерпретатором

some_int = 7    #  int()
some_float = 3.14 # float ()
some_bool = True # bool()

#snake_case = 1
#CamelCase = 2
#camelCase = 3 # bad
# kebab-case = 2   not support

ask_name = "Введите имя:\n"
ask_age = "Введите возраст:\n"
#name = input(ask_name)
#print("Привет", name, end="@@@@", sep="----")
#age = input(ask_age)
#if age.isdigit():
#    age = int(age)
#    if  age >= 18:
#        print('Полный доступ разрешен')
#    elif age > 16:
#        print('Доступ к боевикам разрешен')
#    else:
#        print('Смотри мультики')
#else:
#    print("Введено не число")
#    print('Повторите ввод')

a = 9212312
temp = a
while tmp := temp % 10 :
#    tmp = temp % 10
    temp //= 10
    if tmp == 5:
        break
    print(tmp,temp)
else:
    print("ELSE")

print("THE END")


