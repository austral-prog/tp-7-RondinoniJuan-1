def index_of_by_index(word, list, index):
    for i in range(index, len(list)):
        if list[i] == word:
            return i

    return -1

def index_of_empty(list):
    for i in range(len(list)):
        if list[i] == "":
            return i

    return -1

def index_of(word, list):
    for i in range(len(list)):
        if list[i] == word:
            return i

    return -1

print(index_of("Black", ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]))

def put(word, list):
    for i in range(len(list)):
        if list[i] == "":
            list[i] = word
            return i

    return -1

def remove(word, list):
    count = 0

    for i in range(len(list)):
        if list[i] == word:
            list[i] = ""
            count += 1

    return count
    
    return -1
