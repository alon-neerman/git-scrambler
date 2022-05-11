
from M172.Client import Client as M172Client

class PLC(object):
  def __init__(self, plc_name, host, port, require_setup=False):
    if plc_name == 'M172':
      self.PLC = M172Client(host, port)
  
  def connected(self):
    return self.PLC.connected()
  
  def read_analog_input(self, num):
    return self.PLC.read_analog_input(num)
  
  def read_digital_input(self, num):
    return self.PLC.read_digital_input(num)
  
  def write_digital_output(self, num, value):
    self.PLC.write_digital_output(num, value)

  def read_digital_output(self, num):
    return self.PLC.read_digital_output(num)

  def write_analog_output(self, num, value):
    self.PLC.write_analog_output(num, value)

  def read_analog_output(self, num):
    return self.PLC.read_analog_output(num)

  def write_PWM_config(self, num, value):
    self.PLC.write_PWM_config(num, value)



  #  #  The following functions encapsulate the above functions, which are interface functions of GUI screen
  #  # 1.Power
#
  #  def read_battery_voltage(self):
  #      return self.read_analog_input(3)
#
  #  def control_port(self, num, value):
  #      self.write_digital_output(num, value)
  #  # 2.Directions
  #  def dir_control_up(self, num, value):
  #      self.write_digital_output(num, value)
  #  
  #  def dir_control_down(self, num, value):
  #      self.write_digital_output(num, value)
  #  
  #  def dir_control_left(self, num, value):
  #      self.write_digital_output(num, value)
  #  
  #  def dir_control_right(self, num, value):
  #      self.write_digital_output(num, value)
#
  #  # 5.Read Selected Port
  #  def f_read(self, num, value):
  #      return self.read_digital_input(num,value)
  #  # 6.Enter Data
  #  def f_write(self, num, value):
  #      self.write_digital_output(num, value)
