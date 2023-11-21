
import keyboard

difficulty = 2

print("""
[1]difficulty [impossible]
[2]start
[3]shut down
""")

while (True):
    key = keyboard.read_key()
    if keyboard._Event == keyboard.KEY_DOWN:
        continue
    if key == "1": #den faking dubbel klickar!!!!
        difficulty +=1
        if difficulty >= 4:
            difficulty = 1
        print(f"svårhets graden är nu {difficulty}")    #radera när vi har en print funktion för start menyn
    
    elif key == "2":
        mainloop()
    
    elif key == "3":
        print(0/0)

