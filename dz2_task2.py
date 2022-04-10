my_list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list:int = len(my_list1)
store_id = id(my_list1)
print((f"id before {store_id}"))
for _ in range(length_of_list):
    elem = my_list1.pop(0)
    if elem.isdigit() and elem.isalnum():
        my_list1.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        my_list1.append(f'"+{int(elem):02d}"')
    else:
        my_list1.append(elem)
print(' '.join(my_list1))
print(f"id after {id(my_list1)}")
