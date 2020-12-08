import keyboard, time, sys, os

def countdown(n: int)->None:
    """ print a countdown from n
    """
    while(n):
        print(n, end=" ... ", flush=True);
        time.sleep(1) # wait one second
        n -= 1

def get_file_contents(file_name: str)->str:
    """ open a and return its contents as a string
    """
    with open(file_name) as f:
        return f.read()

def get_printable(args: list)->str or list(str):
    """ return what needs to be printed
    :args[0]: the path of where the script is run
    :args[1]: [optional] should be '-f' to signal if it is running from a file
    :args[1 or 2 thru infinity]: the text to be printed or if '-f' is there then read from file
    :returns: string to print
    """
    if len(args) < 2:
        print("Not enough arguments")
        print_usage()
        return ""
    PATH_TO_DIR = args.pop(0)
    read_from_file = False
    split = False
    if '-f' in args:
        args.remove('-f')
        read_from_file = True
    if '-s' in args:
        args.remove('-s')
        split = True
    else:
        read_from_file = False
    input_arg = ' '.join(args)
    if read_from_file:
        if ':' in input_arg.lower():
            path = input_arg
        else:
            path = PATH_TO_DIR + '\\' + input_arg
        if not os.path.isfile(path):
            print(f"{path} is not a valid path");
            print_usage()
            return ""
        result = get_file_contents(path)
    else:
        result = input_arg
    if split:
        return result.split()
    return split

def print_usage()->None:
    """ print the usage of this command
    """
    print(
            "\tTypeF [flags] {input/filename}" +
            "\n\t\tonly local paths work" +
            "\n\t\tflags:" +
            "\n\t\t\t-f  =  input is a file name:" +
            "\n\t\t\t-s  =  print each word as a line"
            )

def main():
    printable = get_printable(sys.argv[1:])
    if printable != "" and printable != []:
        print(f"printing in", end=": ")
        countdown(5)
        if isinstance(printable, list):
            for i in printable:
                keyboard.write(i + '\n')
        else:
            keyboard.write(printable)

if __name__ == "__main__":
    main()
