import storage
import uuid

def add_player():
    player_load = storage.load_player()
    player_id = str(uuid.uuid4())
    en_name = "MSD" #input("Enter Player name: ")
    role = "WK" #input("Enter the Player Role: ")
    jersey_no  = 7 #int(input("Enter Player Jersey"))

    new_player = {
        "player_id":player_id,
        "Name": en_name,
        "Role": role,
        "Jersey No":jersey_no,
        "Stats": [],
        "Team Played":[]
    }
    
    player_load.append(new_player)        # add new player to list
    storage.save_player(player_load)      # save the whole list back
    print(f"✅ Player {en_name} added successfully!")

def view_player():
    players_info = storage.load_player()
    
    if not players_info:
        print("Players Not Found on DB.")
    else:
        for p in players_info:
            print(f"Player ID: {p['player_id']}, \nName of the player : {p['Name']}, \nRole of on Match : {p['Role']} \nJersey No: {p['Jersey No']}")
    
def update_player():
    player_info = storage.load_player()
    player_id = input("Enter player id: ")

    for p in player_info:
        if p['player_id'] == player_id:
            print(f"Edit player Detials: {p['Name']}")
            p['Name'] = input("Enter the new Name for Player: ") or p['Name']
            p['Role'] = input("Enter the New Role Of Player: ") or p['Role']
            p['Jersey No'] = int(input("Enter the New Jersey No: ")) or p['Jersey No']

            storage.save_player(player_info)
            print("✅ Player updated successfully!")
        else:
            print("❌ Player ID not found.")

def remove_player():
    player_info = storage.load_player()
    player_id = input("Enter Player Id for Delete: ")

    for p in player_info:
        if p['player_id'] == player_id:
            player_info.remove(p)

            storage.save_player(player_info)
            print("✅ Player Delete successfully!")
        else:
            print("❌ Player ID not found.")
            

# Stats 

def add_stats():
    player_info = storage.load_player()
    player_id = input("Enter Player Id for Stats Updation: ")

    for p in player_info:
        if p['player_id'] == player_id:
            runs = int(input("Enter runs scored: "))
            wickets = int(input("Enter wickets taken: "))
            opponent_team = input("Enter opponent team name: ")

            # add stats
            p['Stats'].append({"Runs": runs,"Wickets":wickets})

            # Update the opponent team who are they played.

            op_team = set(p['Team Played'])
            op_team.add(opponent_team)
            p['Team Played'] = list(op_team)

            storage.save_player(player_info)
            print("✅ Match stats added successfully!")
            
        else:
            print("❌ Player ID not found.")

