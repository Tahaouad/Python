def tri_bulles(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

liste_a_trier = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(liste_a_trier)

print("Liste triée:", liste_a_trier)
