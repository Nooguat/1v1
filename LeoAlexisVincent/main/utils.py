import os

def FileExists(file) -> bool:
    try:
        open(file)
    except:
        return False
    return True

def GameFileWrite(text) -> None:
    file = open("game", 'w+')
    file.write(text)
    file.close()