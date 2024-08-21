# LED Control Using Blynk and Raspberry Pi

## Overview

This project demonstrates how to control an LED remotely using the Blynk IoT platform and a Raspberry Pi.

## Components

- Raspberry Pi
- LED
- Resistor
- Breadboard and jumper wires
- Internet connection
- Blynk app

## Setup Instructions

1. **Hardware Setup:**
   - Connect the LED to the Raspberry Pi. Follow standard LED circuit diagrams for proper wiring.
   - For a visual guide, see [hardware_setup.png](hardware_setup.png).

2. **Blynk Setup:**
   - Follow the instructions in [SETUP_blynk.md](../SETUP_blynk.md) to set up Blynk on your Raspberry Pi.

3. **Raspberry Pi Configuration:**
   - Download and install the Blynk library if not already done.
   - Create a Python script (e.g., `led_control.py`) to interact with Blynk and control the LED.

4. **Running the Code:**
   - Execute the Python script on your Raspberry Pi to start controlling the LED remotely.

## Code

For the code used in this project, see [led_control.py](led_control.py).

### Code Explanation

- **Initialization:** Import necessary libraries and set up the Blynk connection.
- **LED Control:** Define functions to turn the LED on and off based on Blynk commands.
- **Main Loop:** Continuously check for commands from the Blynk app and update the LED state accordingly.

## Troubleshooting

- **LED Not Responding:** Ensure that the LED is connected correctly and that the resistor is properly placed.
- **Blynk Authentication Issues:** Verify that you have copied the correct Auth Token into your script.
- **Script Not Running:** Check for any syntax errors in your Python script and ensure that all required libraries are installed.

## Additional Files

- **hardware_setup.png:** Diagram of the LED hardware setup.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, feedback, or collaboration inquiries, feel free to reach out to me:

- **Email:** [safiyakhalid.bus@gmail.com](mailto:safiyakhalid.bus@gmail.com)
- **LinkedIn:** [linkedin.com/in/safiya-khalid/](https://www.linkedin.com/in/safiya-khalid/)

## Acknowledgments

- Special thanks to the [Blynk community](https://community.blynk.cc/) for their support and resources.
```
