# -*- coding=utf-8 -*-
# module is for GUI frame 
import sys
from PLC import PLC
import wx
import subprocess

connected = False

class Login_Frame(wx.Frame):
    def __init__(self, parent, id):
        # Initialize Window
        wx.Frame.__init__(self, parent, id, title='Login Window', size=(800, 600), pos=(100, 100))
        # Initialize Canvas
        panel = wx.Panel(self)
        # Set Background
        image_file = r'login_background.jpg'
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        image_width = to_bmp_image.GetWidth()
        image_height = to_bmp_image.GetHeight()
        # Set Front
        # Title Front
        font1 = wx.Font(pointSize=20, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        # Normal Text Front
        font2 = wx.Font(pointSize=15, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        font3 = wx.Font(pointSize=10, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        
        
        self.plctype_list = ["","M172"]
        self.plctype_lable = wx.StaticText(self.bitmap, label='PLC Type:', pos=(20, 80))
        self.plctype_lable.SetFont(font2)
        self.plctype_cb = wx.ComboBox(self.bitmap, value=' ', pos=(105,75), choices=self.plctype_list, style=2)
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox_plctype, self.plctype_cb)

        self.ip_address_label = wx.StaticText(self.bitmap, label='IP Address:', pos=(200, 80))
        self.ip_address_label.SetFont(font2)
        self.ip_address_text = wx.TextCtrl(self.bitmap, pos=(290, 75), size=(100,30))
        self.plc_port_label = wx.StaticText(self.bitmap, label='Port:', pos=(400, 80))
        self.plc_port_label.SetFont(font2)
        self.plc_port_list = ["","502"]
        self.plc_port_cb = wx.ComboBox(self.bitmap, value=' ', pos=(450,75), choices=self.plc_port_list,style=2)
        self.Bind(wx.EVT_COMBOBOX, self.on_plc_port_cb, self.plc_port_cb)

        self.connect_button = wx.Button(self.bitmap, label="CONNECT", size=(100, 30), pos=(565,75))
        
        # PLC Type Selection
        self.plc_type = None

        # Port Selection
        self.port = None
        self.plc_port = None
        # Instantiation of PLC class

        # Bind button event
        # Connection Port
        self.connect_button.Bind(wx.EVT_BUTTON, self.connect_plc)

    def connect_plc(self, event):
        client_type = self.plc_type
        client_address = self.ip_address_text.GetValue()
        client_port = self.plc_port
        global client 
        client = PLC(client_type,client_address,client_port)
        if client.connected():
            print("Client Connected")
            global connected
            connected = True
            self.Destroy()
        if not client.connected():
            print("Unable to Connect")

    def on_combobox_plctype(self, event):
        self.plc_type = event.GetString()

    def on_plc_port_cb(self, event):
        self.plc_port = event.GetString()




class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        # Initialize Window
        wx.Frame.__init__(self, parent, id, title='PLC-ROBOT-GUI-DESIGNE', size=(800, 600), pos=(100, 100))
        # Initialize Canvas
        panel = wx.Panel(self)
        # Set Background
        image_file = r'main_background.jpg'
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        image_width = to_bmp_image.GetWidth()
        image_height = to_bmp_image.GetHeight()
        # Set Front
        # Title Front
        # Normal Text Front
        font2 = wx.Font(pointSize=15, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        font3 = wx.Font(pointSize=10, family=wx.SWISS, style=wx.NORMAL, weight=wx.BOLD)
        self.client = client
        
        # Power Switch
        #self.power_label = wx.StaticText(self.bitmap, label='Power', pos=(620, 20))
        #self.power_label.SetFont(font=font3)
        #self.power_port_button = wx.Button(self.bitmap, label="ON/OFF", size=(80, 20), pos=(660, 16))
        #self.power_port_button.SetFont(font=font3)

        
        
        #self.select_port_label = wx.StaticText(self.bitmap, label='Select Port:', pos=(20, 180))
        #self.select_port_label.SetFont(font=font2)
        #self.select_port_label.Enable = False
        # Set a list of 8 ports
        #self.port_list = ['port'+str(i) for i in range(8)]
        #self.cb1 = wx.ComboBox(self.bitmap, value='ports', pos=(155,180), choices=self.port_list,style=2)
        # Set event as combobox
        #self.Bind(wx.EVT_COMBOBOX, self.on_combobox, self.cb1)

        # Barcode Scanner
        self.barcode_lable = wx.StaticText(self.bitmap, label='Bar-code:', pos=(20, 240))
        self.barcode_lable.SetFont(font2)
        self.barcode_text = wx.TextCtrl(self.bitmap, pos=(120, 240), size=(300,30))
        self.barcode_button = wx.Button(self.bitmap, label="SCAN:", size=(100, 30), pos=(450, 240))
        
        # Enter Data to Selected Port
        #self.write_portdata_label = wx.StaticText(self.bitmap, label='write-data:', pos=(370, 300))
        #self.write_portdata_label.SetFont(font2)
        #self.write_portdata_text = wx.TextCtrl(self.bitmap, pos=(491, 300), size=(100,30))
        #self.write_portdata_button = wx.Button(self.bitmap, label="Enter", size=(101, 30), pos=(600, 300))
        
        # Leave Blank with IMU
        #self.imu_label = wx.StaticText(self.bitmap, label='IMU:', pos=(20, 400))
        #self.imu_label.SetFont(font2)
        #self.imu_text = wx.TextCtrl(self.bitmap, pos=(80, 400), size=(100,30))
        #self.imu_button = wx.Button(self.bitmap, label="IMU", size=(100, 30), pos=(180, 400))
        
        # Read Battery Voltage
        self.battery_label = wx.StaticText(self.bitmap, label='Battery Voltage:', pos=(20, 450))
        self.battery_label.SetFont(font2)
        self.battery_text = wx.TextCtrl(self.bitmap, pos=(145, 440), size=(100,30))
        self.battery_button = wx.Button(self.bitmap, label="Read Voltage", size=(100, 30), pos=(260, 440))


        # Direction Control
        # self.dir_control_label = wx.StaticText(self.bitmap, label='DIRECTION CONTROL', pos=(600, 500))
        # self.dir_control_label.SetFont(font2)
        self.dir_control_up_bt = wx.Button(self.bitmap, label="FORWARD", size=(100, 30), pos=(580, 450))
        self.stop_robot = wx.Button(self.bitmap, label="STOP", size=(100, 30), pos=(580, 485))

        self.dir_control_down_bt = wx.Button(self.bitmap, label="BACKWARD", size=(100, 30), pos=(580, 525))
        self.dir_control_left_bt = wx.Button(self.bitmap, label="ROTATE LEFT", size=(100, 30), pos=(480, 500))
        self.dir_control_right_bt = wx.Button(self.bitmap, label="RIGHT", size=(100, 30), pos=(680, 500))
        

        # Bind button event
        # Power Port
        #self.power_port_button.Bind(wx.EVT_BUTTON, self.power_port)
        # Direction Control
        # Upward
        self.dir_control_up_bt.Bind(wx.EVT_BUTTON, self.go_forward)
        # Downward
        self.dir_control_down_bt.Bind(wx.EVT_BUTTON, self.go_backward)
        # Leftward
        self.dir_control_left_bt.Bind(wx.EVT_BUTTON, self.dir_left)
        # Rightward
        self.dir_control_right_bt.Bind(wx.EVT_BUTTON, self.dir_right)
        # Stop
        self.stop_robot.Bind(wx.EVT_BUTTON, self.stop)
        # Barcode Scanner
        self.barcode_button.Bind(wx.EVT_BUTTON, self.scan_code)
        # Read Port Data
        #self.read_portdata_button.Bind(wx.EVT_BUTTON, self.read_portdata)
        # Write Port Data
        #self.write_portdata_button.Bind(wx.EVT_BUTTON, self.write_portdata)
        # IMU
        #self.imu_button.Bind(wx.EVT_BUTTON, self.imu)
        # Battery Voltage
        self.battery_button.Bind(wx.EVT_BUTTON, self.read_battery)

    # Select from Drop-down Combobox
    def on_combobox(self,event):
        self.port = event.GetString()
        #print(self.port)
    

    # Power Switch
    def power_port(self,event):
        num = None  # Change to Port Switch's Address
        value = None # Change to Port Switch's Status, same below
        self.plc.control_port(num,value)
        # print function is for testing
        print("Power Button Triggered")


    def read_battery(self, event):
        battery_voltage = self.client.read_analog_input(7) * 3.9
        self.battery_text.ChangeValue(str(round(battery_voltage, 1)))

    # Control direction up
    def go_forward(self, event):

        # Reset digital outputs
        self.stop

        # Sets Duty Cycle to 55%
        self.client.write_analog_output(1, 550)
        self.client.write_analog_output(2, 550)


        # Turns on forward functionality
        self.client.write_digital_output(1, 1)
        self.client.write_digital_output(5, 1)
        print("UP Button Triggered")

    # Control direction down
    def go_backward(self, event):
        
        # Reset digital outputs
        self.stop

        # Sets Duty Cycle to 55%
        self.client.write_analog_output(1, 550)
        self.client.write_analog_output(2, 550)
        
        # Turns off forwards functionality
        self.client.write_digital_output(1, 0)
        self.client.write_digital_output(5, 0)

        # Turns on backwards functionality
        self.client.write_digital_output(2, 1)
        self.client.write_digital_output(6, 1)
        print("DOWN Button Triggered")

    def stop(self, event):

        # Turns off all digital outputs
        self.client.write_digital_output(1, 0)
        self.client.write_digital_output(2, 0)

        self.client.write_digital_output(5, 0)
        self.client.write_digital_output(6, 0)

    # # Control direction left
    def dir_left(self, event):

        # Reset digital outputs
        self.stop

        # Set right wheels to 40% duty cycle
        self.client.write_analog_output(1, 400)

        # Set left wheels to 60% duty cycle 
        #self.client.write_analog_output(2, 600)

        # Right wheels go forward
        self.client.write_digital_output(1, 1)

        # Left wheels go backwards
        #self.client.write_digital_output(6, 1)

        print("LEFT Button Triggered")

    # # Control direction right
    def dir_right(self, event):

        # Reset digital outputs
        self.stop
        
        # Set right wheels to 60% duty cycle
        #self.client.write_analog_output(1, 550)

        # Set left wheels to 20% duty cycle 
        self.client.write_analog_output(2, 300)

        # Left wheels go forward
        self.client.write_digital_output(5, 1)

        # Right wheels go backwards
        #self.client.write_digital_output(2, 1)
        print("RIGHT Button Triggered")
    
    def scan_code(self, event):
        subprocess.call(["rsync", "-ve", "ssh", "pi@10.0.0.227:/home/pi/barcode_data.txt", "."])
        with open('barcode_data.txt', 'r') as f:
            last_line = f.readlines()[-1]
        self.barcode_text.ChangeValue(str(last_line))

        print("SCAN Button Triggered")
    
    
    def write_portdata(self, event):
        num = None
        value = self.write_portdata_text.GetValue()
        self.plc.f_write(num, value)
        print("WRITE DATA Button Triggered")

    def imu(self, event):
        print("Reserved Port")


def going():
    try:
        app = wx.App()
        while connected is False:
            frame = Login_Frame(None, -1)
            frame.Show()
            app.MainLoop()
        
        frame = MyFrame(None, -1)
        frame.Show()
        app.MainLoop()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    going()

