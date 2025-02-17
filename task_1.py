import os

def palindrome(word=""):
    if len(word) < 2:
        return False
    i = 0
    j = len(word) - 1

    while i<j:
        if word[i] == word[j]:
            i+=1
            j-=1
            continue
        else:
            return False
    return True

if os.path.exists("sentences_analysis.txt"):
    os.remove("sentences_analysis.txt")

with open("sentences.txt", "r") as file:
    for line in file:
        line.strip()
        palindromes = list()
        longest = list()
        length = 0
        words = line.split()
        for word in words:
            if palindrome(word):
                palindromes.append(word)
            if len(word) > length:
                length = len(word)
        for word in words:
            if len(word) == length:
                longest.append(word)

        with open("sentences_analysis.txt", "a") as output:
            output.write(f'''Sentence: {line.strip()}
Word Count: {len(words)}
Longest Word: {longest}
Palindrome: {palindromes}

''')



