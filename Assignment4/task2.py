text_to_write = input('Enter text to write to the file: ')
file1 = open('output.txt','w')
file1.write(text_to_write)
file1.close()
print('Data successfully written to output.txt.')

text_to_append = input('Enter additional text to append: ')
file1 = open('output.txt','a')
file1.write(f'\n{text_to_append}')
file1.close()
print('Data successfully appended.')

file1 = open('output.txt','r')
print('Final content of output.txt:')
read_file = file1.read()
print(read_file)
file1.close()