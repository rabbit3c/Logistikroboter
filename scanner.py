import barcode
import camera
import time


def scan():
    print("\033[33mScanning for barcode...\033[0m")
    print("\033[33mTaking pictures...\033[0m\n")
    result = ""

    # take pictures and try to read a barcode until barcode is found
    while True:
        camera.take_picture()
        result = barcode.read()

        if not result:
            continue

        if len(result) == 6:
            break

    point = barcode.decode(result)
    return point


if __name__ == "__main__":
    camera.init()
    scan()
    