# a journaling app
import sys
from datetime import date

arg1 = sys.argv[0]
arg2 = ""

# Filename to write
filename = "journal.txt"

# journal entry function
def add_journal_entry(entry_text):

    # Open the file with append permission
    myfile = open(filename, 'a')

    date_of_entry = str(date.today())
    full_journal_entry = date_of_entry + " : " + entry_text + "\n"

    # Write the entry to the file
    myfile.write(full_journal_entry)

    # Close the file
    myfile.close()


def print_journal_entries(num):
    filename = "journal.txt"
    myfile = open(filename, "r")

    num = int(num)
    line_number = 0
    for line in myfile:
        print(line)
        line_number = line_number + 1
        if line_number == num:
            break

    myfile.close()





if len(sys.argv) == 1:
    new_entry = input("What would you like to enter in the journal? ")
    add_journal_entry(new_entry)
    print("All done!")
    
elif len(sys.argv) == 3:
    if (sys.argv[1] == "--printlast"):
        print_journal_entries(sys.argv[2])
    
