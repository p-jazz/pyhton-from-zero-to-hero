# Separa la lista en 3 listas, una con los pares y ptra con los impares y calcular su promedio

numbers = [14,52,54,64,76,23,5,2,54,6,32]
even = []
odds = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odds.append(num)

even_sum = 0
for num in even:
    even_sum += num

odds_sum = 0
for num in odds:
    odds_sum += num

print(f"El promedio de los pares es:", even_sum/len(even))

print(f"El promedio de los impares es:", odds_sum/len(odds))

# print(f"El promedio de los pares es:",sum(even/len(even))

# print(f"El promedio de los impares es:",sum(odds/len(odds))