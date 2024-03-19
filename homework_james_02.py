# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 2 Assignment: Nested If

### 1. Nested Decisions: The Adventure Game ###

place = input("Choose a place: forest or cave? ")

if place == "forest":                                           # changed = to ==
    action = input("climb a tree or cross a river? ")           # added space at end of prompt
    if action == "climb a tree":                                # changed = to ==
        print("You found a bird's nest!")
    elif action == "cross a river":                             # changed = to ==
        print("You found a boat!")
    else:
        pass
elif place == "cave":                                           # changed = to ==
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You fell down a pit! Oh the humanity!")
    else:                                                       # added else for other inputs
        pass
else:
    pass

print()

### 2. Quick Decisions: The Event Planner ###

# get number of attendees and determine venue
attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"     # type cast attendees variable as int
print("Venue:", venue)

# recommend audio visual equipment
if venue == "large hall":
    print("Be sure you have some very professional equipment for such a large event!")
elif int(attendees) > 20:
    print("Make sure your conference room has an audio system and a projector!")
elif int(attendees) > 8:
    print("Gather attendees around your laptop for all your audio visual needs!")
else:
    print("If you need to share a video, just show it on your phone!")

# recommend caterers
vegetarian_preference = input("Should your event have vegetarian options? (yes/no) ")
caterer_recommendation = "Veggie Delight Caterers" if vegetarian_preference == "yes" else "Gourmet Meals Caterers"
print(caterer_recommendation, "is a great catering company for your needs!")