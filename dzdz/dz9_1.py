# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open('test_file/task1_data.txt', 'r', encoding='utf-8') as f:  # Открываем файл для чтения
    string = f.read()  # Присвваем переменной содержание файла в виде строки
    new_string = ''
    for i in string:
        if i.isdigit() == False:  # Если элемент строки не цифра, то в новую строку new_string добавляем этот элемент
            new_string = new_string + i
with open('test_file/task1_data.txt', 'w', encoding='utf-8') as f:  # Открываем для записи файл или создаем, если такого нет
    f.write(new_string)  # Записываем туда строку без цифр
    f.close()  # Закрываем файл
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')