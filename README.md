# Mini-cybertruck

This project involed myself making a mini foamboard cyber truck that was driven by 4 motors on a acrylic chassis

Power was supplied by a 3S lipo battery for the motors and a 5v portable battery bank for the Raspberry Pi 3b

Motors were controlled by 2 L293D Motor drivers allowing for motor to have it's own control

A Raspberry Pi 3b was used to control the motordriver using gpio zero library and to receive input from a Playstation 4 controller

On startup, "code2code" was programed to run to allow the user to click a button allowing the master "Testcode" to run. This allowed for the playstaion  controller to connect to the Raspberry pi via bluetooth
