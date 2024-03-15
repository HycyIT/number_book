import json

contacts = {}


def add_contact(contacts, number, contact):
    contacts[number] = contact
    print("Kontakt dodany pomyślnie")


def find_contact_number(number, contacts):
    if number in contacts:
        print(contacts[number])
    else:
        print("Nie znaleziono kontaktu")


def find_contact_contact(contacts, contact):
    for number, name in contacts.items():
        if name == contact:
            print(f"Numer telfonu to {number}")
            return
        else:
            print("Nie znaleziono kontaktu")


def delete_contacts_number(contacts, number):
    if number in contacts:
        del contacts[number]
        print("Kontakt usunięty")
    else:
        print("Nie znaleziono kontaktu")


def delete_contacts_contact(contacts, contact):
    for number, name in contacts.items():
        if name == contact:
            del contacts[number]
            print("Kontakt usunięty")
            return
        else:
            print("Nie znaleziono kontaktu")


def adress_book():
    print("Witaj w książce adresowej : ")
    while True:
        print("""
              Menu : 
              1) Dodaj nową osobę.
              2) Pokaż kontakty.
              3) Wyszukaj kontakt.
              4) Usuń kontakt.
              5) Zapisz kontakty.
              6) Zakończ program.
               """)
        choose = int(input("Powiedz co chcesz zrobic? : "))
        if choose == 1:
            number = input("Podaj numer telefonu")
            if len(number) == 9:
                contact = input("Podaj nazwę kontaktu")
                add_contact(contacts, number, contact)
            else:
                print("Numer jest za krótki. Powrót do menu")
        elif choose == 2:
            print(contacts)
        elif choose == 3:
            search = int(input("Wybierz 1 : 'number' lub 2 : 'contact'"))
            if search == 1:
                number = input("Podaj numer telefonu: ")
                find_contact_number(number, contacts)
            elif search == 2:
                contact = input("Podaj nazwe kontaktu: ")
                find_contact_contact(contacts, contact)
            else:
                print("Podaj prawidłową wartość")
        elif choose == 4:
            search = int(input("Wybierz 1 : 'number' lub 2 : 'contact'"))
            if search == 1:
                number = input("Podaj numer telefonu: ")
                delete_contacts_number(contacts, number)
            elif search == 2:
                contact = input("Podaj nazwe kontaktu: ")
                delete_contacts_contact(contacts, contact)
        elif choose == 5:
            file_name = "contacts.json"
            with open(file_name, "w") as file:
                json.dump(contacts, file)
            print("Kontakty zapisane")
        elif choose == 6:
            print("Do zobazenia")
            break


adress_book()
