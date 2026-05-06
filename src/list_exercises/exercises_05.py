from src.common_library import helper_functions as hf


#
# Exercises found at web page https://pynative.com/python-list-exercise-with-solutions/
# Exercises 41 through 45
#


##############################################################################
def exercise_41_rotate_list_to_the_right():
    """
    Exercise 41. Rotate a List (Left or Right by k positions)
    Practice Problem: Write a function to rotate a list to the left by k positions.
        For example, if k=2, the first two elements move to the end of the list.
    Exercise Purpose: List rotation is a common algorithm in circular buffers
        and scheduling. This exercise teaches you how to use the Modulo Operator (%)
        to handle cases where k is larger than the list length, and how to perform
        complex reordering using Slicing.
    Given Input:
        List: [1, 2, 3, 4, 5]
        k: 2
    Expected Output:
        Rotated List: [3, 4, 5, 1, 2]
    """
    print("Exercise 41. Rotate a List to the right by k positions")
    input_list = [1, 2, 3, 4, 5]
    k = 2
    head = input_list[:k:]
    tail = input_list[k::]
    results = tail + head
    print(f"Rotated List: {results}")
    pass



##############################################################################
def exercise_42_split_list_into_chunks():
    """
    Exercise 42. Split List into Chunks of Size N
    Practice Problem: Create a function that takes a list and an integer N,
        and breaks the list into smaller sublists, each of length N. The
        last chunk may be shorter if the list length isn’t perfectly divisible by N.
    Exercise Purpose: Batch processing is essential when dealing with
        large datasets or API limits (e.g., “send 50 emails at a time”).
        This exercise demonstrates the use of the Step Parameter in
        the range() function.
    Given Input:
        List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        N: 3
    Expected Output:
        Chunks: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

    Solution from PyNative website
    [ myList[i: i + N]  for i in range(0, len(myList) , N)]
    """
    print("Exercise 42. Split List into Chunks")
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = 3
    results = [input_list[i * N: i * N + N] for i in range(0, len(input_list) // N + 1)]
    print(f"Chunks: {results}")
    pass



##############################################################################
def exercise_43_move_zeros_to_end_of_list():
    """
    Exercise 43. Move All Zeros to the End (Maintaining Order)
    Practice Problem: Given a list of numbers, push all zeros to the end
        of the list while maintaining the relative order of all non-zero
        elements. This must be done efficiently.
    Exercise Purpose: This “Stable Partitioning” problem is a favorite in
        technical interviews. It tests your ability to filter data based
        on a specific criterion while preserving the integrity of the
        remaining sequence.
    Given Input:
        List: [0, 1, 0, 3, 12]
    Expected Output:
        Result: [1, 3, 12, 0, 0]
    """
    print("Exercise 43. Move All Zeros to the End (Maintaining Order)")
    input_list = [0, 1, 0, 3, 12]
    result = [x for x in input_list if x != 0] + [x for x in input_list if x == 0]
    print(f"Result: {result}")
    pass



##############################################################################
def exercise_44_generate_prime_numbers():
    """
    Exercise 44. Generate Prime Numbers using List Comprehension
    Practice Problem: Write a single list comprehension that generates
        a list of all prime numbers up to a given number n.  Prime number is
        a whole number greater than 1 that cannot be exactly divided by
        any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
    Exercise Purpose: This exercise pushes your List Comprehension skills
        to the limit. It requires nesting logic and understanding the
        mathematical definition of a prime (a number x > 1 that has no
        divisors other than 1 and itself).
    Given Input:
        n = 20
    Expected Output:
        Primes: [2, 3, 5, 7, 11, 13, 17, 19]

    PyNative Solution:
        def get_primes(n):
            # A prime is any number not in the list of products (composites)
            composites = [j for i in range(2, 8) for j in range(i*2, n + 1, i)]
            primes = [x for x in range(2, n + 1) if x not in composites]
            return primes
    """
    print("Exercise 44. Generate Prime Numbers using List Comprehension")
    n = 20
    prime_list = [x for x in range(n) if hf.is_prime_number(x) > 0]
    print(f"Primes: {prime_list}")
    pass



##############################################################################
def exercise_45_find_all_subsets():
    """
    Exercise 45. Find All Subsets of a List (Power Set)
    Practice Problem: Write a function to find the Power Set
        of a given list. The Power Set is a list of all possible subsets,
        including the empty list and the list itself.
    Exercise Purpose: This introduces Combinatorial Logic. The number of
        subsets for a list of size n is always 2n. Mastering this is
        crucial for “Brute Force” algorithms where you need to test
        every possible combination of items.
    Given Input:
        List: [1, 2, 3]
    Expected Output:
        Subsets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """

    # from PyNative website...
    def get_power_set(lst):
        result = [[]]
        for element in lst:
            # For every existing subset, create a new one including the 'element'
            new_subsets = [subset + [element] for subset in result]
            result.extend(new_subsets)
        return result

    # Test the function
    base_list = [1, 2, 3]
    subsets = get_power_set(base_list)

    print("Exercise 45. Find All Subsets of a List (Power Set)")
    # input_list = [1, 2, 3]
    # final_results = []
    # final_results.append([])
    # l1 = [[i] for i in input_list]
    # l2 = [[i, j] for i in input_list for j in input_list if i != j]
    # l3 = sorted(l1 + l2)
    # final_results.append(l3)
    # final_results.append(input_list)
    print(f"Subsets: {subsets}")
    pass



