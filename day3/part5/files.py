# 3.5.1: writing to a file on disk
filename = "myfile.txt"

# Open the file with append permission
myfile = open(filename, 'a')

# Write to the file
log = "this app is rather simple"
myfile.write(log)

# Close the file
myfile.close()