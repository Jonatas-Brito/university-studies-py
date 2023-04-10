listOfOddStudents = []
listOfEvenStudents = []

for studentNumber in range (1, 50, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
    studentGrade = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}\n\n".format(studentNumber)))
    listOfOddStudents.append(studentGrade)
    print("\n----------------------------------------------------------------------------------\n")

    
for studentNumber in range (2, 51, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    studentGrade = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}\n\n".format(studentNumber)))
    listOfEvenStudents.append(studentGrade)
    print("\n----------------------------------------------------------------------------------\n")

print("Média de alunos da lista de alunos impares: {}\n".format(sum(listOfOddStudents) / 25))

print("Média de alunos da lista de alunos pares: {}\n".format(sum(listOfEvenStudents) / 25))

highestScoreOfOddStudents = max(listOfOddStudents)

highestScoreOfEvenStudents = max(listOfEvenStudents)

if(highestScoreOfOddStudents == highestScoreOfEvenStudents):
    print("A maior nota registrada foi {} e está disponível em ambas as listas de alunos".format(highestScoreOfOddStudents))
elif(highestScoreOfOddStudents > highestScoreOfEvenStudents):
    print("A maior nota registrada foi {} e está disponível na lista de alunos impares".format(highestScoreOfOddStudents))
elif(highestScoreOfOddStudents < highestScoreOfEvenStudents):
    print("A maior nota registrada foi {} e está disponível na lista de alunos pares".format(highestScoreOfEvenStudents))

print("\n----------------------------------------------------------------------------------\n")
