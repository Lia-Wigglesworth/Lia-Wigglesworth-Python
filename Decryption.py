# definition of lists used in code
list = []
final_characters = []
beginning_characters = []
decrypted_Code = []
word_List = ["Hi", "hi", "Hello", "hello", "My", "my", "name", "is", "Lia", "Horan", "The" "the", "goodbye", "bye", "and", "this", "thank", "you"]

# main function of code
def my_Function():
    # clears the lists for when function is looped
    decrypted_Code.clear()
    list.clear()
    final_characters.clear()
    beginning_characters.clear()
    # changes the character by a certain amount and adds it to a list
    for y in characters:
        y = chr(ord(y) - my_Val)
        list.append(y)
    list2 = list[::2] # places every second value into another list
    x = (len(list2)) # finds the number of characters in this list
    # splits the text into two parts depending on if it is even or odd
    if (x % 2) != 0:
        final_characters.extend(list2[int(x/2+1):])
        beginning_characters.extend(list2[:int(x/2+1)])
        final_characters.append(" ")
    else:
        final_characters.extend(list2[int(x/2):])
        beginning_characters.extend(list2[:int(x/2)])
    a = 0 # the list item number
    char_Count = (len(beginning_characters)) # the number of characters in the first half
    while char_Count > 0: # loops through the two groups the encrypted text has been sorted into and alternates them to form a new order
        b = (beginning_characters[a] + final_characters[a])
        decrypted_Code.extend(b)
        a = a + 1
        char_Count = char_Count - 1 # using the number of characters it repeats until they have all be recorded

def form_Words():
    a = 0 
    decrypted_Code.extend(" ") # add space to the end of decrypted code so that words can be seperated
    while decrypted_Code.count(" ") != 0:  # while there are spaces in the decrypted code 
        space = decrypted_Code.index(' ')
        decrypted_Code[a:space] = [''.join(decrypted_Code[a:space])] # merges everything up the space into one word
        decrypted_Code.remove(" ")
        a = a + 1

def check_Words(): # identifies specific English words
    global words_Indentified
    words_Indentified = 0
    for x in decrypted_Code:
        if x in word_List:
            words_Indentified = words_Indentified + 1

# main section of code
with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\Text_Files\\encrypted_File.txt") as encrypted_File: # reads the file the encrypted text is contained in
    characters = encrypted_File.read()
my_Val = 1
my_Function()
form_Words()

#checks for key words
with open("C:\\Users\\pc\\Documents\\Y9\\9IST3\\Python Assessment Files\\Text_Files\\word_List.txt") as dictionary: # reads the file the encrypted text is contained in
    for line in dictionary:
        word_List.extend(line)
        a = 0 
    word_List.extend("\n") # add a line break to end so that words can be seperated
    while word_List.count("\n") != 0:  # while there are line breaks in the word list
        linebreak = word_List.index('\n')
        word_List[a:linebreak] = [''.join(word_List[a:linebreak])] # merges everything up the space into one word
        word_List.remove("\n")
        a = a + 1
words_Indentified = 0
check_Words() 

# indentifies the correct option
while words_Indentified < 1: 
    my_Val = my_Val + 1
    my_Function()
    form_Words()
    check_Words()
    if my_Val > 5:
        print()
        print("No keywords were found")
        print()
        import sys
        sys.exit()
print()
print(*decrypted_Code)
print()