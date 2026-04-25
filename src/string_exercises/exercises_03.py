#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 21 through 30
#





#######################################################################################################
def exercise_21():
    """
    Exercise 21. Count occurrences of all characters within a string
    Practice Problem: Count the frequency of every character in a string
        and store the results in a dictionary.
    Exercise Purpose: This exercise introduces Frequency Mapping using
        Dictionaries. Dictionaries are essential for counting and organizing
        data because they store unique “keys” (the characters) and associated
        “values” (their counts).
    Given Input:
        str1 = "apple"
    Expected Output:
        {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    """
    pass



#######################################################################################################
def exercise_22():
    """
    Exercise 22. Remove empty strings from a list of strings
    Practice Problem: Given a list of strings, remove any empty
        strings or None values from it.
    Exercise Purpose: This introduces Data Cleaning. Real-world datasets often
        have missing or empty values. Learning to filter lists is essential
        to prevent your program from crashing when processing empty data points.
    Given Input:
        str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    Expected Output:
        ['Emma', 'Jon', 'Kelly', 'Eric']
    """
    pass



#######################################################################################################
def exercise_23():
    """
    Exercise 23. Remove special symbols/punctuation from a string
    Practice Problem: Write a program to remove all special symbols
        and punctuation from a given string.
    Exercise Purpose: This exercise is a staple of Natural Language Processing (NLP).
        Before analyzing text like sentiment analysis, you must remove “noise”
        such as symbols and punctuation so the computer can focus on the words.
    Given Input:
        str1 = "/*Jon is @developer & musician!!"
    Expected Output:
        "Jon is developer musician"
    """
    pass



#######################################################################################################
def exercise_24():
    """
    Exercise 24. Remove all characters from a string except integers
    Practice Problem: Write a program to extract only the numeric digits
        from a mixed string and combine them into a single string.
    Exercise Purpose: This is a core part of Data Extraction. Often when
        scraping web data or reading OCR text from images, you get strings
        like “Price: $25.00”. This exercise teaches you how to strip away
        the “noise” such as currency, labels, and spaces to get the raw numerical
        data for calculations.
    Given Input:
        str1 = "I am 25 years and 10 months old"
    Expected Output:
        2510
    """
    pass



#######################################################################################################
def exercise_25():
    """
    Exercise 25. Find words with both letters and numbers
    Practice Problem: Write a program to find and print words from a string
        that contain both letters and numbers.
    Exercise Purpose: This exercise focuses on Contextual Filtering. In cybersecurity
        or system administration, you often need to find “alphanumeric” strings like
        Product IDs (e.g., PROD123), license keys, or mixed-character usernames. It
        teaches you how to look for specific patterns within individual tokens.
    Given Input:
        str1 = "Emma25 is Data scientist50 and AI Expert"
    Expected Output:
        Emma25
        scientist50
    """
    pass



#######################################################################################################
def exercise_26():
    """
    Exercise 26. Replace each special symbol with # in the following string
    Practice Problem: Write a program to replace every special symbol (punctuation)
        in a string with a specific character, like #.
    Exercise Purpose: Vital for Data Sanitization. Before sending text
        to certain databases or file systems that can’t handle symbols like @ or &,
        you often need to “mask” them. It’s also a great introduction to the
        string module’s built-in constants.
    Given Input:
        str1 = "/*Jon is @developer & musician!!"
    Expected Output:
        ##Jon is #developer # musician##
    """
    pass



#######################################################################################################
def exercise_27():
    """
    Exercise 27. Palindrome Check
    Practice Problem: Write a program to check if a string is a palindrome
        (reads the same forward and backward).
    Exercise Purpose: The palindrome check is the “Hello World” of Algorithmic
        Logic. It teaches you how to compare a sequence against its own reflection.
        In real-world applications, this concept is used in DNA sequencing
        and data integrity verification.
    Given Input:
        str1 = "radar"
    Expected Output:
        Is Palindrome: True
    """
    pass



#######################################################################################################
def exercise_28():
    """
    Exercise 28. Anagram Detector
    Practice Problem: Write a program to check if two strings are anagrams
        (formed by rearranging the letters of another, such as “listen” and “silent”).
    Exercise Purpose: This exercise teaches Canonical Forms. By sorting two different
        strings into a “standard” order (alphabetical), you can easily determine if
        they contain the exact same ingredients. This is a fundamental concept in data deduplication.
    Given Input:
        s1 = "listen", s2 = "silent"
    Expected Output:
        Are Anagrams: True
    """
    pass



#######################################################################################################
def exercise_29():
    """
    Exercise 29. Unique Character Check
    Practice Problem: Write a function to determine if a string has all
        unique characters. Return True if every character appears only
        once, otherwise return False.
    Exercise Purpose: This introduces the concept of Sets. In Python, a set
        is an unordered collection that cannot contain duplicate items. Comparing
        the length of a string to the length of its “set version” is the most
        efficient way to check for uniqueness in O(n) time.
    Given Input:
        str1 = "python"
        str2 = "alphabet"
    Expected Output:
        "python" unique: True
        "alphabet" unique: False
    """
    pass



#######################################################################################################
def exercise_30():
    """
    Exercise 30. Title Case Logic
    Practice Problem: Write a program to capitalize the first letter of
        every word in a sentence without using the built-in .title() method.
    Exercise Purpose: This practice covers String Splitting and Indexing. While .title() exists,
        manually implementing it helps you understand how to isolate parts of a string, modify them,
        and rebuild the sentence. This is a common requirement in data transformation.
    Given Input:
        str1 = "hello world from python"
    Expected Output:
        Hello World From Python
    """
    pass



