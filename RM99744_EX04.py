print("\n---------------------------------------------------- \n")

currentMinute = int(input("Digite o minuto atual marcado pela sua máquina: "))
fatorialValue = currentMinute

for x in range(1, currentMinute):
    predecessor = currentMinute - x
    fatorialValue = fatorialValue * predecessor

print("\n")

print('A senha para liberar a sua maquina é "LIBERDADE{}"'.format(fatorialValue))
print("\n---------------------------------------------------- \n")
