#Simple Serial Port Logger Script 

import serial #PySerial

filename = input('\nPlease Enter absolute file path with the file name at the end\n') #prompt user to input file path

#Ensure that file can be created/opened
try:
    with open(filename, 'a') as file_object:
        file_object.write("\nStart of Logging Session \n")
except FileNotFoundError:
    print('File could not be created')
    
com_port = input('please enter your COM port number. For example for port 14 you would enter COM14\n') #prompt user for com port 
baudrate = int(input('please enter the baud rate \n')) #prompt user for baudrate, only standard baud rates are supported 

config = 2 #Variable to store whether the default config was selected, 0 = defualt config, 1 = manual config 
while config > 1:
    print('Default config: byte size = 8, Parity = None, Stop bits = 1,No timeouts and all flow control disabled')  
    config = input('Would you like to use the default configuration or configure the rest of the settings manually? Y or N \n')
    if config == 'n' or config == 'N':
        config = 1
    elif config == 'y' or config == 'Y':
        config = 0
    else: print('Invalid Value. Please enter choice again.')

if config == 1:
    bytesize = input('Enter byte size \n')
    if bytesize == 5:
        bytesize = serial.FIVEBITS
    elif bytesize == 6:
        bytesize = serial.SIXBITS
    elif bytesize == 7:
        bytesize = serial.SEVENBITS
    else: bytesize = serial.EIGHTBITS
    print(bytesize)

    parity = input('Enter Parity type as either NONE, EVEN, ODD, MARK, or SPACE \n')
    if parity == 'None' or parity == 'NONE' or parity == 'none':
        parity = serial.PARITY_NONE
    elif parity == 'Even' or parity == 'EVEN' or parity == 'even':
        parity = serial.PARITY_EVEN
    elif parity == 'Odd' or parity == 'ODD' or parity == 'odd':
        parity = serial.PARITY_ODD
    elif parity == 'Mark' or parity == 'MARK' or parity == 'mark':
        parity = serial.PARITY_MARK    
    else: parity = serial.PARITY_SPACE
    print(parity)

    stop_bits = input('Enter number of stop bits\n')
    if stop_bits == 1:
        stop_bits = serial.STOPBITS_ONE
    elif stop_bits == 1.5:
        stop_bits = serial.STOPBITS_ONE_POINT_FIVE
    elif stop_bits == 2:
        stop_bits = serial.STOPBITS_TWO
    else: stop_bits = serial.STOPBITS_ONE
    print(stop_bits)

    timeout = int(input('Enter a Read Timout Value\n'))
    xonxoff = input('Enable Flow control? Y or N?\n')
    if xonxoff == 'Y' or xonxoff == 'y':
        xonxoff = True
    else: xonxoff = False
    rtscts = input('Enable RTS and CTS? Y or N?\n')
    if rtscts == 'Y' or rtscts == 'y':
        rtscts = True
    else: rtscts = False
    dsrdtr = input('Enable DSR and DTR? Y or N?\n')
    if dsrdtr == 'Y' or dsrdtr == 'y':
        dsrdtr = True
    else: dsrdtr = False 
    write_timeout = int(input('Enter a Write timeout value\n'))

else:
    bytesize = serial.EIGHTBITS
    parity = serial.PARITY_NONE
    stop_bits = 1
    timeout = None
    xonxoff = 0
    rtscts = 0
    dsrdtr = 0
    write_timeout = 0

#after com port is configured test to see if com port can be opened    
try:
    ser = serial.Serial(com_port,baudrate,bytesize,parity,stop_bits,timeout,xonxoff,rtscts,write_timeout,dsrdtr)
except serial.serialutil.SerialException:
    print('Unable to open COM port\n')
except ValueError:
    print('Com port parameter out of range\n')

input_character = '0' #character received from com port and written to file 

with open(filename, 'a') as log_file:
     print("Com port and log file open. Press any key to stop logging")
     while input_character != '': #Stop script when the escape character appears. 
         input_character = ser.read(1)
         input_character = input_character.decode("utf-8")
         log_file.write(input_character)
     ser.close()
#End of Script     
