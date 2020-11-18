import keyboard, time, sys

def countdown(n: int)->None:
    """ print a countdown from n
    """
    while(n):
        print(n, end=" ... ", flush=True);
        time.sleep(1) # wait one second
        n -= 1

def type_file(file_name: str)->None:
    """ open a file and write its contents on the keyboard
    """
    with open(file_name) as f:
        keyboard.write(f.read())

def print_usage()->None:
    """ print the usage of this command
    """
    print("\tTypeF {Filename}")


def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        print_usage()
        return
    countdown(10)
    print(f"printing {sys.argv[1]}")
    type_file(sys.argv[1])

if __name__ == "__main__":
    main()
