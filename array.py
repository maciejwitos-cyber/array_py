def print_array(array: list[int]):
    for i in range (len(array)):
        print(f"array[{i}]: {array[i]}")


def enter_values(array: list[int]):
    i=0
    while i < len(array):
        try:
            print(f"Liczba {i + 1}", end="")
            array[i] = int(input())
            i += 1
        except:
            print(f"niepoprawna wartośc, wprowadź lczbę całkowitą:")


def min_value(array: list[int]):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
    return min


def max_value(array: list[int]):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    return max

def calculate_sum(array: list[int]):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

def avg_value(array: list[int]):
    avg = calculate_sum(array) / len(array)
    return avg

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
        match option:
            case 1:
                enter_values(array)
            case 2:
                print_array(array)
            case 3:
                print(f'Minimum value: {min_value(array)}')
            case 4:
                print(f'Maximum value: {max_value(array)}')
            case 5:
                print(f'Average value: {avg_value(array)}')
            case 0:
                break
            case _:
                print(f'Invalid option: {option}')

########

if __name__ == '__main__':
    main()


