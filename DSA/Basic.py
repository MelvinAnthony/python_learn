players = ["Rohit", "Virat", "Dhoni", "Bumrah"]

found = False
for i in players:
    if i == "Virat1":
        found = True
        print(f"Player Name : {i}")
        break

if not found:
    print("Data was Not Found...")