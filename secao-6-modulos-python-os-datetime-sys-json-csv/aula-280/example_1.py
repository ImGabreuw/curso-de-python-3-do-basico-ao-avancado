import locale

locales = locale.locale_alias.items()

for name, value in locales:
    print(name, "=>", value)
