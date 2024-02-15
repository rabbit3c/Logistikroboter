from line_sensor import *
import serial

def main():
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    arduino.reset_input_buffer()
    print("Starting...")

    while(True):
        if (line_left()):
            arduino.write("left\n".encode())
        elif (line_right()):
            arduino.write("right\n".encode())
        else:
            arduino.write("forward\n".encode())

if __name__ == "__main__":
    main()