# def upper_string(s):
#     return s.upper()

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# map_object = map(upper_string, people)
# print(list(map_object))

# Exercise 1

# def display_message():
#     print("I have a big dick")
# display_message()

#Exerecise 2

# def favorite_book(title):
#     print("One of my favorite books is "+title)

# favorite_book("De Grijze Jager")

#Exercise 3

# def describe_city(city, country):
#     print(city + " is in " + country)
# describe_city("paris", "france")

#Exercise 5
# def make_shirt(size='large', text='I Love Python'):
#     print("The size of the shirt is " +size+ " and the text is "+text)
# make_shirt()
# make_shirt('medium')
# make_shirt('small','penis')

#Exercise 6

# def show_magicians(magicians):
#     for magician in magicians:
#         print("The Great"+ magician.title())
# magician_names = [' Harry Houdini', ' David Blaine', ' Criss Angel']
# show_magicians(magician_names)

#Exercise 7
import random
def get_random_temp(season):
    if season == "winter":
        return(random.randint(-10, 16))
    elif season == "summer":
        return(random.randint(32, 40))
    elif season == "spring":
        return(random.randint(24, 32))
    elif season == "autumn":
        return(random.randint(16, 24))
get_random_temp("autumn")
def main():
    temp = get_random_temp("autumn")
    if temp < 0:
        print( "Brrr, that’s freezing! Wear some extra layers today")
    elif 0<= temp <= 16:
        print( "Quite chilly! Don’t forget your coat")
    elif 16< temp <= 23:
         print( "C'EST L'AUTOMNE ESHGHGGGUHVHIC")
    elif 24< temp <= 32:
        print("CHRANAAAA")
    elif 32< temp <= 40:
        print("CANICULEEEE")
main()















