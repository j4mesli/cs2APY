# cs2APY

Counter-Strike 2 Premier Leaderboard API Module & Raw API in `Python3`.

#### Example Use:
```python
import cs2leaderboard as cs2

# w/o manual class instantiation, fetches all leaderboards
all = cs2.fetch_all()

# w/ instantiation, fetches all leaderboards
_instance = cs2.cs2leaderboard()
_all = _instance.fetch_all()
```

#### Methods:
```python
fetch_all(): fetches all the regions' leaderboards and returns them as an array of dicts

fetch_global(): fetches the leaderboard for Global rankings and returns them as an array of dicts

fetch_europe(): fetches the leaderboard for European rankings and returns them as an array of dicts

fetch_africa(): fetches the leaderboard for African rankings and returns them as an array of dicts

fetch_asia(): fetches the leaderboard for Asian rankings and returns them as an array of dicts

fetch_australia(): fetches the leaderboard for Australian rankings and returns them as an array of dicts

fetch_china(): fetches the leaderboard for Chinese rankings and returns them as an array of dicts

fetch_northamerica(): fetches the leaderboard for NA rankings and returns them as an array of dicts

fetch_southamerica(): fetches the leaderboard for SA rankings and returns them as an array of dicts
```

#### Example Output:
```python
import cs2leaderboard as cs2

africa = cs2.fetch_africa()
print(africa)

# Output
# [
#     {
#         "rank": 1,
#         "rating": 22117,
#         "name": "splitsecond kirito",
#         "matches_won": 163,
#         "matches_tied": null,
#         "matches_lost": 21,
#         "map_stats": {
#             "anubis": 2,
#             "inferno": 1,
#             "mirage": 6,
#             "vertigo": 0,
#             "overpass": 0,
#             "nuke": 0,
#             "ancient": 1,
#             "null": 0
#         },
#         "time_achieved": "2023-10-10T19:40:08",
#         "region": "africa"
#     },
#     ...
#  ]
```
