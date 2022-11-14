print("1 - szyfruj\n2 - odszyfruj\n")
wybor = int(input())
if(wybor == 1):
    przesuniecie = int(input("Podaj przesuniecie:"))
    text = input("Podaj text:")
    text_szyfrowany = ""
    for x in text:
        litera = ord(x)
        if (litera+przesuniecie > 122):
            litera -= 26
        text_szyfrowany += chr(litera + przesuniecie)
    print(text_szyfrowany)
else:
    text = input("Podaj text:")
    for y in list(range(1, 27)):
        text_odszyfrowany = ""
        for x in text:
            litera = ord(x)
            if (litera != 32):
                litera -= y
                if (litera < 97):
                    litera += 26
                text_odszyfrowany += chr(litera)
            else:
                text_odszyfrowany += " "
        print(y,": ", text_odszyfrowany)
