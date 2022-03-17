"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл
"""

trans_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

file_in = 'task04.txt'
file_out = 'task04_out.txt'

if __name__ == '__main__':
    v_block = ''
    with open(file_in, "r" ,encoding="UTF-8") as file:
        for line in file:
            v_block += trans_dict[line.split()[0]] + ' ' + ' '.join(map(str, line.split(' ')[1:]))

    with open(file_out,'w', encoding="UTF-8") as file:
        file.write(v_block)

    print(f'Transformation file: \"{file_in}\" finished. You can view the result in the file : \"{file_out}\"')