def checkForCommand(words):
    result = ""
    if (words == "завершить работу"
            or words == "заверши работу"
            or words == "стоп"
            or words == "сворачивайся"):
        result = "exit"

    elif (words == "включи игру"
          or words == "давай поиграем"
          or words == "играть"
          or words == "игра"):
        result = "game"

    elif (words == "погода"
          or words == "узнай погоду"
          or words == "что там с погодой"
          or words == "что с погодой"
          or words == "прогноз погоды"):
        result = "weather"

    return result