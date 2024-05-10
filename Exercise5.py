#5. Looping Lists - The Rhythm of Repetition
#Task 1
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track = 0


for i in range(len(genres)):
    genre = genres[i]
    track += 1
   
    print(f"This is track {track}: {genre}.")


#Task 2 : The Remix Artist with while


track = 1


while track <= len(genres):
    for genre in genres:
         if genre == 'Classical':
            print("Stop the music!")
            break
    print(f"This is track {track}: {genre}.")
    track += 1


    genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']




#Task 3: Light Show Technician Loop


for i in range(len(genres)):
    genre = genres[i]
    if genre == 'Classical':
        continue
   
    print(f"This is track {i+1}: {genre}. Light show is a go.")
