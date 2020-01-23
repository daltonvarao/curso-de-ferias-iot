# importa o modulo principal 
import RPi.GPIO as gpio

# ajusta modo de gpio para BOARD
gpio.setmode(gpio.BOARD)


# define funcao para ligar led
def liga_led(porta: int) -> None:
    """
    Define o porta como saida e muda para desligada.
    """
    gpio.setup(porta, gpio.OUT)
    gpio.output(porta, gpio.HIGH)


def desliga_led(porta: int) -> None:
    """
    Define a porta como saida muda para ligada.
    """
    gpio.setup(porta, gpio.OUT)
    gpio.output(porta, gpio.LOW)
