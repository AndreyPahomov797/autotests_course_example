# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:  # Создаю класс, где каждый элемент это кортеж из двух элементов (координаты точки)
    def __init__(self, x1_y1, x2_y2):
        self.x1_y1 = x1_y1
        self.x2_y2 = x2_y2

    # Метод находит расстояние между точками, где оно является гипотенузой прямоугольного треугольника, round округляет до двух цифр после запятой
    def length(self):
        return round(((self.x2_y2[0]-self.x1_y1[0])**2+(self.x2_y2[1]-self.x1_y1[1])**2)**0.5, 2)

    # Метод определяет пересекает ли отрезок ось абцисс, методом сравнения координат "у" с нулем
    def x_axis_intersection(self):
        if self.x1_y1[1] > 0 > self.x2_y2[1]:
            otvet = True
        if self.x1_y1[1] < 0 < self.x2_y2[1]:
            otvet = True
        else:
            otvet = False
        return otvet

    # Тут сравнивает с нулем координату "x"
    def y_axis_intersection(self):
        if self.x1_y1[0] > 0 > self.x2_y2[0]:
            otvet = True
        if self.x1_y1[0] < 0 < self.x2_y2[0]:
            otvet = True
        else:
            otvet = False
        return otvet
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')