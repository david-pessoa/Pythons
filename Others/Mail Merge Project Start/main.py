with open(r"./Input/Letters/starting_letter.txt", "r") as example:
    texto = example.readlines()
with open(r"./Input/Names/invited_names.txt", "r") as names_file:
    lines = names_file.readlines()
    for name in lines:
        name = name.rstrip()
        linha1 = texto[0]
        linha1 = linha1.replace("[name]", name)
        with open(r"./Output/ReadyToSend/" +"Letter_" + name + ".txt", "w") as letter:
            letter.write(linha1)
            for i in range(1, len(texto)):
                letter.write(texto[i])
