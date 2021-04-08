import random
import statistics
import numpy as np

OUTPUT_FILE = 'output.txt'
LENGTH = 500000

def GenerateInt(a = -10000, b = 10000):
    """Number list generator.

    Args:
        generate_int_list (list): list of Number.

    Returns:
        (list): Random numbers list.

    """

    generate_int_list = []
    for i in range(LENGTH):
        gen_int_list = random.randint(a, b)
        generate_int_list.append(gen_int_list)
    return generate_int_list

def WriteIntList(int_list):
    """Writes result to output file.

    Args:
        Args:
            int_list (str): Random numbers list

    """

    with open(OUTPUT_FILE, 'w') as file:
        file.write('\n'.join(map(str, int_list)))


def getIntFromFile(filename):
    """Get numbers from the file and put them in the list.

    Args:
        get_number_list (List): list of numbers.

    Returns:
        (list): get_number_list(list).

    """
    with open(filename) as f:
            #get_number_list = f.read().splitlines()
            get_number_list = f.read().split()
            map_object = map(int, get_number_list)
            list_of_integers = list(map_object)
    return list_of_integers

def getMaxNumber(number_list):
    """Gets max number of list.

    Args:
        number_list (list): list of numbers.

    Returns:
        (int): max number.

    """
    max_number_list = max(number_list)
    return max_number_list

def getMinNumber(number_list_second):
    """Gets max number of list.

    Args:
        number_list (list): list of numbers.

    Returns:
        (int): max number.

    """
    min_number_list = min(number_list_second)
    return min_number_list

def getMedian(get_median_list):
    """Gets median number of list.

    Args:
        median_of_list (int): median of numbers list.

    Returns:
        (int): median.

    """
    median_of_list = statistics.median(get_median_list)
    return median_of_list

def getMaxRow(max_number_low):
    """Get the longest sequence of numbers from a list.

    Args:
        longest_seq (list): median of numbers list.

    Returns:
        (list): max sequence.

    """
    nums = np.array(max_number_low)
    longest_seq = max(np.split(nums, np.where(np.diff(nums) != 1)[0]+1), key=len).tolist()
    return longest_seq

if __name__ == "__main__":
    generate_integer_list = GenerateInt()
    write_int_list = WriteIntList(generate_integer_list)
    get_int_with_list = getIntFromFile(OUTPUT_FILE)
    get_max_number_of_list = getMaxNumber(get_int_with_list)
    print('Максимальное число последовательности: ' + str(get_max_number_of_list))
    get_min_number_of_list = getMinNumber(get_int_with_list)
    print('Минимальное число последовательности: ' + str(get_min_number_of_list))
    get_median_number = getMedian(get_int_with_list)
    print('Медиана: ' + str(get_median_number))
    get_longest_seq = getMaxRow(get_int_with_list)
    print('Самая длинная возростающая последовательность: : ' + str(get_longest_seq))

