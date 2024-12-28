from decorators import (
    Voice,
    Lamp,
    Automation
)


def client_code(decorator):
    decorator.functional()
lamp = Lamp()
client_code(Voice(lamp))
#client_code(Automation(lamp))