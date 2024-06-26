import serial
from time import sleep

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.reset_input_buffer()

def communication_test():
    print("Testing communication...")

    arduino.reset_input_buffer()
    arduino.write("_".encode())
    arduino.write("communication test".encode())
    sleep(0.1)

    if confirmation():
        print("\033[32mArduino is available and ready to receive commands\033[0m\n")
        return True
    
    print("\033[31mArduino not reachable\033[0m")
    sleep(1)
    print("Retrying...")
    communication_test()


def send_command(command):
    # print(f"Sending command: \"{command}\"")
    arduino.write(f"{command}\n".encode())
    return confirmation()


def set_speed(speed):
    print("Setting speed...\n")
    arduino.reset_input_buffer()
    arduino.write(f"v{speed:03d}".encode())
    sleep(0.1)

    if not confirmation():
        communication_test()
        set_speed(speed)


def confirmation():
    answer = arduino.readline().decode('utf-8').rstrip()
    return answer == "ok"
