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
fetch_all(): fetches all the regions' leaderboards, conglomerates them into one object/dict, and returns said object

fetch_global(): fetches the leaderboard for Global rankings, conglomerates them into one object/dict, and returns said object

fetch_europe(): fetches the leaderboard for European rankings, conglomerates them into one object/dict, and returns said object

fetch_africa(): fetches the leaderboard for African rankings, conglomerates them into one object/dict, and returns said object

fetch_asia(): fetches the leaderboard for Asian rankings, conglomerates them into one object/dict, and returns said object

fetch_australia(): fetches the leaderboard for Australian rankings, conglomerates them into one object/dict, and returns said object

fetch_china(): fetches the leaderboard for Chinese rankings, conglomerates them into one object/dict, and returns said object

fetch_northamerica(): fetches the leaderboard for NA rankings, conglomerates them into one object/dict, and returns said object

fetch_southamerica(): fetches the leaderboard for SA rankings, conglomerates them into one object/dict, and returns said object
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
