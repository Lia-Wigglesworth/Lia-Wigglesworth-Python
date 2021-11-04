characters = []
import random

text = input("Enter text to be encrypted here: ")
random_Number = random.randint(1,4) #generates random number
# shifts each letter up by a random amount
for x in text:
    x = chr(ord(x) + random_Number)
    characters.append(x)
# each second character is moved to the beginning and all other characters to the end
beginning_Char = " ".join(characters[::2])
end_Char = " ".join(characters[1::2])
print(beginning_Char + " " + end_Char)
# this information is sent to a text file
outFileName="C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\encrypted_File.txt"
outFile=open(outFileName, "w")
outFile.write(beginning_Char + " " + end_Char)
outFile.close() 
