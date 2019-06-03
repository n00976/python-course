#Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os
statinfo = os.stat("cytaty.txt")
statinfo
print(statinfo.st_size)