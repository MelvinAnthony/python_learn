import json, os

players_file = "player.json"
team_file = "team.json"


# General
def load_data(file_path, default):
    if not os.path.exists():
        return default
    with open(file_path,'r') as f:
        return json.load(f)
    
def save_data(file_path,data):
    with open(file_path,"w") as f:
        json.dump(data, f,indent=4)

# player
def load_player():
    return load_data(players_file, [])

def save_players(players):
    return save_data(players_file, players)

# Team
def load_team():
    return load_data(team_file,[])

def save_team(team_det):
    return save_data(team_file, team_det)



