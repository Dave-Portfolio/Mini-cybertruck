# Mini-cybertruck

This project involved creating a mini foamboard Cybertruck driven by four motors on an acrylic chassis.

The motors were powered by a 3S LiPo battery, while a 5V portable battery bank supplied power to a Raspberry Pi 3b.

Motor control was achieved through two L293D motor drivers, allowing individual control for each motor.

A Raspberry Pi 3b managed the motor drivers using the GPIO Zero library and received input from a PlayStation 4 controller.

On startup, a program named "code2code" was executed, enabling the user to click a button that triggered the main "Testcode" program. This allowed time for the PlayStation 4 controller to connect to the Raspberry Pi via Bluetooth.

A camera with a 2-axis gimbal was positioned at the rear, providing movement in two axes. The controller had a dedicated button for capturing pictures.
