# 3.5.1: writing to a file on disk
filename = "mynewfile.txt"

# Open the file with append permission
# myfile = open(filename, 'a')

# # Write to the file
# log = "Just kidding I love Python\n"
# myfile.write(log)

# Close the file
# myfile.close()

myfile = open(filename, 'r')

for i in myfile:
    print(i)
