def is_isogram(string):
    string = string.lower()
    return all(string.count(c) == 1 for c in string)
print(all("string".count(c) == 1 for c in "string"))