quantityFood = input("Qual o total de alimentos que você consumiu hoje?") 
quantityOfCalories = 0

for x in range(int(quantityFood)):
    calorie = input("Qual o total de calorias do seu {}º alimento? ".format(x + 1))
    quantityOfCalories = quantityOfCalories + int(calorie)

print("O seu total de calorias consumidas hoje foi de {} calorias.".format(quantityOfCalories))