# pcb-christmas-card

Have you ever wanted to send a christmas card showing your technical abilities? I have the solution for you, you don't need to change any tracks. Just change the text and you are good to send gift this card.

You can send this card to practically anyone.

## Features

- Brightness, speed, effect control
- Simple 3 button interface
- 73 WS2812B adressable RGB leds (very bright)
- 32 Alternating flashing leds
- Customizable text (removed from my image)

![pcb image](https://github.com/HeyJoFlyer/pcb-christmas-card/blob/main/christmas%20PCB.avif?raw=true)

## Getting started

1. `git clone https://github.com/HeyJoFlyer/pcb-christmas-card.git`
1. open files with kicad and edit the text on the front and back (you dont need to install any libraries if you just edit the text)
1. upload the gerber files to your pcb manufacturer of choice
1. decide if you want PCB assembly (highly recommended due to high led density)
1. upload `bom` and `pos` files from `jlcpcb` directory.
1. Verify placement of components!
1. Order pcb
1. Solder a raspberry pi pico to the backside (you could also use pcba assembly, but 2 sided assembly is typically way more expensive)
1. Upload Circuitpython by Adafruit to the raspberry pi pico
1. Upload libraries from lib to lib on th respberry pi pico (the provided libraries only work for Circuitpython 8.x.x)
1. Upload `code.py`
1. I used a permanent marker to write a different name on each card, because the minimum order quantitiy is five so I could gift it to different people.

## License
This project is licensed under the [MIT LICENSE](LICENSE), circuitpython and the libraries by Adafruit are also licensed under the MIT LICENSE.