# Open Closed Principle
# Open for extension, closed for modification

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1 
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size


# Breaks Open-Closed Principle
class ProductFilter:
    def filter_by_color(self,products,color):
        for p in products:
            if p.color == color: yield p
    
    def filter_by_size(self,products,size):
        for p in products:
            if p.size == size: yield p

# Specification (Enterprise Pattern)

class Specification:
    def is_satisfied(self,item):
        pass

    def __and__(self,other):
        return AndSpecification(self,other)
    

class Filter:
    def filter(self,items,spec):
        pass

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self,size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(lambda spec:spec.is_satisfied(item),self.args))



apple = Product("apple",Color.GREEN,Size.SMALL)
tree = Product("tree",Color.GREEN,Size.LARGE)
house = Product("hose",Color.BLUE,Size.LARGE)

products = [apple,tree,house]

bf = BetterFilter()
print("Green Products:")
green_spc = ColorSpecification(Color.GREEN)

for p in bf.filter(products,green_spc):
    print(f' - {p.name} is green')
        
print("Large Products:")
large_spc = SizeSpecification(Size.LARGE)

for p in bf.filter(products,large_spc):
    print(f' - {p.name} is large')

print("Large and Green Products:")

large_and_green_spc = AndSpecification(large_spc,green_spc)
large_and_green_spc = large_spc & green_spc
for p in bf.filter(products,large_and_green_spc):
    print(f' - {p.name} is large and green')



