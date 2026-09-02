def printArray():
    pass

def entervalues():
    pass

def minvalue():
    pass

def maxvalue():
    pass

def calculateSum():
    pass

def avgvalue():
    pass

def menu():
    print("\t1. Enter the values into the array")
    print("\t2. Display the content of the array")
    print("\t3. Determine the minimum value")
    print("\t4. Determine the maximum value")
    print("\t5. Determine the average value")
    print("\t0. EXIT")
    print("\tSelect an option:")


def main():
    print(f'Test, {__name__}')
    array = [0] * 10



    while True:
        menu()
        option = int(input())
        match(option):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                break
            case _:
                print(f'Invalid option: {option}')

########

if __name__ == '__main__':
    main()


