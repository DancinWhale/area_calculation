import math

class Circle:  # Класс для круга
    def __init__(self):
        self.radius = 0

    def area(self, radius):
        self.radius = radius
        return "Area of your circle: " + str(round((math.pi * self.radius ** 2), 3))


class Triangle:  # Класс треугольника
    def __init__(self):
        self.r_1 = 0
        self.r_2 = 0
        self.r_3 = 0
        self.flag = 0

    def area(self, r_1, r_2, r_3):
        self.r_1, self.r_2, self.r_3 = r_1, r_2, r_3
        p = (self.r_1 + self.r_2 + self.r_3) / 2
        if r_3 ** 2 == r_1**2 + r_2**2:
            return "Area of your right triangle: " + str(
                round(math.sqrt(p * (p - self.r_1) * (p - self.r_2) * (p - self.r_3)), 3))
        else:
            return "Area of your triangle: " + str(
                round(math.sqrt(p * (p - self.r_1) * (p - self.r_2) * (p - self.r_3)), 3))


def area(x=""):
    try:
        figure = list(map(float, x.split()))
        if len(list(filter(lambda x: x <= 0, figure))) > 0:
            return "Incorrect Input. Enter the correct number or numbers."
    except:
        return "Incorrect Input. Please input only numbers."
    match len(figure):
        case 1:
            user_figure = Circle()
            return user_figure.area(figure[0])
        case 3:
            figure = sorted(figure)
            if figure[0] < figure[1] + figure[2] and figure[1] < figure[0] + figure[2] and figure[2] < figure[1] + figure[0]:
                user_figure = Triangle()
                return user_figure.area(figure[0], figure[1], figure[2])
            else:
                return "Incorrect Input."
        case _:
            return "Incorrect Input."
