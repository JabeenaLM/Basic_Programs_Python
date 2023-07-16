'''
@Author : Jabeena L Moolimani
@Date : 16-July-2023
@Last Modified By : Jabeena L Moolimani
@Last Modified Date : 16-July-2023
@Title : Executing basic programs of python (Main File)

'''


from Basic_python_programs import BasicProgramsOfPython

if __name__ == "__main__":

    programs_obj = BasicProgramsOfPython()

    print("Welcome to Basic programs of python")

    while True:
        option = int(input("1:Temperature conversion from celsius to fahrenheit and vice versa\n2:Check if the given character is vowel or not\n3:Accept word from the user and reverses it\n4:Number in letters\n5:Greatest and smallest of 3 numbers\n6:Print 'Hello' if given number is multiple of zero else 'Bye'\n7:Exit\n"))

        if option == 1:
            programs_obj.temperature_conversion()

        elif option == 2:
            programs_obj.check_vowel()

        elif option == 3:
            programs_obj.word_reverse()
        
        elif option == 4:
            programs_obj.number_in_letter()
        
        elif option == 5:
            programs_obj.largest_small_num()

        elif option == 6:
            programs_obj.hello_bye()

        elif option == 7:
            break

    