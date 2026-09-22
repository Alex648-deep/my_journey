import pandas

complete_list= []

whole_dic = pandas.read_csv("nato_phonetic_alphabet.csv")

all_letters={rows.letter:rows.code for (index,rows) in whole_dic.iterrows() }


name=input("enter your name: ").upper()

for letter in name:
    complete_list.append(all_letters[letter])

print(complete_list)



