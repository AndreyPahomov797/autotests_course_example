# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
class PersonInfo:  # Задаю класс, есть фамилия и имя, возраст и неизвестное количесвто подразделений, где работает сотр.
    def __init__(self, FI, age, *department):
        self.FI = FI
        self.age = age
        self.department = department

    def short_name(self):  # Тут метод берет атрибут Фамилия и имя, разделяет строку по пробелу, выводит фамилию и
        # первую букву имени
        a = self.FI.split(" ")
        a1 = a[0]
        return f'{a[1]} {a1[:1]}.'

    def path_deps(self): # Метод берет элементы кортежа атрибута, где работает сотр. и складывает их в строку через
        #  стрелку. После не отображает последние 5 элементов строки (чтобы не показывать последнюю стрелку)
        c = ''
        b = self.department
        for i in range(len(b)):
            c = c + str(b[i]) + ' --> '
        return c[:-5]
    def new_salary(self):
        n = []
        st = ''
        for j in range(len(self.department)):  # Превращаю кортеж в строку без пробелов
            st = st + self.department[j]
        letters_dict = {}
        for i in range(len(st)):  # Пробегает по всему слову по буквам
            summ = 0
            for k in range(len(st)):  # Пробегает по всему слову и считает сколько повторяется i-ый символ слова
                if st[k] == st[i]:
                    summ = summ + 1
                letters_dict.update({st[i]: summ})  # Добавляет в пустой словарь тождественно равный
        n = []
        x = letters_dict.values()  # Вывожу значения ключей словаря в виде списка
        s = sorted(x)  # Сортирую в порядке возрастания
        multi = (s[-1]+s[-2]+s[-3])*1337*self.age
        return multi


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')