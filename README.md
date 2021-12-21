# Control-Philips-Hue-Lights-with-Raspberry-Pi-and-Push-Buttons

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

Another easy way to get the IP address with your raspberry pi is this:

Install nmap by opening the terminal and typing

`sudo apt install nmap`

and then run the command

`namp -sP 192.168.178.0/24`

Adjust the IP address for your own network. 

The output looks something like this:
```
Starting Nmap 7.80 ( https://nmap.org ) at 2021-12-21 20:34 CET
Nmap scan report for fritz.box (192.168.178.1)
Host is up (0.0089s latency).
Nmap scan report for homebridge.fritz.box (192.168.178.21)
Host is up (0.0072s latency).
```
  
Now that you have the IP address of your hue bridge write it down. We're gonna need it for the code.

### Step 2: Wire up your Pi

Here is a wiring diagram. 
Use 10k resistors and wire up everything like on the schematics. 

![Wiring diagram!](https://github.com/adriankae/Control-Philips-Hue-Lights-with-Raspberry-Pi-and-Push-Buttons/blob/main/wiring_pi.png "Wiring diagram")


### Step 3: Install the PHUE library

Just open up a terminal and type:

`pip install phue`

Now you are good to run the code! 

### Step 4: Run the code

Just clone the repository or download it to your computer. 
Open a terminal and navigate to the folder where the python file is located and run it with

`python hue_control.py`

The video in the next sections shows the setup in action. Enjoy!

## Video


## Further pictures

![Actual Setup 1](https://github.com/adriankae/Control-Philips-Hue-Lights-with-Raspberry-Pi-and-Push-Buttons/blob/main/IMG_0444.jpeg "Setup 1")
![Actual Setup 2](https://github.com/adriankae/Control-Philips-Hue-Lights-with-Raspberry-Pi-and-Push-Buttons/blob/main/IMG_0445.jpeg "Setup 2")
