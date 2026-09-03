def printArray(array: list[int]):
    for i in range (len(array)):
        print(f"array[{i}]: {array[i]}")

def entervalues(array: list[int]):
    i=0;
    while i < len(array):
        try:
            print(f"Liczba {i + 1}", end="")
            array[i] = int(input())
            i += 1
        except:
            print(f"nie poprawna wartośc, wprowadź lczbę całkowitą:")


def minvalue(array: list[int]):



def maxvalue(array: list[int]):
    pass

def calculateSum(array: list[int]):
    pass

def avgvalue(array: list[int]):
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
                entervalues(array)
            case 2:
                printArray(array)
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


