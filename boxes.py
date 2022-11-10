import math
items = int(input("Enter the number of items: "))
boxes = int(input("Enter the number of items per box: "))

num_boxes = math.ceil(items / boxes)

print(f"For {items} items, packing {boxes}"
    f" items in each box, you will need {num_boxes} boxes.")

n = 0
for i in range(1, 4):
    n = n + i
    
print(n)