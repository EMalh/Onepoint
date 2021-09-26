""" Caesar Cipher """


def ceasar_code(plain_text, n_shift):
    """ A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a
    letter found by moving n places down the alphabet.
    :param plain_text: plain-text message
    :param n_shift: number of letters to shift in the cipher
    :return: encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged
    :note: The plain text is all lowercase ASCII except for whitespace and punctuation
    """

    ciphed_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        # "a" is 97, "z" is 122
        if ord(char) < 97 or ord(char) > 122:  # Keeping punctuation and whitespace
            ciphed_text += char
        else:
            ciphed_text += chr((ord(char) + n_shift - 97) % 26 + 97)
    return ciphed_text


if __name__ == '__main__':

    print("Please, enter your plain text :")
    plain_text = input().lower()
    print("Please, enter your number of letters to shift :")
    try:
        n_shift = int(input())
    except:
        print("Format not valid, enter a number !")
    print(ceasar_code(plain_text, n_shift))
