""" CUENTA REGRESIVA
Escribe un programa en Python que realice una cuenta regresiva desde 10 hasta 0.
Durante la cuenta regresiva, cuando el número llegue a 5, imprime un mensaje """

for number in range(10, -1, -1):
    print(number)
    if number == 5:
        print("Halfway point reached!")
print("Countdown complete!")