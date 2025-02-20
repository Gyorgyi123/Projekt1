'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author = Bc. Gyorgyi Fucsekova Posztosova
email: posztosgyorgyi@seznam.cz
'''
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
               
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "passeord123", "pass123"]
uppercase = 0
titlecase = 0
lowwercase = 0
num_of_digits = 0
digits = []
words_lenght = []
len_dict = {}
user_name = (input("Please enter your user name: "))
if user_name in users:
    password = str(input("Please enter your password: "))
    if password in passwords and passwords.index(password) == users.index(user_name):
        print(f"""
{'-' * 40}              
Wellcome to the app, {user_name}
We have 3 texts to be analyzed.   
{'-' * 40}           
              """)
        print("Text 1:", 
      TEXTS[0],
      "\nText 2:\n",
      TEXTS[1],
      "\nText 3:\n",
      TEXTS[2])
        print("-" * 40)
        selected_text = (input("Please select text 1, 2 or 3: "))  
        if not selected_text in {"1", "2", "3"}:
            print("Invalid input, terminating the program")
            exit()
        else: 
            selected_num = int(selected_text)
            text = (TEXTS[selected_num - 1])
            text = (text.replace(",", "").replace(".", "").split())
            for word in text:
                if word.isalpha() and word.isupper():
                    uppercase += 1
                if word.isalpha() and word.istitle():
                    titlecase += 1
                if word.isalpha() and word.islower():
                    lowwercase += 1
                if word.isalpha() and word.isdecimal():
                    num_of_digits += 1
                    digits.append(word)
                words_lenght.append(len(word))
                lenghts = set(words_lenght)
            sum_of_digits = sum([int(item) for item in digits])
            print("-" * 40)
            print(f"You selected text {selected_text}")
            print(f"There are {len(text)} words in this text.")
            print(f"There are {uppercase} uppercase words.")
            print(f"There are {titlecase} titlecase words.")
            print(f"There are {lowwercase} lowercase words.")
            print(f"There are {num_of_digits} numeric strings.")
            print(f"The sum of all the numbers is {sum_of_digits}.")
            for leng in lenghts:
                len_dict.update({leng:words_lenght.count(leng)})
            print(f"""
{'-' * 40}
{"LEN":>4}|{"OCCURENCES":^16} \t |NR. 
{'-' * 40}""")
            for leng in len_dict:
                print(f"{leng:>4}|{'*' * len_dict.get(leng):<16} \t |{len_dict.get(leng)}") 
    else:
        print("Wrong password, terminating the program....")
else:
    print("You are not registered user, terminating the program....")
    











        

    





















