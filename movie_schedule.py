current_movies = {"The Grinch": "11:00AM",
                  "Rudolph": '1:00PM',
                  'Frost the Snowman': '3:00PM',
                  'Christmas Vacation': '5:00PM'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, "is playing at", showtime)