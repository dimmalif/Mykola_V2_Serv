from Recognition.recognition import *
from Skills.skills import *


def run(filename):
    parameters = Recognition.recognise(filename)
    # speak(parameters[1].replace(parameters[2], ''))
    exec(f'{parameters[2]} + (parametesr[0])')
