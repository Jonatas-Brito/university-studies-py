quantityOfExpenses = input("Quantas transações consideradas como despesas você executou hoje?") 
totalOfExpenses = 0

for x in range(int(quantityOfExpenses)):
    expenses = input("Qual o total de sua {}ª primeira despesa? ".format(x + 1))
    totalOfExpenses = totalOfExpenses + int(expenses)

print("O valor total de suas despesas do dia foi de {}. E a média para cada uma das despesas foi de {}.".format(totalOfExpenses, int(totalOfExpenses) / int(quantityOfExpenses)))