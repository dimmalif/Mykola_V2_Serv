from Skills.BFunction import BFunction
from Skills.Functions import *


def run(parameters, text):
    result = exec(parameters[0] + '(text)')
    return result
