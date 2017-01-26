def alphabet_position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    for i in range(len(alphabet)):
        if alphabet[i] == letter.lower():
            return i

def rotate_character(char, rot):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    if char.isalpha():
        position = alphabet_position(char)
        rot_char = (position + rot) % 26

        if char in upper:
            return upper[rot_char]
        else:
            return lower[rot_char]
    else:
        return char


def encrypt(text, rot):
    encrypted = ""

    for char in text:
        encrypted = encrypted + rotate_character(char, rot)

    return encrypted
