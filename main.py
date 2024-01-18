def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    sum_words = count_words(text)
    dic_letters = count_letters(text.lower())
    print_report(sum_words, dic_letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    sum_words = len(text.split())
    return sum_words

def count_letters(text):
    dic_letters = {}
    for letter in text:
        if letter in dic_letters:
            dic_letters[letter] += 1
        else:
            dic_letters[letter] = 1
    return dic_letters
    
def print_report(sum_words, dic_letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print("{} words found in the document".format(sum_words))
    print()
    dic_letters = {k: v for k, v in sorted(dic_letters.items(), key=lambda item: item[1], reverse=True)}
    dic_letters = {k: v for k, v in dic_letters.items() if k.isalpha()}
    for letter, count in dic_letters.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")
main()
