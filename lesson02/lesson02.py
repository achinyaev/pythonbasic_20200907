"""
Занятие 02. Типы в питоне

"""
var_str = "Это строка" # неизменяемый тип коллекция итерируемый
var_int = 22 #itn не изменяемый тип
var_list = [1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO'] #список изменяемая коллекция итерируемая
var_tuple = (1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO') #кортеж неизменяемая коллекция итерируемая

# inf   a = float('inf')    бесконечность
# nan   a = float('nan')    нечто
var_float = 2.33 #float не изменяемое


var_set = {1, 2, 3, 4, 5, 1, 2, 3, (1, 2, 3)} # set множество изменяемый тип, но неможет содержать изменяемые типы (например список)

var_dict = {'key': 'HELLO', 1:22, (1,2):33} # словарь изменяемый тип итерируемый

# i=0
# while i < len(var_str):
#     print(var_str[i])
#     i+=1

# for ch in var_str:
#     print(ch)
#
# for key,value in var_dict.items():
#     print(key,value)

# user_template = {
#     'age': 'Ввдеите возраст',
#     'name':'Введите имя',
#     'surname':'Введите фавмилию'
# }
#
# user = {}
# for key, ask in user_template.items():
#     user[key] = input(ask+'\n')
#
# print(user)

# for idx, ch in enumerate(var_str,10):
#      print(idx, ch)
#
# for num in range(-10,10,1):
#     print(num)
temp=[]
for idx, num in enumerate(range(-10,10,1),77):
    temp[idx] = num