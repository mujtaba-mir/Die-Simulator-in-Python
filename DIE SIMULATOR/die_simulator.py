print("WELCOME TO THE DIE SIMULATOR")
import random
  
x = "y"
  
while x == "y":
     
    no = random.randint(1,6)
     
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print("You got 1")
        print("\n")

    elif no == 2:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")
        print("Wow you got 2")
        print("\n")

    elif no == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
        print("Yeah! its a 3")
        print("\n")

    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print("Wow! 4 for you")
        print("\n")

    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print("Give me a high five cuz its a 5")
        print("\n")

    elif no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print("Fantastic you got 6")
        print("\n")
        
    x=input("press y to roll again and n to exit:")

    print("\n")
    print("BYE BYE! :)")