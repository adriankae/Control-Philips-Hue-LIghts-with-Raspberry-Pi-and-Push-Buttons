# Control-Philips-Hue-LIghts-with-Raspberry-Pi-and-Push-Buttons

With this set up you can control any Light Bulb connected to your Philips Hue Bridge. 
You can toggle the light, change the brightness and change the color temperature.
Here you can learn how!

## Components you need

All the componentes you need for realising this project. 
It's a complete list with amazon affiliate links:

- [Raspberry Pi 4 (or 3 or 2 or Zero W)](https://amzn.to/3pfbdiW) 
- [Mouse & Keyboard](https://amzn.to/3FhlSj1)
- [Monitor](https://amzn.to/32lkzkk)
- [Philips Hue Bridge](https://amzn.to/3poGctj)
- [Philips Hue Lamp White Ambiance](https://amzn.to/3Fgyy9C)
- [Fritz!Box](https://amzn.to/3q7Ucqk)
- [Breadboard & Jumper Wires](https://amzn.to/3J6E15e)
- [10k Resistors](https://amzn.to/3EnyNPa)
- [Push Buttons](https://amzn.to/3EeDQ4b)

I realise that there are some expensive components included but I already had most of it at home. You may have some equipment already, too.

## Getting Started

### Step 0: Assumptions & Preconditions
- Your Rapberry Pi is running the newest version of Raspbian
- Your Router, Hue Bridge and Hue Lamp are connected and set up and it is possible to control the light via the Philips Hue App or your Smart Home App of choide (Apple Home, etc.)
- You have physical access to the Hue Bridge

### Step 1: Get your Hue Bridge's IP address

In order to talk to our Hue Bridge we need its IP address.
We can get it from the FRITZ!Box or from our router or DHCP server if we have access to those.
