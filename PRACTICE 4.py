names = ["Kudzai", "Maitaishe", "Munashe", "Tanatswa", "Aizivaishe"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


with open("names.txt", "r") as file:
    print("Names read from the file:")
    for line in file:
        print(line.strip()) 