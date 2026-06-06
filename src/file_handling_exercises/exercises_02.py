#
# Exercises found at web page https://pynative.com/python-file-handling-exercises/
# Exercises 11 through 20
#



##############################################################################
def exercise_11_count_total_words():
    """
    Exercise 11: Count Total Words in File
    Problem Statement: Write a Python program that reads a file
        called data.txt and counts the total number of words
        across all its lines.
    Purpose: This exercise builds on reading file content and
        applying string methods to analyse text. Word counting
        is a fundamental operation in text processing, search
        indexing, and natural language processing tasks.
    Given Input:
        A file named data.txt containing:
            Hello World
            Python is great
            File handling is easy
    Expected Output:
        Total words: 9
    """
    print("Exercise 11: Count Total Words in File")
    pass


##############################################################################
def exercise_12_count_total_characters():
    """
    Exercise 12: Count Total Characters in File
    Problem Statement: Write a Python program that reads a file
        called data.txt and counts the total number of characters
        it contains, including spaces and newlines.
    Purpose: This exercise demonstrates how to measure the size
        of text content at the character level. Character
        counting is useful in text editors, form validation,
        data compression analysis, and anywhere that the byte
        or character length of a file is relevant.
    Given Input:
        A file named data.txt containing: Hello, World!
    Expected Output:
        Total characters: 13
    """
    print("Exercise 12: Count Total Characters in File")
    pass


##############################################################################
def exercise_13_count_word_occurrences():
    """
    Exercise 13: Count Specific Word Occurrences in File
    Problem Statement: Write a Python program that reads a
        file called data.txt and counts how many times the
        word Python appears in it.
    Purpose: This exercise combines file reading with string
        search methods. Counting specific word or pattern
        occurrences is a core technique in log parsing,
        keyword analysis, content auditing, and search
        engine development.
    Given Input:
        A file named data.txt containing:
            Python is great.
            I love Python.
            Python makes file handling easy.
    Expected Output:
        Occurrences of 'Python': 3
    """
    print("Exercise 13: Count Specific Word Occurrences in File")
    pass


##############################################################################
def exercise_14_read_first_n_lines():
    """
    Exercise 14: Read Only First N Lines
    Problem Statement: Write a Python program that reads and
        prints only the first 3 lines from a file called
        data.txt.
    Purpose: This exercise teaches you how to limit file
        reading to a specific number of lines. This technique
        is critical when working with large files where
        reading the entire content is inefficient, such
        as previewing log files, inspecting dataset headers,
        or loading configuration sections.
    Given Input: A file named data.txt containing:
        Line 1
        Line 2
        Line 3
        Line 4
        Line 5
    Expected Output:
        Line 1
        Line 2
        Line 3
    """
    print("Exercise 14: Read Only First N Lines")
    pass


##############################################################################
def exercise_15_read_last_n_lines():
    """
    Exercise 15: Read Only Last N Lines
    Problem Statement: Write a Python program that reads and
        prints only the last 3 lines from a file called
        data.txt.
    Purpose: Reading the tail of a file is one of the most
        common real-world file operations, used extensively
        in log monitoring, debugging, and audit trail review.
        This exercise teaches you how to retrieve the most
        recent entries from a file efficiently.
    Given Input: A file named data.txt containing:
        Line 1
        Line 2
        Line 3
        Line 4
        Line 5
    Expected Output:
        Line 3
        Line 4
        Line 5
    """
    print("Exercise 15: Read Only Last N Lines")
    pass


##############################################################################
def exercise_16_read_line_numbers_from_file():
    """
    Exercise 16: Read Specific Line Numbers from File
    Problem Statement: Write a Python program that reads a file
        called data.txt and prints only the lines at positions
        1, 3, and 5 (using 1-based line numbering).
    Purpose: This exercise teaches selective file reading by
        targeting specific line numbers. This pattern is useful
        when parsing structured files where particular lines
        carry known information, such as headers, metadata
        rows, or fixed-position records in a report.
    Given Input: A file named data.txt containing:
        Line 1
        Line 2
        Line 3
        Line 4
        Line 5
    Expected Output:
        Line 1
        Line 3
        Line 5
    """
    print("Exercise 16: Read Specific Line Numbers from File")
    pass


##############################################################################
def exercise_17_find_longest_word():
    """
    Exercise 17: Find Longest Word in File
    Problem Statement: Write a Python program to read a text file
        and find the longest word present in it.
    Purpose: This exercise strengthens your ability to read file
        content, split text into tokens, and apply comparison
        logic across a collection – skills useful in text
        analysis, NLP preprocessing, and content parsing tasks.
    Given Input:
        A file words.txt containing: Python is a powerful programming language
    Expected Output:
        Longest word: programming
    """
    print("Exercise 17: Find Longest Word in File")
    pass


##############################################################################
def exercise_18_letter_frequency():
    """
    Exercise 18: Count Each Letter Frequency in File
    Problem Statement: Write a Python program to read a text
        file and count how many times each letter of the
        alphabet appears in it.
    Purpose: This exercise practises file reading, string
        filtering, and frequency counting using dictionaries –
        foundational techniques in text mining, cryptography,
        and data analysis.
    Given Input:
        A file sample.txt containing: Hello World
    Expected Output:
        h: 1
        e: 1
        l: 3
        o: 2
        w: 1
        r: 1
        d: 1
    """
    print("Exercise 18: Count Each Letter Frequency in File")
    pass


##############################################################################
def exercise_19_search_for_words_in_file():
    """
    Exercise 19: Search Word and Print Matching Line Numbers
    Problem Statement: Write a Python program to search for a specific
        word in a file and print the line numbers where that
        word appears.
    Purpose: This exercise builds skills in line-by-line file reading,
        string searching, and index tracking – useful in log analysis,
        debugging tools, and text search utilities.
    Given Input:
        A file notes.txt where the word Python appears on lines 1 and 3,
        and the search term is Python.
    Expected Output:
        "Python" found on line 1
        "Python" found on line 3
    """
    print("Exercise 19: Search Word and Print Matching Line Numbers")
    pass


##############################################################################
def exercise_20_strip_whitespace():
    """
    Exercise 20: Strip Extra Whitespace and Save to New File
    Problem Statement: Write a Python program to read a text
        file, remove leading and trailing whitespace from
        each line, and save the cleaned content to a new file.
    Purpose: This exercise practises reading, transforming,
        and writing file content line by line – a common
        pattern in data cleaning pipelines, log processing,
        and file preprocessing tasks.
    Given Input:
        A file messy.txt with lines such as Hello World  and Python
    Expected Output:
        A new file clean.txt containing Hello World
        and Python, with all surrounding whitespace removed.
    """
    print("Exercise 20: Strip Extra Whitespace and Save to New File")
    pass




