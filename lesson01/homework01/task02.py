"""
Задание №2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
#86400 секунд в сутках

tmp = False     # Временная переменная, флаг выхода из цикла
while tmp != True:  # Цикл проверки корректности ввода
    time_sec = input("Введите время в секундах ")
    if not time_sec.isdigit():
        print("Вы ввели не правильное время в секундах, повторите ввод")
        tmp = False
    else:
        tmp = True
        print("Спасибо за правильный ввод.\n")

time_sec = int(time_sec)    #Преобразование строки в целое число
tmp = False

if time_sec > 86400:    #Проверка если введено больше секунд чем 1-их сутках
    print("Вы ввели лишних секунд = %d," % (time_sec - time_sec % 86400), "что равняется", time_sec // 86400,"суткам.\n")
    time_sec = time_sec % 86400
    print("Расчитаем время для оставшихся =", time_sec ,"секунд")

time_h = time_sec // 3600   #Вычисляем кол-во часов
time_m = (time_sec % 3600) // 60    #Вычисляем кол-во минут
time_s = time_sec - time_h * 3600 - time_m * 60     #Вычисляем кол-во секунд

print("Время в формате hh:mm:ss- %02d:%02d:%02d" % (time_h, time_m, time_s))





