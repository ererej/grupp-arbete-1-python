import os
import keyboard

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
[3]shut down
""")

start_screen_printer(difficulty)

while (True):
    key = keyboard.read_key()
    if keyboard._Event == keyboard.KEY_DOWN:
        continue
    if key == "1": #den faking dubbel klickar!!!!
        difficulty +=1
        if difficulty >= 4:
            difficulty = 1
        start_screen_printer(difficulty)
    
    elif key == "2":
        mainloop()
    
    elif key == "3":
        print(0/0)

