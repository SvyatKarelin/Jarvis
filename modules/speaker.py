from modules import weather


def speaker ():
    user_input = input("")
    while user_input != "/exit":
        if user_input == "узнать погоду" or user_input == "узнай погоду":
            weather.weather()
        print()
        user_input = input("")
