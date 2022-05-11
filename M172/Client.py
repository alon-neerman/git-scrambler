
from pyModbusTCP.client import ModbusClient
from IO import IO

class Client(object):
  def __init__(self, host, port, requires_setup=False):
    if requires_setup:
      self.setup_client()
    
    self.client = ModbusClient()
    self.client.host(host)
    self.client.port(port)
    self.client.timeout(2)
    self.client.open()

    self.ANALOG_IN = [IO(self.client, num + 1, 8335 + num) for num in range(8)]
    self.ANALOG_OUT = [IO(self.client, num + 1, 8447 + num) for num in range(2)]
    self.DIGITAL_IN = [IO(self.client, num + 1, 8191 + num) for num in range(2)]
    self.DIGITAL_OUT = [IO(self.client, num + 1, 8527 + num) for num in range(6)]
    self.PWM_CONFIG = [IO(self.client, num + 1, 15768 + num) for num in range(1)]

  def setup_client(self):
    return
  
  def connected(self):
    if self.client.is_open():
      return True
    else:
      return False

  def read_analog_input(self, num):
    if num > len(self.ANALOG_IN):
      raise Exception('Analog input out of range')
    io = [x for x in self.ANALOG_IN if x.num == num][0]
    return io.find_value() / 100

  def read_digital_input(self, num):
    if num > len(self.DIGITAL_IN):
      raise Exception('Digital input out of range')
    io = [x for x in self.DIGITAL_IN if x.num == num][0]
    return bool(io.find_value())
  
  def write_digital_output(self, num, value):
    if num > len(self.DIGITAL_OUT):
      raise Exception('Digital output out of range')
    io = [x for x in self.DIGITAL_OUT if x.num == num][0]
    io.write_value(value)

  def read_digital_output(self, num):
    if num > len(self.DIGITAL_OUT):
      raise Exception('Digital output out of range')
    io = [x for x in self.DIGITAL_OUT if x.num == num][0]
    return bool(io.find_value())

  def write_analog_output(self, num, value):
    if num > len(self.ANALOG_OUT):
      raise Exception('Analog output out of range')
    io = [x for x in self.ANALOG_OUT if x.num == num][0]
    io.write_value(value)

  def read_analog_output(self, num):
    if num > len(self.ANALOG_OUT):
      raise Exception('Analog output out of range')
    io = [x for x in self.ANALOG_OUT if x.num == num][0]
    return io.find_value() / 10

  def write_PWM_config(self, num, value):
    if num > len(self.PWM_CONFIG):
      raise Exception('PWM output out of range')
    if value > 2000 or value < 0:
      raise Exception('PWM frequency out of range')
    io = [x for x in self.PWM_CONFIG if x.num == num][0]
    io.write_value(value)