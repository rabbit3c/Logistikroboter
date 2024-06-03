import barcode
import camera
import time


def scan():
    print("Scanning for barcode...")
    camera.init()
    result = ""

    # take pictures and try to read a barcode until barcode is found
    while True:
        camera.take_picture()
        result = barcode.read()

        if not result:
            continue

        if len(result) == 6:
            camera.stop()
            break
        
        time.sleep(1)

    point = barcode.decode(result)
    return point


if __name__ == "__main__":
    scan()
    