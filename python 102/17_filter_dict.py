matches = [
    {
        "home_team": "Bolivia",
        "away_team": "Uruguay",
        "home_team_score": 3,
        "away_team_score": 1,
        "home_team_result": "Win",
    },
    {
        "home_team": "Brazil",
        "away_team": "Mexico",
        "home_team_score": 1,
        "away_team_score": 1,
        "home_team_result": "Draw",
    },
    {
        "home_team": "Ecuador",
        "away_team": "Venezuela",
        "home_team_score": 5,
        "away_team_score": 0,
        "home_team_result": "Win",
    },
]

print("-" * 20, "MATCHES", "-" * 20)
print(matches)
print("Numbers of matches--", len(matches), "\n")

new_list = list(
    filter(lambda item: item["home_team_result"].lower() == "Win".lower(), matches)
)

print(new_list)

print("Numbers of matches Win--", len(new_list))
