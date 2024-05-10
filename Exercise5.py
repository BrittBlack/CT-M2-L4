#5. Looping Lists - The Rhythm of Repetition
#Task 1: The for Loop DJ Set

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']


for track in range(len(genres)):
    print(f"Track {track + 0}: This is {genres[track]}")

# Task 2: The Remix Artist with while


while track < len(genres):
    print(f"Track {track + 0}: This is {genres[track]}")
    break
    if genres[track] == 'Hip-hop':
        print("Party over.")
        
track += 1
       