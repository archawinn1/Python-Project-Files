# string concantentation (aka how to put strings together)
# suppose we want to create a string that says "Subscribe to ____"

youtuber = "Tharches" #Empty string variable

# a few ways to do this
#print("Subscribe to " + youtuber)

#print("Subscribe to {}".format(youtuber))

#print(f"Subscribe to {youtuber}")

adj = input("Insert adjective: ")
verb1 = input("Insert verb:")
verb2 = input("Insert verb:")
famous_person = input("Insert Celebrity: ")

madlib = f"Computer programming is {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)