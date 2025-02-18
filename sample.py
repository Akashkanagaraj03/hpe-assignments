import os

def is_palindrome(word=""):
    word = word.lower()
    if len(word) < 2:
        return False

    start, end = 0, len(word) - 1
    while start<end:
        if word[start] == word[end]:
            start+=1
            end-=1
            continue
        else:
            return False
    return True

def longest_words(words):
    longest = list()
    longest.append("")
    for word in words:
        if len(word) > len(longest[0]):
            longest.clear()
            longest.append(word)
        elif len(word) == len(longest[0]):
            longest.append(word)
    return longest

def palindrome_words(words):
    palindromes = list()
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

if os.path.exists("sentences_analysis.txt"):
    os.remove("sentences_analysis.txt")

with open("sentences.txt", "r") as file:
    for line in file:
        line.strip()
        words = line.split()

        longest = longest_words(words)
        palindromes = palindrome_words(words)

        with open("sentences_analysis.txt", "a") as output:
            output.write(f'''Sentence: {line.strip()}
Word Count: {len(words)}
Longest Word: {longest}
Palindrome: {palindromes if len(palindromes) >0 else "None"}

''')



