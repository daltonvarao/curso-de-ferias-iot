# Curso de IoT

## Módulos do curso


### Aprendendo a manipular o GPIO do Raspberry Pi
O GPIO _(General Purpose Input and Output)_ são portas programáveis de entrada e saída de dados que são utilizadas para prover uma interface entre os periféricos e os microcontroladores ou microprocessadores [[1]](#araujo2014).

![Image of Yaktocat](/screenshots/manipulando_gpio.png)

```python
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
```

### 

## Referências 
 - <a id="araujo2014">[1]</a> ARAÚJO, Thayron. Raspberry Pi B+: Introdução a Porta GPIO. 2014. Disponível em: <https://blog.fazedores.com/raspberry-pi-b-introducao-porta-gpio/>. Acesso em: 12 jan. 2020.