# Curso de IoT

## Módulos do curso


## Aprendendo a manipular o GPIO do Raspberry Pi
O GPIO _(General Purpose Input and Output)_ são portas programáveis de entrada e saída de dados que são utilizadas para prover uma interface entre os periféricos e os microcontroladores ou microprocessadores [[1]](#araujo2014).

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

## Desenvolvendo um Servidor HTTP
Um servidor HTTP é um software que compreende URLs (endereços web) e HTTP (o protocolo que seu navegador utiliza para visualizar páginas web [[2]](#mozilla).
```python
from flask import Flask, render_template

# define a classe principal do servidor
app = Flask(__name__)

# rota para requisição GET em '/'
@app.route('/')
def index():
    """A função é executada em toda requisição."""
    return 'Servidor IoT'

# sobe o servidor localmente
if __name__ = '__main__':
    app.run()
```

## Introdução ao MQTT e a Websockets
MQTT é um protocolo de comunicação entre máquinas que utiliza do protocolo TCP/IP, famoso no ramo da computação e em redes de computadores.
O seu funcionamento consiste na configuração de um servidor central **BROKER** e na troca de mensagens **_Publish_** e **_Subscribe_** entre clientes.

## Referências 
 - <a id="araujo2014">[1]</a> ARAÚJO, Thayron. Raspberry Pi B+: Introdução a Porta GPIO. 2014. Disponível em: <https://blog.fazedores.com/raspberry-pi-b-introducao-porta-gpio/>. Acesso em: 12 jan. 2020.

 - <a id="mozilla">[2]</a> Fundação Mozilla. O que é um servidor web (web server)?. 2019. Disponível em: <https://developer.mozilla.org/pt-BR/docs/Learn/Common_questions/o_que_e_um_web_server/>. Acesso em: 12 jan. 2020.