import json


data = None
items = []


# Load persistent data from data.json
def get():
    global data
    f = open("data/data.json")
    data = Data(json.load(f))


# Save data persistently
def save():
    json_data = json.dumps(data.data(), indent=4)
    with open("data/data.json", "w") as f:
        f.write(json_data)


# Convert array to tuple
def array_to_tuple(array):
    return (int(array[0]), int(array[1]))


# Data class
class Data():
    position = None


    # initialize data class
    def __init__(self, data) -> None:
        self.start_position = array_to_tuple(data["start_position"])
        self.start_direction = array_to_tuple(data["start_direction"])
        self.delivery_position = array_to_tuple(data["delivery_position"])
        self.delivery_direction = array_to_tuple(data["delivery_direction"])
        pass


    # return data as a dictionary
    def data(self):
        return {
            "start_position": self.start_position,
            "start_direction": self.start_direction,
            "delivery_position": self.delivery_position,
            "delivery_direction": self.delivery_direction
        }

