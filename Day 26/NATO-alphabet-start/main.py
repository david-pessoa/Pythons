import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value["letter"]:value["code"] for key, value in data.iterrows()}
while True:
    name = input("Type your name: ").upper()
    try:
        nato_list_name = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, type only letters in the aplhabet, please")
    else:
        break

print(nato_list_name)

