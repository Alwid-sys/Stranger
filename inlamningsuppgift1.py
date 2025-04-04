import os

input_file =input("vilken fil vill du undersöka?: ")

if os.path.isfile(input_file) == True:
    print("Filen finns och är en fil")
else:
    print("Filen finns inte eller är inte en fil")

if True:
    with open(input_file) as f:
        rad = f.readlines()
        bokstav = sum(len(ord) for ord in rad)
print("Den innehåller:\nAntal rader:", len(rad),"\nAntal bokstäver:", bokstav)

fraga = input("vill du söka efter ett ord i filen? J/N: ").upper()
if fraga == "J":
    input_ord = input("vilket ord vill du söka efter?: ").strip()

    rad_index = [i +1 for i, rad in enumerate(rad) if input_ord in rad]
    if rad_index:             
        print(f"Ordet finns i filen och förekommer {len(rad_index)} gånger, på rad: {', '.join(map(str, rad_index))}")
    else:
        print("Ordet finns inte i filen")
else:
     print("Nehe, inte den här gången")

#if mimetypes.guess_file(input_file) == "text/plain":
#   print("Snyggt, är en textfil")
#else: 
#        print("Är inte en fil")
    




    

