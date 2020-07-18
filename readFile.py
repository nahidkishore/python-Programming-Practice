#read file
''' 
file= open('student.txt','r')

text=file.read()
print(text)
file.close() '''

#read and write korte chaile " r+" use korbo

file= open('student.txt','r+')

text=file.read()
print(text)
file.close()


f = open("demofile.txt", "r")
print(f.read())

#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

#Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))


#Python File Write
#Write to an Existing File
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



#Create a New File

''' "x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist '''


#Create a file called "myfile.txt":
 #f = open("myfile.txt", "x") 
#Result: a new empty file is created!

f = open("myfile.txt", "w")
f.write("Now the file has more content!")
f.close()

#Delete a File
import os
os.remove("testFile.txt")
