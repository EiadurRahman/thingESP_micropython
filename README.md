# MicroPython Library: ThingESP Client

The ThingESP Client library facilitates easy communication with the ThingESP platform using MQTT for IoT projects on MicroPython-based microcontroller boards. It allows you to interact with the ThingESP platform, subscribe to messages, and perform actions based on received messages.

## Installation

1. Ensure your MicroPython environment is set up on your microcontroller board.
2. Copy the `thingesp_client.py` file to your project directory.

## Usage

```python
import ThingESP
thing = ThingESP.Client('user_name', 'project_name', 'password')
ThingESP.send_msg('device is back online ')

# this function handles query, add conditions to trigger certain tasks
def handleResponse(query):
    if query == 'are you up?':
        return 'Iam up!'

    else:
        return 'no task is set for [%s]'%query


thing.setCallback(handleResponse).start()

print('END_TASK')


```

## API Reference

### `Client(username, projectName, password)`

Creates a ThingESP client instance.

- `username`: Your ThingESP username.
- `projectName`: The name of your project on ThingESP.
- `password`: Your ThingESP password.

### `setCallback(func)`

Sets the callback function to handle incoming messages.

- `func`: The callback function. It should accept a single argument (the query) and return a response.

### `start()`

Starts the client, listening for messages from ThingESP.

### `device_call(to_num, msg)`

Sends a message from your ESP module to a specified number.

- `to_num`: The recipient's phone number.
- `msg`: The message to send.

## Independent Message Sending

The `send_msg(msg)` function allows you to send messages independently, without relying on the ThingESP server. This function utilizes the Twilio API for sending WhatsApp messages.

```python
from thingesp_client import send_msg

# Send a message
send_msg("Hello from your ESP!")
```

## Contributions

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request on github.
