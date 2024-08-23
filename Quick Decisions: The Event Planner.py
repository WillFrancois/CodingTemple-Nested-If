#Task 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

#Task 2
should_have_audio_system = "No audio system" if attendees < 50 else "Bring audio system"
should_have_projector = "No projector" if attendees < 15 else "Bring projector"

#Task 3
food = input("Would you like vegetarian food y/n? ")
if food[0] == 'y':
    food_preference = "I recommend Veggie Delight Caterers!"
else:
    food_preference = "I recommend Gourmet Meals Caterers!"

print("", venue, should_have_audio_system, should_have_projector, "Food: " + food_preference, sep="\n")
