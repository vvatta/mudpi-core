import adafruit_mcp3xxx.mcp3008 as MCP


# Base sensor class to extend all other mcp3xxx sensors from.
class Sensor:

    PINS = {
        '0': MCP.P0,
        '1': MCP.P1,
        '2': MCP.P2,
        '3': MCP.P3,
        '4': MCP.P4,
        '5': MCP.P5,
        '6': MCP.P6,
        '7': MCP.P7,
    }

    def __init__(self, pin: int, mcp, name='Sensor', key=None):
        self.pin = pin
        self.mcp = mcp
        self.channel = None

        self.name = name
        self.key = key.replace(" ", "_").lower() if key is not None else self.name\
            .replace(" ", str(pin))

    def init_sensor(self):
        """
        Initialize the sensor here (i.e. set pin mode, get addresses, etc)
        :return:
        """
        raise NotImplementedError

    def read(self):
        """
        Read the sensor(s), parse the data and store it in redis if redis is configured
        :return:
        """
        raise NotImplementedError

    def readRaw(self):
        """
        Read the sensor(s) but return the raw voltage, useful for debugging
        :return:
        """
        return self.channel.voltage

    def readPin(self):
        """ Read the pin from the MCP3xxx as unaltered digital value"""
        return self.channel.value
