import cv2
from pyzbar import pyzbar


# Reading a barcode
def read(filename="picture.jpg"):
    image_path = f"pictures/{filename}"

    # load image
    image = cv2.imread(image_path)
    if image is None:
        raise Exception(f"Error: Unable to load image at {image_path}")

    # read barcodes from image
    barcodes = pyzbar.decode(image)

    # decode barcodes and return correct barcode
    for barcode in barcodes:
        data = barcode.data.decode("utf-8")

        # if the data of the barcode has the right length return it to start navigation
        if data is None:
            continue
        if len(data) == 6: 
            return data
        
    return False
        
# Decode barcode in the needed values
def decode(string):
    y = int(string[:2]) # take first to characters
    x = int(string[2:4]) # take two middle characters
    h = int(string[4:]) # take last two characters

    point = (x, y)

    print("\033[32mBarcode successfully read & decoded: \033[0m")
    print(f"Destination: Point \033[31m{point}\033[0m at height {h}\n")
    return point


if __name__ == "__main__":
    read()
