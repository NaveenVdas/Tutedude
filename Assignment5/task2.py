list = []

for i in range(1,11):
    list.append(i)
print(f'Original list: {list}')

sliced_list = list[:5]
print(f'Extracted first five elements: {sliced_list}')
sliced_list.reverse()
print(f'Reversed extracted elements: {sliced_list}')

