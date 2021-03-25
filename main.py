# TODO: Create a letter using starting_letter.docx

with open("letter.docx") as letter:
    contents = letter.read()


with open("./input/Names/invited_names.txt") as name_list:
    # Used the readlines method
    names = name_list.readlines()
    name_list = []
    for i in names:
        # dot strip method to remove "\n"
        stripped_name = i.strip()
        name_list.append(stripped_name)


for x in range(0, (len(name_list))):
    # Replace method
    new_test = contents.replace("[name]", name_list[x])
    with open(f"./Output/ReadyToSend/letter_for_{name_list[x]}.docx", "w") as files:
        final_result = files.write(new_test)

