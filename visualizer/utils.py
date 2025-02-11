import glob
import serial
import struct
import sys
from math import log, ceil

from pymodbus.payload import BinaryPayloadBuilder

from visualizer.constants import RADIX_PREFIX

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def format_data(data, dtype:str, byte_order=">", word_order=">", base=10):
    """
    Should convert a list of data to the specified data type in the specified base.

    :param data:
    :param dtype:
    :param byte_order:
    :param word_order:
    :param base:
    :return:
    """
    raw_byte_str = struct.pack(byte_order + 'H'*len(data), *data)
    size = struct.calcsize(dtype)
    stub = len(raw_byte_str) % size

    if stub > 0:
        byte_str = raw_byte_str[:-stub]  # lop off any segmented data that wont fit in target datatype
    else:
        byte_str = raw_byte_str[:]

    fmt_len = len(byte_str) // size
    if size == 4:
        if (word_order == "<"):
            byte_str = b"".join([ byte_str[i:i+2][::-1] for i in range(0,len(byte_str),2) ])

        result = struct.unpack(word_order + dtype * fmt_len, byte_str)

    else:
        result = struct.unpack(">" + dtype*fmt_len, byte_str)

    num_base_prefixes = {2: "0b", 8: "0o", 16: "0x"}

    prefix = num_base_prefixes.get(base, "")
    if prefix:
        # pad_len -> https://math.stackexchange.com/questions/593670/proving-number-of-digits-d-to-represent-integer-n-in-base-b
        pad_len = int(ceil( log(2**(size * 8), base) ))  # Putting the math degree to use.

        formatted = []
        for i in result:
            num = str_base(i, base)
            if num[0] == '-':
                sign = '-'
                num = num[1:]
            else:
                sign = ''

            formatted.append(sign + prefix + num.upper().rjust(pad_len, '0'))
        # formatted = [ prefix + str_base(i, base).rjust(pad_len, '0') for i in result ]

    elif dtype == 'f':
        formatted = [ str(i) for i in result ]  # Don't call `str_base` since base is always 10 for floats.
                                                # And it causes strange formatted outputs for negative floats.
    else:
        formatted = [ str_base(i, base) for i in result ]

    if size == 4:
        copy = formatted[:]
        formatted = []
        for num in copy:
            formatted.extend([num, ''])  # Leave every other cell blank since registers are combined in size 4

    return formatted

def format_write_value(string, dtype='H', byte_order='>', word_order='>'):
    builder = BinaryPayloadBuilder(byteorder=byte_order, wordorder=word_order)
    builder_functions = {"H": builder.add_16bit_uint,
                         "h": builder.add_16bit_int,
                         "I": builder.add_32bit_uint,
                         "i": builder.add_32bit_int,
                         "f": builder.add_32bit_float}

    num_txt = string[:]
    sign = ''

    if string[0] == '-':
        sign = '-'
        num_txt = string[1:]

    radix = RADIX_PREFIX.get(num_txt[:2], 10)
    if radix != 10:
        num_txt = string[2:]

    vals = []
    if dtype == 'f':
        try:
            val = float(sign + num_txt)
        except ValueError:
            return None
    else:
        try:
            val = int(sign + num_txt, radix)
        except ValueError:
            return None

    try:
        builder_functions[dtype](val)
    except struct.error:
        return None

    builder.build()
    payload = builder.to_registers()

    return payload

def serial_ports():
    """
        Thanks to: https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
        Lists available serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == '__main__':
    print(serial_ports())