from picamera2 import Picamera2, Preview
import time


camera = Picamera2()


def init():
    print("Starting camera...")
    camera_config = camera.create_still_configuration()
    camera.configure(camera_config)
    camera.start_preview(Preview.NULL)
    camera.start()
    time.sleep(2)


def take_picture(filename="picture"):
    print("Taking picture...")
    camera.capture_file(f"pictures/{filename}.jpg")

if __name__ == "__main__":
    init()
    take_picture()

