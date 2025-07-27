"""
* Author:    Avichal Kaul
* Updated:   07/2025
"""

import struct ## to convert to IEE 32 bit format

def registers_to_decimal(register):
    """ Convert array of decimal register values to IEEE floating point number
            Input:
                register: `array of ints`
                    Array of length 1 for 2-byte number (one register), 2 for a 4-byte number (two registers)

            Returns:
                value: `float`
                    Correct decimal representation of stored value
    """
    print(f'Registers: {register}')
    hex_representation = ''
    for decimal_value in register:
        ## convert each decimal value to a 2-byte hex value and concatenate
        hex_representation += "{:04x}".format(decimal_value)
    print(f'Hex Representation: {hex_representation}')

    ## convert hex representation into a Big-Endian IEEE 32-bit float
    return struct.unpack('!f', bytes.fromhex(hex_representation))[0]

 

def decimal_to_registers(decimal):
    """ Convert IEEE floating point number to array of decimal register values
            Input:
                value: `float`
                    Correct decimal representation of stored value         

            Returns:
                register: `array of ints`
                        Array of length 1 for 2-byte number (one register), 2 for a 4-byte number (two registers)
    """
    print(f'Value: {decimal}')

    ## convert Big-Endian IEEE 32-bit float into a hex representation (and removes 0x at start)
    hex_representation = hex(struct.unpack('<I', struct.pack('<f', decimal))[0])[2:]
    print(f'Hex Representation: {hex_representation}')

    ## split into two registers, then convert from hex back to int
    if len(hex_representation) <= 4:
        return [int(hex_representation), 16]
    return [int(hex_representation[:4], 16), int(hex_representation[4:], 16)]

 

if __name__ == "__main__":
    x = input("1. Decimal to Register \n2. Register to Decimal\n")
    if x == "1":
        x1 = input("Decimal Value=")
        print(decimal_to_registers(float(x1)))
 
    elif x == "2":
        x1 = input("Register Value 1=")
        x2 = input("Register Value 2=")
 
        ## if second value is blank, only pass array w/ len 1
        print(registers_to_decimal([[int(x1), int(x2)] if x2 != '' else [int(x1)]][0]))