import cv2
from pyzbar import pyzbar


def scan(filename="picture.jpg"):
    print("Scanning image for barcodes...")

    image_path = f"pictures/{filename}"
    print(f"Reading image from {image_path}...")

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    barcodes = pyzbar.decode(image)

    print("Barcodes:")
    for barcode in barcodes:
        print(barcode.data.decode("utf-8"))


if __name__ == "__main__":
    scan("test_barcode.jpg")
