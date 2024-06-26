#6. Advanced Looping Techniques
#Task 1: The Selective DJ


# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']


sublist = genres[1:4]


for genre in sublist:
    print("Playing. " + genre + " Playing it how we want to.")


#Task 2: The One-Liner Band with List Comprehensions
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genres_update = [i + ' Music' for i in genres ]

print(genres_update)

#Task 3: Numerical Beats with range

timer = 10
for i in range(timer, 0, -1):
    print(i)
    if i == 1:
        print("The beat drops now!")