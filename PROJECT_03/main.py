# Fake News Headline Generator

import random

subjects =[ "ShahRukhKhan","Virat Kohli","Nirmala Sitaraman","Modi","Rahul Gandhi"]
actions=["launches","eats at","dances with","cancels","declare war ","orders","celebrates"]
places_or_things=["at red fort","mumbai local train","inside parliament","during IPL match","at India Gate","a plate of samosa"]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    Headine=f"BREAKING NEWS:{subject} {action} {place_or_thing}"
    print(Headine)
    user_input=input("Do you want another Headline? (yes/no)\n").strip().lower()
    if(user_input=="no"):
        break

print("Good Bye,Thanks for using Fake News Headline Generator")
          