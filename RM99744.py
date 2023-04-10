    
daysOfTheWeek = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
monday = 0
tuesdays = 0
wednesday = 0
thursday = 0
friday = 0

for index in range(5):
    print("Votação para live da semana")
    print("\n------------------------------------------------- \n")
    amountOfVotes = input("Qual a quantidade de votos para {}?\n".format(daysOfTheWeek[index]))
    if (index == 0):
        monday = int(amountOfVotes)
    elif (index == 1):
        tuesdays = int(amountOfVotes)
    elif (index == 2):
        wednesday = int(amountOfVotes)
    elif (index == 3):
        thursday = int(amountOfVotes)
    elif (index == 4):
        friday = int(amountOfVotes)

daysOfTheWeek = [monday, tuesdays, wednesday, thursday, friday]
