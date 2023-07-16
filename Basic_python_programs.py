'''
@Author : Jabeena L Moolimani
@Date : 16-July-2023
@Last Modified By : Jabeena L Moolimani
@Last Modified Date : 16-July-2023
@Title : Executing basic programs of python

'''

class BasicProgramsOfPython():


    # 1. Write a program to check if the given character is Vowel or Not.
    def check_vowel(self):
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        Character = input("Enter the alphabet : ")

        if Character.lower() in vowels:
            print("The given alphabet is vowel")
            
        else:
            print("Its not Vowel")

    #check_vowel()



    # 2. Write a Python program that accepts a word from the user and reverses it.
    def word_reverse(self):

        word = input("enter the word : ")

        reverse_word = word[::-1]
        print(reverse_word)

    #word_reverse()



    # 3. Write a program when you give number from terminal it should gives you that
    #number in letters (1 to 10)(one to ten )

    def number_in_letter(self):
        num_dictionary = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}

        number = int(input("Enter the number : "))

        if number in num_dictionary.keys():
            print(num_dictionary[number])

        else:
            print('no output')

    #number_in_letter()




    # 4. Greats of 3 numbers and smallest of 3 numbers. (Using list method)
    def largest_small_num(self):
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))
        num3 = int(input("Enter number 3 : "))

        num_list = [num1, num2, num3]

        large = max(num_list)
        small = min(num_list)
        print(f"Largest number is {large}")
        print(f"Smallest number is {small}")

    #largest_small_num()


    # 5.Write a program to print “Hello” if a number entered by user is multiple of 5 otherwise print “Bye”

    def hello_bye(self):
        num = int(input("Enter the number : "))

        if num%5 == 0:
            print('Hello')
        else:
            print('Bye')

    #hello_bye()


    # 6.Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
    def temperature_conversion(self):

        celsius_temp = input("Enter the value of celsius to convert it into Fahrenheit : ")
        TF = round((float(celsius_temp)*1.8) + 32, 3)
        print(f"Temperature in fahrenheit is {TF}")

        fahrenheit_temp = input("Enter the value of Fahrenheit to convert it into celsius  : ")
        TC = round((float(fahrenheit_temp) - 32) * (5/9), 3)
        print(f"Temperature in celcius is {TC}")

    #temperature_conversion()















