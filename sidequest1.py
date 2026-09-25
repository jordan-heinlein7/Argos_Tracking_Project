#Set a variable to the CSV filename (string object that is the file path to data)
the_filename = 'Data/raw/Satellite tracking of black-capped petrels 2019-argos.csv'
#Create a file object pointing to file name, the mode 'r' stands for read only
f = open(the_filename,'r')

#Create a list of all the lines in the file via the file object.
line_list = f.readlines()
#Close the file
f.close()
#print the 11th item in the line list
print(line_list[10])

#alternative method to open files in python using with open
with open(the_filename, "r") as file:
    text = file.read()

print(text)

