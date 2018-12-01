def caesar(input:str):
    new_word = ''
    for letter in input:
        if letter.isalpha():
            new_letter = chr(ord(letter) + 1)
            #print(new_letter)
            new_word = new_word + new_letter
        else:
            #print(letter)
            new_word = new_word + letter
    print(str(new_word))

if __name__ == "__main__":
    sentence = input("Teie lause?" )
    caesar(sentence)