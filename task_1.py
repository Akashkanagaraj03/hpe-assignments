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

def main():
    if os.path.exists("sentences_analysis.txt"):
        os.remove("sentences_analysis.txt")
    with open("sentences.txt", "r") as input_file, open("sentences_analysis.txt", "a") as output_file:
        for line in input_file:
            line.strip()
            words = line.split()

            output = f"Sentence: {line.strip()}\n" + \
                     f"Word Count: {len(words)}\n" + \
                     f"Longest Word: {longest_words(words)}\n" + \
                     f"Palindrome: {palindrome_words(words) if len(palindrome_words(words)) > 0 else 'None'}\n\n"

            output_file.write(output)

if __name__ == "__main__":
    main()
