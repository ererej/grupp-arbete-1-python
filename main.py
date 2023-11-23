import os
import keyboard
import time

difficulty = 2

def start_screen_printer(difficulty: int):
    """printar start screenen :D"""
    os.system("cls")
    if difficulty == 1:
        difficulty = "Easy"
    elif difficulty == 2:
        difficulty = "Normal"
    else:
        difficulty = "Hard"
    print(f"""
[1]difficulty [{difficulty}]
[2]start
[3]keybinds
[4]shut down
""")

start_screen_printer(difficulty)

ofset = 0

while (True):
    if ofset == 1:
        ofset = 0
        print()
        continue
    ofset = 1
    key = keyboard.read_key()
    if keyboard._Event == keyboard.KEY_DOWN:
        print("sup")
    if key == "1": #den faking dubbel klickar!!!!
        difficulty +=1
        if difficulty >= 4:
            difficulty = 1
        start_screen_printer(difficulty)
    
    elif key == "2":
        #mainloop()
        pass
    
    elif key == "3":
        #os.system("cls")
        print("""
Keybinds:
Enter the left door:    [Q]            
Enter the middle door:  [W]
Enter the right door:   [E]
""")
 
    elif key == "4":
        print(0/0)


