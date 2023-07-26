import time
# Agregar un menu de 2 opcione para ver la bomba de tiempo
# 1 ver bomba de tiempo, 2 para salir

num = 10
user_option = ""
while user_option != "2" :
    user_option = input("Ingresa 1 para jugar y 2 para salir: ")

    if user_option == "1":
        while (num >= 0 ):
            print(num)
            time.sleep(1)
            num = num - 1
    print("BOOM")
    

    if user_option == "2":
        print("adios")