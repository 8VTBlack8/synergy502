word = input('Введите свое слово : ')

eg = word.count('e') # считает количество гласных e
ag = word.count('a') # считает количество гласных a
ig = word.count('i') # считает количество гласных i
ug = word.count('u') # считает количество гласных u
og = word.count('o') # считает количество гласных o

howmanyglas = eg + ag + ig + ug + og # суммирует гласные

print("всего гласных", howmanyglas) # выводит количество гласных
print("всего согласных", len(word) - howmanyglas) # считает сколько букв в слове и минусует от общего количества букв
# гласные, выводит количество согласных
if (eg == 0): print ("гласной E - False")
else: print("гласное e -", eg, "в слове")
if (ug == 0): print ("гласной U - False")
else: print("гласной u -", ug, "в слове")
if (og == 0): print ("гласной O - False")
else: print("гласной o -", og, "в слове")
if (ag == 0): print ("гласной A - False")
else: print("гласной a -", ag, "в слове")
if (ig == 0): print ("гласной I - False")
else: print("гласной i -", ig, "в слове")