#Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url
#pozwól użytkownikowi podać adres www.
#Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się: https:// , http://, www, bez www
#Może się kończyć za pomocą: .pl, .com
#Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.

import webbrowser
import urllib.error as ue


def open_url(site_name):
    if site_name[:8] == "https://" or site_name[:7] == "http://" or site_name[:3] == "www":
        if site_name[-3:] == ".pl" or site_name[-4:] == ".com":
            webbrowser.open(site_name)
    else:
        raise ue.URLError("Twój adres strony jest nieprawidłowy, spróbuj zacząć od https://, http:// lub www")


def main():
    site_name = input("Podaj stronę internetową, którą chcesz otworzyć:")
    open_url(site_name)


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')