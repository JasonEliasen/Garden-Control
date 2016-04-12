import tkinter
import time
import socket
import sys
import threading

#connection_status = tkinter.StringVar()

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("failed to create socket")
    sys.exit()


class Valve:

    def __init__(self, pin, location):
        self.pin = pin
        self.location = location

    timer = 0
    status = False
    auto = False

    def turn_on(self):
        self.status = True
        self.send_info()

    def turn_off(self):
        self.status = False
        self.send_info()

    def set_timer(self, minutes):
        self.timer = minutes * 60

    def initiate(self):
        if self.timer > 0:
            self.auto = True
            self.turn_on()
            while self.timer > 0:
                print(self.timer)
                self.timer -= 1
                time.sleep(1)
            if self.auto is True:
                self.turn_off()
        elif self.timer == 0 and self.status is False:
            self.auto = False
            self.turn_on()
        elif self.timer == 0 and self.status is True:
            self.auto = False
            self.turn_off()

    def start(self):
        thread = threading.Thread(target=self.initiate)
        thread.start()

    def send_info(self):
        message_to_send = str(self.pin) + " " + str(self.status)
        encoded_message_to_send = str.encode(message_to_send)
        print(encoded_message_to_send)
        my_socket.sendall(encoded_message_to_send)


class Connection:

    def __init__(self):
        self.ip_address = ""
        self.port_address = ""
        self.connection_established = False

    def connect(self):
        try:
            self.connection_established = True
            my_socket.connect((self.ip_address, self.port_address))
            # connection_status.set("connected to: " + str(self.ip_address) + " " + str(self.port_address))
            print("Connected to:", self.ip_address)
            print(my_socket)

        except:
            #connection_status.set("failed to connect to: " + str(self.ip_address) + " " + str(self.port_address))
            print("Not connected!")
            self.connection_established = False

    # def disconnect(self):


root = tkinter.Tk()




# functions for buttons
def start1():
    if len(timer1.get()) != 0:
        hose1.set_timer(0)
        time.sleep(1.1)
        timer_1_entry = int(timer1.get())
        hose1.set_timer(timer_1_entry)
    if len(timer1.get()) == 0:
        timer_1_entry = 0
        hose1.set_timer(timer_1_entry)
    hose1.start()


def start2():
    if len(timer2.get()) != 0:
        hose2.set_timer(0)
        time.sleep(1.1)
        timer_2_entry = int(timer2.get())
        hose2.set_timer(timer_2_entry)
    if len(timer2.get()) == 0:
        timer_2_entry = 0
        hose2.set_timer(timer_2_entry)
    hose2.start()


def start3():
    if len(timer3.get()) != 0:
        hose3.set_timer(0)
        time.sleep(1.1)
        timer_3_entry = int(timer3.get())
        hose2.set_timer(timer_3_entry)
    if len(timer3.get()) == 0:
        timer_3_entry = 0
        hose3.set_timer(timer_3_entry)
    hose3.start()


def start4():
    if len(timer4.get()) != 0:
        hose4.set_timer(0)
        time.sleep(1.1)
        timer_4_entry = int(timer4.get())
        hose4.set_timer(timer_4_entry)
    if len(timer4.get()) == 0:
        timer_4_entry = 0
        hose4.set_timer(timer_4_entry)
    hose4.start()


# create class objects
hose1 = Valve(9, 'Garden')
hose2 = Valve(27, 'Lawn')
hose3 = Valve(22, 'Patio')
hose4 = Valve(10, 'Front')

pi = Connection()


# GUI layout
def setup_window():
    # create host object and connect function from object's class
    def connect_button():
        pi.ip_address = str(ip_entry.get())
        pi.port_address = int(port_entry.get())
        pi.connect()

    connection_window = tkinter.Toplevel(root)

    ip_label = tkinter.Label(connection_window, text="IP Address:", width=10, anchor='e')
    port_label = tkinter.Label(connection_window, text="Port:", width=10, anchor='e')
    ip_entry = tkinter.Entry(connection_window, width=15)
    port_entry = tkinter.Entry(connection_window, width=15)
    connect_to_server_button = tkinter.Button(connection_window, text='Connect', width=25, command=connect_button)

    ip_label.grid(row=0, column=0)
    port_label.grid(row=1, column=0)
    ip_entry.grid(row=0, column=1)
    port_entry.grid(row=1, column=1)
    connect_to_server_button.grid(row=2, column=0, columnspan=2)


logo = tkinter.PhotoImage(file="v1.gif")

top_frame = tkinter.Frame(root)
bottom_frame = tkinter.Frame(root)
top_frame.grid()
bottom_frame.grid()

# top_frame
label = tkinter.Label(top_frame, text="Jason's Watering System", width=70)
open_connection = tkinter.Button(top_frame, text="Connection setup", width=20, height=3, command=setup_window)
photo_label = tkinter.Label(top_frame, image=logo)
label.grid(row=0, column=0, columnspan=2, sticky='w')
open_connection.grid(row=0, column=2, sticky='e')
photo_label.grid(row=1, column=0, columnspan=3)

# Bottom frame Headers
pin_header = tkinter.Label(bottom_frame, text="Pin #", width=20)
location = tkinter.Label(bottom_frame, text="Area", width=20)
timer = tkinter.Label(bottom_frame, text='Timer (mins)', width=20)
spacer = tkinter.Label(bottom_frame, width=20)
black_spacer = tkinter.Label(bottom_frame, width=1, bg='black')
auto = tkinter.Label(bottom_frame, text="Configure Auto", width=15)

pin_header.grid(row=0, column=0)
location.grid(row=0, column=1)
timer.grid(row=0, column=2)
spacer.grid(row=0, column=3)
black_spacer.grid(row=0, column=4)
auto.grid(row=0, column=5)

# area 1 GUI
pin1 = tkinter.Label(bottom_frame, text=int(hose1.pin))
location1 = tkinter.Label(bottom_frame, text=hose1.location)
timer1 = tkinter.Entry(bottom_frame, width=8)
button1 = tkinter.Button(bottom_frame, text="Start/Stop", command=start1, width=13)
black_spacer1 = tkinter.Label(bottom_frame, width=1, bg='black')
configure1 = tkinter.Button(bottom_frame, text='setup')


pin1.grid(row=1, column=0)
location1.grid(row=1, column=1)
timer1.grid(row=1, column=2)
button1.grid(row=1, column=3)
black_spacer1.grid(row=1, column=4)
configure1.grid(row=1, column=5)

# area 2 GUI
pin2 = tkinter.Label(bottom_frame, text=int(hose2.pin))
location2 = tkinter.Label(bottom_frame, text=hose2.location)
timer2 = tkinter.Entry(bottom_frame, width=8)
button2 = tkinter.Button(bottom_frame, text="Start/Stop", command=start2, width=13)
black_spacer2 = tkinter.Label(bottom_frame, width=1, bg='black')
configure2 = tkinter.Button(bottom_frame, text='setup')


pin2.grid(row=2, column=0)
location2.grid(row=2, column=1)
timer2.grid(row=2, column=2)
button2.grid(row=2, column=3)
black_spacer2.grid(row=2, column=4)
configure2.grid(row=2, column=5)

# area 3 GUI
pin3 = tkinter.Label(bottom_frame, text=int(hose3.pin))
location3 = tkinter.Label(bottom_frame, text=hose3.location)
timer3 = tkinter.Entry(bottom_frame, width=8)
button3 = tkinter.Button(bottom_frame, text="Start/Stop", command=start3, width=13)
black_spacer3 = tkinter.Label(bottom_frame, width=1, bg='black')
configure3 = tkinter.Button(bottom_frame, text='setup')


pin3.grid(row=3, column=0)
location3.grid(row=3, column=1)
timer3.grid(row=3, column=2)
button3.grid(row=3, column=3)
black_spacer3.grid(row=3, column=4)
configure3.grid(row=3, column=5)

# area 4 GUI
pin4 = tkinter.Label(bottom_frame, text=int(hose4.pin))
location4 = tkinter.Label(bottom_frame, text=hose4.location)
timer4 = tkinter.Entry(bottom_frame, width=8)
button4 = tkinter.Button(bottom_frame, text="Start/Stop", command=start4, width=13)
black_spacer4 = tkinter.Label(bottom_frame, width=1, bg='black')
configure4 = tkinter.Button(bottom_frame, text='setup')


pin4.grid(row=4, column=0)
location4.grid(row=4, column=1)
timer4.grid(row=4, column=2)
button4.grid(row=4, column=3)
black_spacer4.grid(row=4, column=4)
configure4.grid(row=4, column=5)


try:
    root.mainloop()
finally:
    if pi.connection_established:
        hose1.turn_off()
        hose2.turn_off()
        hose3.turn_off()
        hose4.turn_off()
        print("socket closed")
        my_socket.close()
