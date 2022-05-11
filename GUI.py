#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import os
from PLC import PLC
import PySimpleGUI as sg

connected = False

while(connected is False):


    layout = [       [sg.Text('Please enter the PLC Name you want to use: ')],      
                     [sg.Combo(['M172'], key='-PLC-')],
                     [sg.Text('Please enter the IP Address you want to access ')],
                     [sg.InputText(key='-IP-')],
                     [sg.Text('Please enter the port of the device ')],
                     [sg.InputText(key='-Port-')],
                     [sg.Submit(button_text="Connect"), sg.Exit()]]      
    window = sg.Window('PLC Project', layout)    
    event, values = window.read()    
    window.close()

    if(event == sg.WIN_CLOSED or event == "Exit"):exit()

    PLC_name = values['-PLC-']    
    IP_Addr = values['-IP-']
    Port = values['-Port-']
    client = PLC(plc_name=PLC_name, host=IP_Addr, port=Port)
    if client.connected():connected = True

while connected is True:

    Welcome_message = "You are accessing the " + PLC_name + ' controller on ' + IP_Addr + ':' + Port

    layout = [      
                    [sg.Text(Welcome_message)],
                    #[sg.Image(r'/Users/alonneerman/image.png')],
                    [sg.Text('Please select the function to use')],
                    [sg.Combo(['read_analog_input', 'read_digital_input', "write_digital_output", "read_digital_output", "write_pwm_signal"], key='-function-')],
                    [sg.Text('Please enter the IO port you want to access ')],
                    [sg.InputText(key='-IO-')],
                    [sg.Text('(For digital output only!!) Relay on or off?')],
                    [sg.Combo(['on', 'off'], key='-Relay-')],
                    [sg.Text('(For PWM signal only!!) Frequency Range 0-2000Hz')],
                    [sg.InputText(key='-Frequency-')],
                    [sg.Text('(For PWM signal only!!) PWM Duty Cycle 0-100%')],
                    [sg.InputText(key='-PWM-')],
                    [sg.Submit(), sg.Exit()]] 

    window = sg.Window('PLC Project', layout)    

    event, values = window.read()    
    window.close()

    if(event == None or event == "Exit"):exit()

    function = values['-function-']
    IO = values['-IO-']
    PWM = values['-PWM-']
    Frequency = values['-Frequency-']
    Relay = values['-Relay-']
    if(Relay == "on"):
        Relay = 1
    else:
        Relay = 0

    if function == "read_analog_input":
        result = client.read_analog_input(int(IO))
        sg.popup(f"{result}V on port {IO}")
    elif function == "read_digital_input":
        result = client.read_digital_input(int(IO))
        sg.popup(f"Digital input {IO} is {result}")
    elif function == "write_digital_output":
        client.write_digital_output(int(IO), int(Relay))
        result = client.read_digital_output(int(IO))
        sg.popup(f"Digital output {IO} is {result}")
    elif function == "read_digital_output":
        result = client.read_digital_output(int(IO))
        sg.popup(f"Digital output {IO} is {result}")

    elif function == "write_pwm_signal":
        client.write_PWM_config(1, int(Frequency))
        PWM = int(PWM) * 10
        client.write_analog_output(int(IO), int(PWM))
        result = client.read_analog_output(int(IO))
        sg.popup(f"Analog output {IO} is set to {Frequency}Hz at a {result}% Duty Cycle")

    else:
        result = "Invalid function"

