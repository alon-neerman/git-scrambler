

class IO(object):
  def __init__(self, client, num, address):
    self.client = client
    self.num = num
    self.address = address
  
  def find_value(self):
    return self.client.read_holding_registers(self.address, 1)[0]
  
  def write_value(self, value):
    if not self.client.write_multiple_registers(self.address, [value]):
      raise Exception('Could not write output')
    
