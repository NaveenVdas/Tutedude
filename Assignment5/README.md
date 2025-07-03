## ✅ Task 1: Create a Dictionary of Student Marks

### 📝 Problem Statement

Write a Python program that:

1. Creates a dictionary where student names are keys and their marks are values
2. Asks the user to input a student's name
3. Retrieves and displays the corresponding marks
4. If the student’s name is not found, display an appropriate message

### 💡 Solution

```python
# 1. Create a dictionary of student marks
students = {'Naveen': 99, 'Dileep': 99}

# 2. Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# 3. Retrieve and display marks if the student is found
if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
# 4. If not found, show an appropriate message
else:
    print('Student not found.')

```

## ✅ Task 2: Demonstrate List Slicing

### 📝 Problem Statement

Write a Python program that:

1. Creates a list of numbers from 1 to 10
2. Extracts the first five elements from the list
3. Reverses these extracted elements
4. Prints both the extracted list and the reversed list

### 💡 Solution

```python
list = []

# 1.  Creates a list of numbers from 1 to 10.
for i in range(1,11):
    list.append(i)
print(f'Original list: {list}')

# 2.  Extracts the first five elements from the list.
sliced_list = list[:5]
print(f'Extracted first five elements: {sliced_list}')

# 3.  Reverses these extracted elements.
sliced_list.reverse()

# 4.  Prints both the extracted list and the reversed list
print(f'Reversed extracted elements: {sliced_list}')
```
