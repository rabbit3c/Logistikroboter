import os
from picamera2 import Picamera2, Preview
from libcamera import Transform
import time


os.environ["LIBCAMERA_LOG_LEVELS"] = "ERROR" # remove libcamera logs from output

camera = Picamera2()


# Initialize camera to be able to take images
def init():
    print("Starting camera...")
    transform = Transform(vflip = True, hflip = True) # flipping image vertically and horizontally
    camera_config = camera.create_preview_configuration(transform=transform)
    camera.configure(camera_config)
    camera.start_preview(Preview.NULL) # no preview
    camera.start()
    time.sleep(2)
    print("\33[32mCamera started\33[0m\n")


# Take a picture with the camera
def take_picture(filename="picture"):
    camera.autofocus_cycle()
    camera.capture_file(f"pictures/{filename}.jpg")


if __name__ == "__main__":
    init()
    take_picture()

