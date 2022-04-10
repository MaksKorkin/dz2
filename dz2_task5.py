input_list = [57.8, 46.51, 97, 32.54, 15.21, 84.26, 25, 97.09, 0.16, 46]

store_id = id(input_list)
print(input_list)

# task 5.a
print(f"{'a':-^100}")

end_word:str = ", "

for i, num in enumerate(input_list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(input_list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

# task 5.b
print(f"{'b':-^100}")
print(f"id before sort {store_id}")
input_list.sort()
print(input_list)
print(f"id after sort {id(input_list)}")

if store_id == id(input_list):
    print("In place")
else:
    print("Diff obj")


# task 5.c
print(f"{'c':-^100}")

copy_of_list = input_list.copy() # or use input_list[:]
copy_of_list.sort(reverse=True) # or use list(sorted()) without copy

print(copy_of_list)
print(store_id)
print(id(copy_of_list))

if store_id == id(copy_of_list):
    print("In place")
else:
    print("Diff obj")



# task 5.d
print(f"{'d':-^100}")

# 1. input_list is sorted in 5.b so we need just take last 5 elem
print("five biger prices", input_list[-6:-1])
