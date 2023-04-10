
class Vote:
  def __init__(self, dayOfTheWeek, amountOfVote):
    self.dayOfTheWeek = dayOfTheWeek
    self.amountOfVote = amountOfVote


listOfVotesByDay = [
    Vote(dayOfTheWeek="Segunda-feira", amountOfVote=0),
    Vote(dayOfTheWeek="Terça-feira", amountOfVote=0),  
    Vote(dayOfTheWeek="Quarta-feira", amountOfVote=0),  
    Vote(dayOfTheWeek="Quinta-feira", amountOfVote=0),  
    Vote(dayOfTheWeek="Sexta-feira", amountOfVote=0)
    ]

topRatedDays = []

listOfVotes = []
print("\n------------------------------------------------------------------------------------------------------\n")

for index in range(5):
    if(index == 0):
        print("Votação para live da semana\n")
    
    amountOfVotes = int(input("Qual a quantidade de votos para {}?\n\n".format(listOfVotesByDay[index].dayOfTheWeek)))
    print("\n")

    if (index == 0):
        listOfVotesByDay[index].amountOfVote = amountOfVotes
        listOfVotes.append(amountOfVotes)
    elif (index == 1):
        listOfVotesByDay[index].amountOfVote = amountOfVotes
        listOfVotes.append(amountOfVotes)
    elif (index == 2):
        listOfVotesByDay[index].amountOfVote = amountOfVotes
        listOfVotes.append(amountOfVotes)
    elif (index == 3):
        listOfVotesByDay[index].amountOfVote = amountOfVotes
        listOfVotes.append(amountOfVotes)
    elif (index == 4):
        listOfVotesByDay[index].amountOfVote = amountOfVotes
        listOfVotes.append(amountOfVotes)

for vote in listOfVotesByDay:
    if(vote.amountOfVote == max(listOfVotes)):
        topRatedDays.append(vote.dayOfTheWeek)

days = ""
if(len(topRatedDays) > 1):
    print('Os dias mais votados foram "{}", com um total de {} votos cada.'.format(" - ".join(topRatedDays), max(listOfVotes)))
else: 
    print('O dia mais votado foi "{}", com um total de {} votos'.format(topRatedDays[0], max(listOfVotes)))
print("\n------------------------------------------------------------------------------------------------------\n")
