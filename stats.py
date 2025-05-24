def wordcount(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters = {}

    for letter in text:
        low = letter.lower()
        if low in letters:
            letters[low] +=1
        else:
            letters[low] = 1

    return letters

def sort_on(d):
    return d["num"]

def dictionary_sort(num_letters):
    sorted_list = []
    for ch in num_letters:
        sorted_list.append({"char": ch, "num": num_letters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list