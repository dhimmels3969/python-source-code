#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 31 through 38
#





#######################################################################################################
def exercise_31():
    """
    Exercise 31. Remove Duplicate Characters
    Practice Problem: Write a program to remove all duplicate characters
        from a string while keeping the remaining characters in their original order.
    Exercise Purpose: This focuses on Order-Preserving Filtering. While a set()
        removes duplicates, it also ruins the order. This exercise teaches you
        how to use a loop and a “seen” tracker to clean data without scrambling it.
    Given Input:
        str1 = "google"
    Expected Output:
        gole
    """
    pass



#######################################################################################################
def exercise_32():
    """
    Exercise 32. Word Reversal
    Practice Problem: Reverse the order of words in a given sentence, but
        keep the characters within the words in their original order.
    Exercise Purpose: This clarifies the difference between Sequence Reversal
        and Character Reversal. It’s a standard interview question that tests your
        ability to manipulate lists of strings rather than just raw text.
    Given Input:
        str1 = "Python is fun"
    Expected Output:
        fun is Python
    """
    pass



#######################################################################################################
def exercise_33():
    """
    Exercise 33. Character Interleaving
    Practice Problem: Given two strings of equal length, merge them by alternating characters.
    Exercise Purpose: This exercise introduces Parallel Iteration. In data science,
        you often need to merge two separate arrays of data (like names and IDs) into
        a single paired format. It teaches you how to coordinate multiple indices simultaneously.
    Given Input:
        s1 = "ABC", s2 = "xyz"
    Expected Output:
        AxByCz
    """
    pass



#######################################################################################################
def exercise_34():
    """
    Exercise 34. Longest Word
    Practice Problem: Write a program to find the longest word
        in a given sentence. If there is a tie, return the first one found.
    Exercise Purpose: This exercise practices Comparison Logic and State
        Tracking. It’s a fundamental pattern in programming: iterating through
        a collection while keeping track of the “best” (or longest/largest) item found so far.
    Given Input:
        str1 = "The quick brown fox jumps over the lazy dog"
    Expected Output:
        Longest word: quick
    Note: “brown” and “jumps” are also 5 letters, but “quick” appears first.
    """
    pass



#######################################################################################################
def exercise_35():
    """
    Exercise 35. Acronym Creator
    Practice Problem: Write a program to generate an acronym from a
        given phrase (e.g., “Random Access Memory” becomes “RAM”).
    Exercise Purpose: This exercise focuses on String Transformation. It teaches
        you how to extract specific metadata (the first letter) from tokens
        and combine them into a new, condensed format.
    Given Input:
        str1 = "Random Access Memory"
    Expected Output:
        RAM
    """
    pass



#######################################################################################################
def exercise_36():
    """
    Exercise 36. Word Frequency
    Practice Problem: Count the occurrences of each word in a string and store the result in a dictionary.
    Exercise Purpose: This is the word-level version of character counting. It introduces
        Frequency Mapping at scale, which underpins search engine indexing and “word cloud” generation.
    Given Input:
        str1 = "apple banana apple cherry banana apple"
    Expected Output:
        {'apple': 3, 'banana': 2, 'cherry': 1}
    """
    pass



#######################################################################################################
def exercise_37():
    """
    Exercise 37. First Non-Repeating Character
    Practice Problem: Find the first character in a string that does not repeat anywhere else.
    Exercise Purpose: This exercise demonstrates Multi-Pass Algorithms.
        You cannot solve this in a single pass because you won’t know if a
        character repeats until you see the whole string. It teaches you to
        use a frequency map to guide a second traversal.
    Given Input:
        str1 = "swiss"
    Expected Output:
        w
    """
    pass



#######################################################################################################
def exercise_38():
    """
    Exercise 38. String Rotation Check
    Practice Problem: Write a program to check if one string is a rotation of
        another (e.g., “waterbottle” is a rotation of “erbottlewat”).
    Exercise Purpose: This exercise teaches Algorithmic Cleverness. While
        you could try to rotate the string manually in a loop, there is
        a “cheat code” logic that involves string concatenation, which
        is much more efficient.
    Given Input:
        s1 = "waterbottle" s2 = "erbottlewat"
    Expected Output:
        Is Rotation: True
    """
    pass







