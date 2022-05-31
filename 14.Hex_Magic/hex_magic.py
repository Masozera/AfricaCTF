import sys

def main():
    for inpt in sys.stdin:
        if 'exit' == inpt.rstrip():
            break
        print(f'You input is: {inpt}')

        hex_to_bytes_object = bytes.fromhex(inpt) # Creating a bytes object

        ascii_string        =  hex_to_bytes_object.decode("ASCII") # Converting the bytes oject to ASCII representation



        sys.stdout.write('The ASCII representation is: ' + ascii_string + '\n')

    print("You exited the program")

main()
