# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny
# zapis. Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import modul_zad3 as m3

def main():
    save_or_open = input("zapis/odczyt?")
    file_name = input("nazwa pliku:")

    if save_or_open == "zapis":
        save_content = input("co chcesz zapisać?:")
        m3.save_file(file_name, save_content)
    elif save_or_open == "odczyt":
        m3.open_file(file_name)

main()