# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("Przelicznik walut")
zlote = float(input("Proszę, podaj kwotę pieniędzy, którą chcesz wziąć na wakacje:"))
euro = zlote // 4.30385192
dolary = zlote // 3.82362388
print("Twoja kwota w euro to: " + str(euro))
print("Twoja kwota w dolarach to:" + str(dolary))