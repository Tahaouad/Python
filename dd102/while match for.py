# def find_needle(haystack):
#     i=0
#     for item in haystack:
#         print(i,item)
#         if item == "needle":
#             return "found the needle at position " + str(i)
#         i = i+1

# def find_needle(haystack):
#     return f'found the needle at position {haystack.index("needle")}'


# haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# result = find_needle(haystack)
# print(result)
# arr = [1,2,3,4,5,6]
# arr = max(arr)
# print(arr)


import timeit

# Première version de la fonction fake_bin
def fake_bin_v1(x):
    R = ""
    for i in range(len(x)):
        if int(x[i]) < 5:
            R = R + "0"
        elif int(x[i]) >= 5:
            R = R + "1"
    return R

# Deuxième version de la fonction fake_bin
def fake_bin_v2(x):
    return ''.join('0' if c < '5' else '1' for c in x)

# Comparaison des temps d'exécution
input_string = "346789"
time_v1 = timeit.timeit(lambda: fake_bin_v1(input_string), number=100000)
time_v2 = timeit.timeit(lambda: fake_bin_v2(input_string), number=100000)

print(f"Temps d'exécution pour la première version: {time_v1} secondes")
print(f"Temps d'exécution pour la deuxième version: {time_v2} secondes")
