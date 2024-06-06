import json


data = None


def get():
    global data
    f = open("data/data.json")
    data = Data(json.load(f))


def save():
    json_data = json.dumps(data.data(), indent=4)
    with open("data/data.json", "w") as f:
        f.write(json_data)


def array_to_tuple(array):
    return (array[0], array[1])


class Data():
    position = None

    def __init__(self, data) -> None:
        self.start_position = array_to_tuple(data["start_position"])
        self.start_direction = array_to_tuple(data["start_direction"])
        pass

    def data(self):
        return {
            "start_position": self.start_position,
            "start_direction": self.start_direction
        }

