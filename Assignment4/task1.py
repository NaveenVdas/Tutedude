try:
    file = open('sample.txt','r')
    print("Reading file content:")
    reading_file_firstLine = file.readline()
    reading_file_secondLine = file.readline()
    print(f'Line 1: {reading_file_firstLine}')
    print(f'Line 2: {reading_file_secondLine}')
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
