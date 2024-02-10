import random
print("losowanie w lotto!")
print("-------------------")
while True:
    try:
        liczba_losow = int(input("ile masz losów? (max. 10): "))
        break
    except ValueError:
        print("wpisz poprawną liczbę")

if (liczba_losow > 0) and (liczba_losow <= 10):
    for i in range(liczba_losow):
        liczby_end = []
        for z in range(5):
            liczba = random.randint(1, 49)
            liczby_end.append(str(liczba))
        print(f"{i + 1}.  ", ", ".join(liczby_end))

else:
    print("Wpisz poprawną liczbę")

