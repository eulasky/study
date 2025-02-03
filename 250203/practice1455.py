# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height

        return area
    
    def calculate_perimeter(self):
        perimeter = (self.width + self.height) * 2
        
        return perimeter
    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.calculate_area()}')
        print(f'Perimeter: {self.calculate_perimeter()}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)
