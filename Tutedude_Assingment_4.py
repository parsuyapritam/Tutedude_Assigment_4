#Task1

try:
    File = open('sample.txt','r')
    Lines = File.readlines()
    print("Reading file content: ")
    print("Line1: "+ Lines[0] + "Line2: "+ Lines[1]+'\n')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.\n")

#Task2


A=input('Enter text to write to the file: ')

File = open('output.txt','w')
Write = File.write(A+'\n')
print('Data successfully written to output.txt.\n')
#File.close()

B=input('Enter additional text to append: ')

File = open('output.txt','a')
Write = File.write(B+'\n')
print('Data successfully written to output.txt.\n')
#File.close()

File = open('output.txt','r')
read = File.readlines()
File.close()

print('Final content of output.txt: \n',read[0],read[1])

#end




