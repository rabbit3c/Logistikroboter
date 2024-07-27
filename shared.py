from threading import Event

# event to stop the robot gracefully
stop_event = Event()

# event to stop robot immediately
emergency_stop_event = Event()