"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomas Zechmeister

email: t.zech@seznam.cz

discord: Tony Rocky Horror#9131

"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = input('username: ')
password = input('password: ')

splitter = 40 * '-'

registered_users = {'bob':'123',
                    'ann':'pass123',
                    'mike':'password123',
                    'liz':'pass123'}

registered = username in registered_users.keys()
correct_password = password == registered_users.get(username)

if registered:
    if correct_password:
        print(f'{splitter}\nWelcome to the app, {username}.\nWe have {len(TEXTS)} texts to be analyzed.\n{splitter}')
        selection = input(f'Enter a number btw. 1 and {len(TEXTS)} to select: ')
        while selection.isalpha() or int(selection) not in range(1, len(TEXTS) + 1): 
            print(f'ERROR:Please enter NUMBERS ONLY! Available options: {list(range(1, len(TEXTS) + 1))}\n{splitter}')
            selection = input(f'Enter a number btw. 1 and {len(TEXTS)} to select: ')
        else:
            print(splitter)
            cleaned_text = TEXTS[int(selection) - 1].split()
            final_text = []
            length_words = dict()
            titlecase_counter, uppercase_counter, lowercase_counter, numeric_counter, sum_numeric = 0,0,0,0,0
            
            for word in cleaned_text:
                word = word.strip(",.?!")
                final_text.append(word)
                length_word = len(word)
                if length_word not in length_words.keys():
                    length_words[length_word] = 1
                else:
                    length_words[length_word] += 1
                if word.isalpha() and word.isupper():
                    uppercase_counter += 1
                elif word.isalpha() and word.islower():
                    lowercase_counter += 1
                elif word.isnumeric():
                    numeric_counter += 1
                    sum_numeric += int(word)
                for letter in word[0]:
                    if letter.isalpha() and letter.isupper():
                        titlecase_counter += 1
                
            sum_words = (len(final_text))
            print(f'There are {sum_words} words in the selected text.')
            print(f'There are {titlecase_counter} titlecase words.')
            print(f'There are {uppercase_counter} uppercase words.')
            print(f'There are {lowercase_counter} lowercase words.')
            print(f'There are {numeric_counter} numeric strings.')
            print(f'The sum of all the numbers {sum_numeric}')
            header = f"{splitter}\nLEN|\tOCCURENCES\t| NR.\n{splitter}"
            print(header)
            sorted_length_words = sorted(length_words.keys(),reverse = True)
            for number in range(sorted_length_words[-1],sorted_length_words[0] + 1):
                if number not in length_words.keys():
                    continue
                stars_counter = length_words.get(number) * '*'
                letters_counter = length_words.get(number)
                line_new = f'{number:>3}|{stars_counter:<11}  \t|{letters_counter:<25}'
                print(line_new)    
                
    else:
        print('ERROR: Invalid password!')
        quit() 
else:
    print(f'ERROR: Unregistered user - {username}, terminating the program..')
    quit()
