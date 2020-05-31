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

    elif (words == "радио"
            or words == "включи радио"
            or words == "эфир"):
        result = "radio"

    elif (words == "выключи радио"
            or words == "стоп радио"):
        result = "radiostop"

    elif (words == "анекдот"
            or words == "еще анекдот"
            or words == "расскажи анекдот"
            or words == "шутку давай"):
        result = "anekdot"

    elif (words == "давай поиграем в города"
            or words == "города"
            or words == "давай поиграем в игру города"):
        result = "cities"

    return result