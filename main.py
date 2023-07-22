import testing code
number = input("scrivi \n")
print("hai scritto: \n" + number)


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def areaclc(self):

        area = self.radius * self.radius * 3.14
        return(area)


circle1 = Circle(int(number))
print(circle1.areaclc())





