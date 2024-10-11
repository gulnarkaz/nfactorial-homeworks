def exercise1():
    print("Exercise 1: start")
    # Declare 2 numbers and calculate their sum
    num1 = 5  
    num2 = 6 
    total = num1 + num2
    print("Total:", total)
    print("Exercise 1: end")

def exercise2():
    print("Exercise 2: start")
    # Declare a string and reverse it
    string1 = "Almaty" 
    reversed_string = string1[::-1]
    print("Reversed string:", reversed_string)
    print("Exercise 2: end")

def exercise3():
    print("Exercise 3: start")
    # Declare a string and calculate its length
    string2 = "Astana" 
    length = len(string2)
    print("String length:", length)
    print("Exercise 3: end")
        
def exercise4():
    print("Exercise 4: start")
    # Declare 2 strings and concatinate them
    name = "Gulnara "
    surname = "Bakirova"
    concatinated_string = name + surname
    print("Full name:", concatinated_string)
    print("Exercise 4, end")

def exercise5():
    print("Exercise 5: start")
    # Declare a character and check if is vowel
    # First define a dictionary with vowel charcters
    vowels = {
        "a", "e", "i", "o", "u"
    }
    declared_char = "a"
    if declared_char in vowels:
        print("The character is vowel:", declared_char)
    else:
        print("It is not vowel:", declared_char)
    print ("Exercise 5: end")
    
def exercise6():
    print("Exercise 6: start")
    # Declare a string and swap first and last character of the string
    original_string = "Computer"
    swapped_string = original_string[-1] + original_string[1:-1] + original_string[0]
    print("Swapped string is ", swapped_string)
    print ("Exercise 6: end")
def exercise7():
    print("Exercise 7: start")
    # Declare a string and convert to uppercase
    lowercase_string = "example"
    uppercase_string = lowercase_string.upper()
    print("Uppercase string is ", uppercase_string)
    print ("Exercise 7: end")
    
def exercise8():
    print("Exercise 8: start")
    # Declare the length and width of a rectangle and Calculate the area
    length_rectangle = 4
    width_rectangle = 6
    area = length_rectangle * width_rectangle
    print("Area of the rectangle is ", area)
    print ("Exercise 8: end")
    
def exercise9():
    print("Exercise 9: start")
    # Declare a number and Check if the number is even
    number = 7
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is not even")
    
    print ("Exercise 9: end")
    
def exercise10():
    print("Exercise 10: start")
    # Declare a string and Extract the first three characters of the string
    city = "Shymkent"
    extracted_char = city[:3]
    print("First three characters are", extracted_char)
    
    print ("Exercise 10: end")
    
def exercise11():
    print("Exercise 11: start")
    # Declare 2 variables, name and age and Use string interpolation to create a message
    name_ = "Aizat"
    age = 19
    message = f"Name {name_}, age {age}"
    print(message)
    
    print ("Exercise 11: end")
    
def exercise12():
    print("Exercise 12: start")
    # Declare a string and Extract the characters from index 2 to 5 (inclusive)
    str_ = "exercise"
    char_extract = str_[2:6]
    print("Extracted characters indexed 2 to 5 is ", char_extract)
    print ("Exercise 12: end")
    
def exercise13():
    print("Exercise 13: start")
    # Declare a number as a string and Convert the string to an integer
    str_number = "5"
    number_int = int(str_number)
    print("The number is", number_int)
    print ("Exercise 13: end")
    
def exercise14():
    print("Exercise 14: start")
    # Declare a string and Repeat the string 3 times
    str__ = "Thank you! "
    repeat_str_3 = str__ * 3
    print("Repeat 3 times", repeat_str_3)
    print ("Exercise 14: end")
    
def exercise15():
    print("Exercise 15: start")
    # Declare 2 numbers and Calculate the quotient and remainder
    num_1 = 9
    num_2 = 2
    quotient = 9 // 2
    remainder = 9 % 2
    result = f"quotient is {quotient}, remainder is {remainder}"
    print(result)
    print ("Exercise 15: end")
    
def exercise16():
    print("Exercise 16: start")
    # Declare 2 numbers and Calculate the result of float division
    num_1 = 9
    num_2 = 2
    float_division = 9 / 2
    
    print(f"The result of float division is {float_division}")
    print ("Exercise 16: end")
    
def exercise17():
    print("Exercise 17: start")
    # Declare a string and Use a string method to count the occurrences of a character
    string_new = "Hello"
    # We will count each character
    count_h = string_new.lower().count('h')
    count_e = string_new.lower().count('e')
    count_l = string_new.lower().count('l')
    count_o = string_new.lower().count('o')
    print(f"Total number of h is {count_h} times")
    print(f"Total number of e is {count_e} times")
    print(f"Total number of l is {count_l} times")
    print(f"Total number of o is {count_o} times")
    print ("Exercise 17: end")
    
def exercise18():
    print("Exercise 18: start")
    # Declare a string with double quotes inside and Use escape sequences to include the quotes

    print("He said \"I am hungry\" and started to eat")
    print ("Exercise 18: end")
    
def exercise19():
    print("Exercise 19: start")
    # Declare a multi-line string and Print the multi-line string

    print("Astana\nAlmaty\nShymkent\nAtyrau")
    print ("Exercise 19: end")
    
def exercise20():
    print("Exercise 20: start")
    # Declare 2 numbers, base and exponent and Calculate the result of base to the power of exponent
    base = 2
    exponent = 3
    result = 2 ** 3
    print(result)
    print ("Exercise 20: end") 
    
def exercise21():
    print("Exercise 21: start")
    # Declare a palindrome string (A palindrome is a word that is spelled the same forward and backward. ex: "racecar")
    #Check if it is palindromic without using loops
    palindrome_str = "racecar"
    if palindrome_str == palindrome_str[::-1]:
        print(palindrome_str, "is palindrome")
    else:
        print(palindrome_str, "is not palindrome")
    
    print ("Exercise 21: end")
    
def exercise22():
    print("Exercise 22: start")
    # Declare 2 strings and Check if the strings are anagrams (ignoring case)
    # Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

    if sorted("loop") == sorted("pool"):
        print("It is Anagram")
    else:
        print("It is not Anagram")
    
    print ("Exercise 22: end")

if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()
    exercise18()
    exercise19()
    exercise20()
    exercise21()
    exercise22()