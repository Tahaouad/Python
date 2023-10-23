
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
sum_of_factorials = 0

for i in range(1, 101):
    sum_of_factorials += factorial(i)

print("La somme des factoriels des 100 premiers nombres entiers positifs est :", sum_of_factorials)