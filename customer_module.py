#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
from PLC import PLC
import time
import sys
import argparse

def main():


  parser = argparse.ArgumentParser()
  parser.add_argument('plc_name')
  parser.add_argument('host')
  parser.add_argument('port')

  args = parser.parse_args()
  try:
    client = PLC(plc_name=args.plc_name, host=args.host, port=args.port)
  except:
    print("Wrong PLC")

  while True:

    while True:

    print("\nWhat function would you like to use from the list:")
    print("\t1: read_analog_input")
    print("\t2: read_digital_input")
    print("\t3: write_analog_output")
    print("\t4: write_digital_output")
    print("\t5: read_digital_output")

    print("\t6: exit")

    function = input("What function would you like to use : ")
    if function == "6" or function == "exit":exit()

    IO_Port = input("What IO Port would you like to access : ")

    if function == "1" or function == "read_analog_input":
      print(f'\nValue: {client.read_analog_input(int(IO_Port))}')
    elif function == "2" or function == "read_digital_input":
      print(f'\nValue: {client.read_digital_input(int(IO_Port))}')
    elif function == "3" or function == "write_analog_output":
      print("\nFunction not supported yet")
    elif function == "4" or function == "write_digital_output":
      IO_Value = input("Would you like to turn the relay on or off? ")
      if IO_Value == "on": IO_Value=1
      elif IO_Value == "off": IO_Value=0
      else:
        print("\nInvalid Input")
        exit()
      
      client.write_digital_output(int(IO_Port), IO_Value)
      print(f'\nRelay {IO_Port} is now: {client.read_digital_output(int(IO_Port))}')

    elif function == "5" or function == "read_digital_output":
      print(f'\nRelay {IO_Port} is: {client.read_digital_output(int(IO_Port))}')
      
    else:
      print("\nYou have selected an invalid option")


if __name__ == '__main__':
    main()