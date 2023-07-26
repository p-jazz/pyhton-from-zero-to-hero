# Podemos tener listas anidadas:

# Podriamos tener unalista con las calificaciones de cada estudiante

students = ["Seba", "Gonza", "Gaby"]
grades = [[5,6,4,5,6,7],[6,7,6,5,6,4],[6,6,5,6,7,7]]

# SE pide hacer un programa que imprima algo similar a:
# El estudiante Seba tiene primedio xx
# El estudiante Gonza tiene...


averages = []
for student_grades in grades:
    averages.append(sum(student_grades)/len(student_grades))

for position in range(len(students)):
    print(f"El estudiante", students[position], "tiene promedio:", averages[position])



    
