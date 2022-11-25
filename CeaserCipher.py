TheText = input("Input your text here: ")

def CeasarCipher(TheText, Step):
    CryptText = []
    OutText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for EachLetter in TheText:
        if EachLetter in uppercase:
            Number = uppercase.index(EachLetter)
            Crypting = (Number + Step) % 26
            CryptText.append(Crypting)
            NewLetter = uppercase[Crypting]
            OutText.append(NewLetter)
        elif EachLetter in lowercase:
            Number = lowercase.index(EachLetter)
            Crypting = (Number + Step) % 26
            CryptText.append(Crypting)
            NewLetter = lowercase[Crypting]
            OutText.append(NewLetter)
    return OutText

OfficialCipher = CeasarCipher(TheText, 2)
print(OfficialCipher)