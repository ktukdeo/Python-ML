# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
d1=data['innings'][0]['1st innings']['deliveries'];
d2=data['innings'][1]['2nd innings']['deliveries'];

batsman = "SC Ganguly"
d = filter(lambda x:(list(x.values()))[0]['batsman'] == batsman,d1)
print("#Deliveries Ganguly faced:",len(list(d)))

#  Who was man of the match and how many runs did he scored ?
man_of_match = data["info"]["player_of_match"][0]
batsman = man_of_match
runs = sum([z['runs']['batsman'] for x in d1 for y,z in x.items() if z['batsman'] == batsman])
runs = runs + sum([z['runs']['batsman'] for x in d2 for y,z in x.items() if z['batsman'] == batsman])
print("Man of the match:",man_of_match,"  Runs:",runs);


#  Which batsman played in the first inning?
batsmen = set([z['batsman'] for x in d1 for y,z in x.items()])
batsmen = " , ".join(batsmen)
print("Batsmen in 1st innings: ",batsmen)

# Which batsman had the most no. of sixes in first inning ?
batsman = list(Counter([z['batsman'] for x in d1 for y,z in x.items() if z['runs']['batsman'] == 6]))[0]
print("Max no of sixes in 1st innings by: ",batsman)

# Find the names of all players that got bowled out in the second innings.
batsmen = [z['batsman'] for x in d2 for y,z in x.items() if z.get('wicket',{}).get('kind','') == 'bowled']
print("Batsmen bowled in 2nd innings: "," , ".join(batsmen))


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
runs = sum([z['runs']['extras'] for x in d2 for y,z in x.items()]) - sum([z['runs']['extras'] for x in d1 for y,z in x.items()])
print("More Extra runs: ",runs)


# Code ends here


