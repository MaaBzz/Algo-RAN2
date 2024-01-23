temperature_ambiante = float(input("Saisir une température"))
temperature_bassins = float(input("Saisir une température"))
diff_temp = abs(temperature_ambiante - temperature_bassins)
if diff_temp <20 or diff_temp >40:
    print("Alarme")
else:
    print("Température normale")