from enum import Enum

class Subscription (Enum):
    BASIC = 30
    SILVER = 20
    GOLD = 10
    PLATINUM = 5
    DEFAULT = "Default"

class Any (Enum):
    DEFAULT = any

subscriptionType = Subscription.DEFAULT
annualBilling = 0
percentageOnBilling = 0

subscriptionsNameList = [Subscription.BASIC.name, Subscription.SILVER.name, Subscription.GOLD.name, Subscription.PLATINUM.name]

counter = 0
    
while subscriptionType in Subscription:
    if(counter == 0):
        counter = 1
        print("\n-----------------------------------------------------------\n")

        print("Calcule o bônus por assinatura\n")
    subscriptionTypeInput = input("Qual é o tipo de assinatura do cliente? \n\n")
    subscriptionTypeInputToUpper = subscriptionTypeInput.upper()

    if (subscriptionTypeInputToUpper in subscriptionsNameList):
        
        annualBilling = float(input("\nQual é o faturamento anual deste cliente? \n\n"))

        if subscriptionTypeInputToUpper == Subscription.BASIC.name:
            percentageOnBilling = annualBilling * Subscription.BASIC.value / 100
            subscriptionType = Any.DEFAULT

        elif subscriptionTypeInputToUpper == Subscription.SILVER.name:
            percentageOnBilling = annualBilling * Subscription.SILVER.value / 100
            subscriptionType = Any.DEFAULT

        elif subscriptionTypeInputToUpper == Subscription.GOLD.name:
            percentageOnBilling = annualBilling * Subscription.GOLD.value / 100
            subscriptionType = Any.DEFAULT

        elif subscriptionTypeInputToUpper == Subscription.PLATINUM.name:
            percentageOnBilling = annualBilling * Subscription.PLATINUM.value / 100
            subscriptionType = Any.DEFAULT

    else:
        print('\nO tipo "{}" não é um tipo de assinatura válida \n'.format(subscriptionTypeInput))
        print('-----------------------------------------------------------\n')

print('\nO valor de bônus a receber deste cliente é de {} reais\n'.format(percentageOnBilling))
print('-----------------------------------------------------------\n')

   

    

