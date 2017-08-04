# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# To open file in subdirectory (on Linux and OS X) it would look like this:
# with open('text_files/filename.txt') as file_object:

# To open file in subdirectory (on Windows) it would look like this:
# with open('text_files\filename.txt') as file_object:

# To open file in absolute path (on Linux and OS X) it would look like this:
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# To open file in absolute path (on Windows) it would look like this:
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:


# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())