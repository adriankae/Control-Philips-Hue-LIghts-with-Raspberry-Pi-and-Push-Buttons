#!/usr/bin/python

# incorporates a push button with a toggle mode for on and off.
# mapping:
# GPIO15: Toggle on/off
# GPIO17: Brightness lower
# GPIO18: brightness higher
# GPIO22: CT lower
# GPIO23: CT higer

from gpiozero import Button
from phue import Bridge
import time

# enter the ip address of your hue bridge here:
hue_ip = '192.168.XXX.XX'

b = Bridge(hue_ip)


# define all the buttons
btn_toggle = Button(15)
btn_bri_lower = Button(17)
btn_bri_higher = Button(18)
btn_ct_lower = Button(22)
btn_ct_higher = Button(23)

# constants for value changes
brightness_change = 20
ct_change = 20

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
# print(b.get_api())


lights = b.lights
# Print all light names
for l in lights:
    print(l.name)

# enter the light you want to change here from the list that is printed above:
hue_light = 'Name of your lamp like Hue Spot Ambience 123'

current_brightness = b.get_light(hue_light, 'bri')
current_ct = b.get_light(hue_light, 'ct')

while True:
    if btn_toggle.is_pressed:
        print('btn_toggle is pressed')
        if b.get_light(hue_light, 'on'):
            print('current brightness is ' + str(current_brightness))
            print('spot 15 is off')
            b.set_light(hue_light,'on', False, transitiontime=0)
            time.sleep(0.2)
        else:
            print('spot 15 is on')
            print('current brightness is ' + str(current_brightness))
            b.set_light(hue_light,'on', True, transitiontime=0)
            b.set_light(hue_light,'bri', current_brightness, transitiontime=0)
            time.sleep(0.2)
    
    while btn_bri_lower.is_pressed and current_brightness >= 1 and b.get_light(hue_light, 'on'):
        temp = current_brightness - brightness_change
        if temp < 1:
            temp = 1
        current_brightness = temp
        print('current brightness is ' + str(current_brightness))
        b.set_light(hue_light,'bri', current_brightness, transitiontime=5)
      
    while btn_bri_higher.is_pressed and current_brightness <= 254 and b.get_light(hue_light, 'on'):
        temp = current_brightness + brightness_change
        if temp > 256:
            temp = 255
        current_brightness = temp
        print('current brightness is ' + str(current_brightness))
        b.set_light(hue_light,'bri', current_brightness, transitiontime=5)
    
    while btn_ct_lower.is_pressed and current_ct >= 120 and b.get_light(hue_light, 'on'):
        current_ct -= ct_change
        print('current ct is ' + str(current_ct))
        b.set_light(hue_light,'ct', current_ct, transitiontime=5)
    
    while btn_ct_higher.is_pressed and current_ct <= 500 and b.get_light(hue_light, 'on'):
        current_ct += ct_change
        print('current ct is ' + str(current_ct))
        b.set_light(hue_light,'ct', current_ct, transitiontime=5)
        

