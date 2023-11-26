def tri_insertion(arr):
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1
        while j >= 0 and cle < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle

liste_a_trier = [12, 11, 13, 5, 6]
tri_insertion(liste_a_trier)
print("Liste triée:", liste_a_trier)
