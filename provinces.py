
list_provinces = []
counter = 0
with open ("provinces.txt", 'rt') as provinces_file:
    for prov in provinces_file:
        clean_line = prov.strip()
        list_provinces.append(clean_line)

list_provinces.pop(0)
list_provinces.pop(70)
print(list_provinces)
for joy in list_provinces:
    if joy == "Alberta":
        counter += 1
    elif joy == "AB":
        counter += 1

print(counter)


