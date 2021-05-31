import pathlib 
import sys, getopt, configparser
from pathlib import Path

def horner(multinomial, n, x):
    result = multinomial[0] 
    for i in range(1, n):
        result = result*x + multinomial[i]
    return result



def parse():                                  # Function that parses arguments
    USAGE = "\n -c: missing file argument \n Syntax: c [argument] \n -h, --help displaying this description and ending\n -v, --version  display version information and exit\n -c, --config starting the program\n "
    VERSION = "Super MEGA 2.0"
    try:
        options, arguments = getopt.getopt(
            sys.argv[1:],                      # Arguments
            'vhc:',                            # Short option definitions
            ["version", "help", "config="])    # Long option definitions
        for o, a in options:
            if o in ("-v", "--version"):
                print(VERSION)
                sys.exit()
            if o in ("-h", "--help"):
                print(USAGE)
                sys.exit()
            if o in ("-c", "--config"):
                x, inputfile = read_config(a)
                main(x, inputfile)
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(1) 
        
def read_config(filename):              # Configuration function
    x = 2
    inputfile = "input.txt"
    config = configparser.ConfigParser()
    filename = Path(filename)
    if not(filename.is_file()):
        print("Config file does not exist")
        sys.exit(1) 
    config.read(filename)
    if "OurX" in config['DEFAULT']:
        x =  config['DEFAULT']['OurX']
    if "InputFile" in config['DEFAULT']:
        inputfile = config['DEFAULT']['InputFile']
    return  x, inputfile


def file_open(filename):
    my_path = pathlib.Path(__file__).parent.absolute()
    file_name = Path(str(my_path) +  "\\" + filename)
    if not(file_name.is_file()):
        print("Input file does not exist")
        sys.exit(1) 
    table = []
    f = open(file_name, 'r')
    for line in f:
        if len(line)>0: 
            table.append(parsing_function(line))
    return table

def parsing_function(record):
    result = []
    record = record.replace(" ", "") 
    place_of_sight = record.find('=')
    record = record[place_of_sight+1:-1] 
    start = 0
    for indeks in range(len(record)):
        if record[indeks] == '+' or record[indeks] == '-':
            if record[start] == '+': start +=1 
            result.append(record[start:indeks])
            start = indeks
    if record[start] == '+': start +=1 
    result.append(record[start:])
    return result


def main(x, filename):
    x = int(x)
    sparsowanyplik  = file_open(filename)
    for row in sparsowanyplik:
        polynomial = []
        lastpower = None
        for el in row:
            muliplier, power = function_reads_the_val(el)
            if lastpower is None:
                polynomial.append(muliplier)
                lastpower = power
            else:
                if power == lastpower-1:
                    polynomial.append(muliplier)
                    lastpower = power
                else:
                    for i in range(lastpower-power-1):
                        polynomial.append(0)
                    polynomial.append(muliplier)
                    lastpower = power
        n = len(polynomial)
        print("Value of the polynomial " + str(row) + " for x=" +str(x) + " is equal to:  " +str(horner(polynomial, n, x)))

def function_reads_the_val(valin):
    power = 0
    muliplier = 0
    xpos = valin.find('x^')
    if xpos == -1:
        if valin.find('x') != -1:
            power = 1
        valin = valin.replace('x', '')
        muliplier = valin
    elif xpos == 0:
        valin = valin.replace('x', '')
        valin = valin.replace('^', '')
        muliplier = 1
        power = valin
    else:
        values = valin.split('x^')
        muliplier = values[0]
        power =  values[1]
    return int(muliplier), int(power)
   

if __name__ == "__main__":
    parse()