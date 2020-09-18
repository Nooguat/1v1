import os

def FileExists(file): -> bool
    try:
        open(file)
    except:
        return False
    return True