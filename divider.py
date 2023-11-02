def main():
    """
    Ermittelt den grössten gemeinsamen Teiler von zwei Ganzzahlen
    :return: None
    """
    first_number = int(input("Gib die erste Ganzzahl ein > "))
    second_number = int(input("Gib die zweite Ganzzahl ein > "))
    while second_number != 0:
        modulo = first_number % second_number
        second_number = first_number
        first_number = modulo
    print(str(second_number))


if __name__ == '__main__':
    main()