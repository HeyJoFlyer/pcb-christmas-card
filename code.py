# SPDX-FileCopyrightText: 2024 HeyJoFlyer
#
# SPDX-License-Identifier: MIT
import board
import neopixel
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.pulse import Pulse
from digitalio import DigitalInOut, Direction, Pull
import time

colors = [(255, 220, 220), (0, 0, 0), (255, 0, 0), (255, 120, 0), (0, 255, 0), (0, 255, 140), (0, 0, 255),  (50, 255, 255), (255, 200, 0), (255, 0, 200), (0, 255,255),] # needs to have an 8 bit R, G, B value
# Don't change these values if you haven't changed the board
SPEED_BUTTON_PIN = board.GP0
BRIGHTNESS_BUTTON_PIN = board.GP2
MODE_BUTTON_PIN = board.GP1
LED_1_PIN = board.GP11
LED_2_PIN = board.GP12
RGB_LED_PIN = board.GP22
NUM_OF_LED = 73


def setup_pins():
    global speed_button
    speed_button = DigitalInOut(SPEED_BUTTON_PIN)
    speed_button.direction = Direction.INPUT
    speed_button.pull = Pull.UP
    global brightness_button
    brightness_button = DigitalInOut(BRIGHTNESS_BUTTON_PIN)
    brightness_button.direction = Direction.INPUT
    brightness_button.pull = Pull.UP
    global mode_button
    mode_button = DigitalInOut(MODE_BUTTON_PIN)
    mode_button.direction = Direction.INPUT
    mode_button.pull = Pull.UP
    global led_1
    led_1 = DigitalInOut(LED_1_PIN)
    led_1.direction = Direction.OUTPUT
    global led_2
    led_2 = DigitalInOut(LED_2_PIN)
    led_2.direction = Direction.OUTPUT
    global rgb_leds
    rgb_leds = neopixel.NeoPixel(RGB_LED_PIN, NUM_OF_LED, brightness = 0.5, auto_write=False)
def blink_leds(nametag_leds, enabled, old_time):
    if enabled == True:
        print(time.time() - old_time)
        if time.time() - old_time > 0.4:
            led_1.value = nametag_leds
            led_2.value = not nametag_leds
            nametag_leds_out = not nametag_leds
            return nametag_leds_out, time.time()
        else: return nametag_leds, old_time
    else:
        led_1.value = False
        led_1.value = False
        return False, time.time()


def main():
    modes = ["solid_color", "rainbow", "colorcycle", "chase", "blink", "pulse"] # only for your reference
    mode_index = 0
    old_mode_index = 0
    brightness = 30 # 0 (off) - 100 (max brightness)
    speed = 120 # 20 (very fast) - 420 (slow)
    color = 0 #index of list from colors module
    colors_number = len(colors)
    current_animation = Solid(rgb_leds, color=colors[0])
    nametag_leds_enabled = True
    nametag_leds = False
    old_time = time.time()
    while True:
        if brightness_button.value == False:
            print("brightness_button")
            brightenss_time = time.time()
            while time.time() - brightenss_time < 0.6:
                current_animation.animate()
            if brightness_button.value == False:
                nametag_leds_enabled = not nametag_leds_enabled
                time.sleep(0.5)
            else:
                brightness += 10
                if brightness > 100:
                    brightness = 0
                rgb_leds.brightness = brightness / 100
        elif speed_button.value == False:
            print("speed_button")
            if mode_index == 0: #change color instead of speed
                color += 1
                if color > colors_number - 1:
                    color = 0
                time.sleep(0.3)
            else:
                speed -= 50
                if speed < 20:
                    speed = 420
                old_mode_index = -1
                time.sleep(0.1)
        elif mode_button.value == False:
            mode_index += 1
            if mode_index > len(modes) - 1:
                mode_index = 0
            time.sleep(0.2)

        if mode_index == 0: #if solid color
                color_tuple = colors[color]
                current_animation = Solid(rgb_leds, color=color_tuple)
        elif mode_index != old_mode_index:
            old_mode_index = mode_index
            if mode_index == 1:
                current_animation = Rainbow(rgb_leds, speed = speed/1000,)
            elif mode_index == 2:
                current_animation = ColorCycle(rgb_leds, speed = speed/1000)
            elif mode_index == 3:
                current_animation = Chase(rgb_leds, speed = speed/1000, color = (255, 255, 0))
            elif mode_index == 4:
                current_animation = Blink(rgb_leds, speed = speed/25, color = (255, 255, 0))
            elif mode_index == 5:
                current_animation = Pulse(rgb_leds, speed = speed/1000, color = (50, 255, 255))
        current_animation.animate()
        nametag_leds, old_time = blink_leds(nametag_leds, enabled = nametag_leds_enabled, old_time = old_time)


setup_pins()
main()
