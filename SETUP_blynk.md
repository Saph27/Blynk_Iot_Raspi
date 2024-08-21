# Blynk Setup on Raspberry Pi

## Prerequisites
- A Raspberry Pi with Raspberry Pi OS installed.
- An active internet connection.
- Blynk app installed on your smartphone (available on iOS and Android) with an active Blynk account.

## Initial Blynk Setup

### Download and Extract Blynk Library

1. **Download the Blynk Library:**
   - Go to [Blynk GitHub Releases](https://github.com/blynkkk/blynk-library/releases).
   - Download the latest version of Blynk library for Linux (`BlynkLin.zip`).

2. **Extract the Blynk Library:**
   - Extract the ZIP file using a file manager or terminal. In a terminal, navigate to the download location and run:
     ```bash
     unzip BlynkLin.zip
     ```

3. **Install Dependencies:**
   - Ensure you have `git` and `python3` installed. Install the necessary Python packages:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pip
     pip3 install blynk-library
     ```

4. **Set Up Blynk on Raspberry Pi:**
   - Copy the Blynk library files to your project directory or follow the specific instructions provided in the Blynk documentation.

### Blynk Project Setup

1. **Create a New Project in Blynk App:**
   - Open the Blynk app and create a new project.
   - Select your device type as **Raspberry Pi**.
   - Choose **Connection Type** (e.g., WiFi).

2. **Add Widgets and Configure Datastreams:**
   - Add the necessary widgets (e.g., Button) to control the LED.
   - Configure the datastreams and obtain your **Auth Token**.

3. **Update Auth Token:**
   - Copy the Auth Token from the Blynk app and use it in your code as specified in the project instructions.

For more detailed setup, refer to the Blynk documentation or community resources.

