# Laser Pointer Detection

This project uses OpenCV to detect and track a red laser pointer in real-time using a webcam. It captures each frame, filters for a specified range of red colors in HSV space, and identifies contours matching the color of the laser pointer. When the laser pointer is detected, the program draws a green circle around it and displays its coordinates.

## Features
- Real-time red laser pointer detection
- Circle overlay and coordinate display on detected laser spots
- Adjustable HSV color range for tuning to different laser pointer colors

## Requirements
- Python 3.x
- OpenCV library
- Numpy library

## Installation

1. **Clone the repository:**
   https://github.com/msc0v0/detect-a-laser-pointer_winter-hack
   ```bash
   pip install opencv-python-headless numpy
   python import cv2.py
## Usage
- Make sure your webcam is connected.
- Run the script as shown in the installation instructions.
- The live video feed from your webcam will appear.
- Point a red laser at the camera view; the program will detect it, draw a green circle around it, and show its coordinates.

## Adjusting HSV Range
If the laser pointer is not detected accurately, adjust the HSV range in the script:

```python
lower_red = np.array([160, 100, 100])
upper_red = np.array([179, 255, 255])
```
## Exiting the Program
To close the program, press 'q' on the keyboard in the video window.

## License
This project is licensed under the MIT License.

## Acknowledgements
- OpenCV for powerful computer vision tools.
- Numpy for efficient array handling.






   
   
   
   
