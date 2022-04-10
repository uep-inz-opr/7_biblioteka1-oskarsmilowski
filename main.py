from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Ksiazka:
    tytul: str
    autor: str
    rok: int

@dataclass(frozen=True, order=True)
class Biblioteka:
    ksiazka: Ksiazka
    egzemplarze: int


def main():
    liczba_ksiaze = input()
    print(liczba_ksiaze)

    for _ in range(int(liczba_ksiaze))
        ksiazka = input()
        print(ksiazka)

if __name__ == "__main__":
    main()
