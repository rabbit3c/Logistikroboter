import os
from picamera2 import Picamera2, Preview
from libcamera import Transform
import time


os.environ["LIBCAMERA_LOG_LEVELS"] = "ERROR" # remove libcamera logs from output

camera = Picamera2()


def init():
    print("Starting camera...")
    transform = Transform(vflip = True, hflip = True) # flipping image vertically and horizontally
    camera_config = camera.create_still_configuration(transform=transform)
    camera.configure(camera_config)
    camera.start_preview(Preview.NULL) 
    camera.start()
    time.sleep(2) 


def take_picture(filename="picture"):
    print("Taking picture...")
    camera.autofocus_cycle()
    camera.capture_file(f"pictures/{filename}.jpg")


def stop():
    camera.stop()


if __name__ == "__main__":
    init()
    take_picture()

