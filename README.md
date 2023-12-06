# Air Mouse - Fingers

## Project Overview

The Air Mouse - Fingers project involves the creation of a gesture-controlled mouse using a combination of accelerometers, gyroscopes, a real-time clock (RTC), and an SD card module. The goal is to allow users to control their computer's mouse cursor by moving their fingers in the air, creating patterns and gestures for various actions.

### Hardware Components

- 2 Accelerometers with Gyroscopes
- Real-Time Clock (RTC)
- SD Card Module

### Interface

The communication with the PC is established through USART/UART, using a USB connection.

## Features

1. **Finger-Based Mouse Control:**
   - Utilize finger movements to replicate traditional mouse actions (up/down - left/right).
   - Enable clicks and double clicks through specific finger gestures.
   - (Optional) Implement left and right-click functionalities.

2. **Gesture Design:**
   - Collaboratively design mouse gestures using two fingers.
   - Examples of gestures include zoom in/out, ALT-TAB, and more.

3. **Calibration:**
   - Develop a calibration process using software (typically available on operating systems) to ensure accurate and responsive air mouse movements.

4. **Communication Protocol:**
   - Design a robust communication protocol from the STM32-Air mouse to the PC for seamless interaction.

5. **Interface Design:**
   - Create proper interfaces to buses, ensuring efficient data transfer between components.

6. **Event Logging:**
   - Log each event, such as movements, with the following information:
     - Timestamp obtained from the RTC.
     - Write a codified representation of the event to the SD card (e.g., [from:(x,y,z); to:(x,y,z); accel: (x,y,z); gyro: (x,y,z)]).

7. **Task Management:**
   - Implement different tasks for various activities, such as logging, sensor inputs, etc.
   - Utilize FreeRTOS for task scheduling, potentially under real-time constraints.
