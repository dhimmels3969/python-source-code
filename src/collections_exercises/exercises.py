import logging
import re
from collections import Counter, defaultdict

#
# https://pynative.com/python-collections-module-exercises/
# Exercises 1 through 10
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_01_word_frequency_counter():
    """
    Exercise 1: Word Frequency Counter
    Problem Statement:
        Write a Python program that takes a sentence string and uses
        Counter to count how many times each word appears, then prints
        each word alongside its frequency.
    Purpose:
        Counting word frequencies is one of the most common text processing
        tasks, appearing in search engines, NLP pipelines, content analysis
        tools, and spam filters. This exercise introduces Counter as a
        purpose-built, readable alternative to manually incrementing
        dictionary keys in a loop.
    Given Input:
        sentence = "the cat sat on the mat the cat sat"
    Expected Output:
        Each word and its count printed on a separate line
        , e.g. the: 3, cat: 2, sat: 2, on: 1, mat: 1
    """
    logger.info(f"Exercise 1: Word Frequency Counter")
    sentence = "the cat sat on the mat the cat sat"
    words_in_sentence_counter = Counter(sentence.split(" "))
    for word in words_in_sentence_counter:
        logger.info(f"  {word}: {words_in_sentence_counter[word]}")
    pass


#########################################################################################
def exercise_02_most_common_elements():
    """
    Exercise 2: Most Common Elements
    Problem Statement:
        Write a Python program that takes a list of items and uses
        Counter.most_common(n) to find and print the top 3 most
        frequently occurring elements along with their counts.
    Purpose:
        Finding the top N most frequent elements is a classic problem in
        data analysis, log monitoring, and recommendation systems. The
        most_common() method solves it in one line without sorting
        manually, making this one of the most practically useful
        features of Counter.
    Given Input:
        items = ["apple", "banana", "apple", "cherry", "banana"
        , "apple", "date", "cherry", "banana", "apple"]
    Expected Output:
        apple: 4, banana: 3, cherry: 2
    """
    logger.info(f"Exercise 2: Most Common Elements")
    items = ["apple", "banana", "apple", "cherry", "banana"
        , "apple", "date", "cherry", "banana", "apple"]
    items_counter = Counter(items)
    most_frequent_items_counter = items_counter.most_common(n=3)
    logger.info(f"  Most Frequent Items: {most_frequent_items_counter}")
    pass



#########################################################################################
def exercise_03_counter_subtraction():
    """
    Exercise 3: Subtract Two Counters
    Problem Statement:
        Write a Python program that creates two Counter objects from
        two lists and subtracts one from the other to find the difference
        in element counts, then prints only the elements with a
        positive remaining count.
    Purpose:
        Counter arithmetic is useful in inventory management, stock
        reconciliation, and diff-checking tools where you need to
        know what remains after removing a set of items from a collection.
        This exercise highlights the difference between the - operator
        and the .subtract() method, which handle negative results
        differently.
    Given Input:
        stock = ["apple", "apple", "apple", "banana", "banana", "cherry"] and
        sold = ["apple", "apple", "banana", "cherry", "cherry"]
    Expected Output:
        apple: 1, banana: 1 (items with positive remaining count only)
    """
    logger.info(f"Exercise 3: Subtract Two Counters")
    stock = ["apple", "apple", "apple", "banana", "banana", "cherry"]
    sold = ["apple", "apple", "banana", "cherry", "cherry"]
    stock_counter = Counter(stock)
    sold_Counter = Counter(sold)
    message = "Remaining Items: "
    results = stock_counter - sold_Counter
    for item in results.items():
        message = message + f" {item[0]}: {item[1]},"
    logger.info(f"  {message[:-1]}")
    pass


#########################################################################################
def exercise_04_character_frequency_string():
    """
    Exercise 4: Character Frequency in a String
    Problem Statement:
        Write a Python program that uses Counter to count the frequency
        of every character in a given string, then prints only the
        alphabetic characters sorted from most to least frequent.
    Purpose:
        Character frequency analysis is foundational in cryptography,
        compression algorithms, language detection, and data validation.
        This exercise also reinforces filtering and sorting a Counter
        result, skills that extend naturally to any frequency-ranked
        output.
    Given Input:
        text = "hello world"
    Expected Output:
        Alphabetic characters sorted by frequency
        descending, e.g. l: 3, o: 2, h: 1, e: 1,
        w: 1, r: 1, d: 1
    """
    logger.info(f"Exercise 4: Character Frequency in a String")
    text = "hello world"
    resolved_text = re.sub(r'\s+', '', text)
    character_counter = Counter(resolved_text)
    logger.info(f"  {character_counter}")
    pass



#########################################################################################
def exercise_05_counter_addition():
    """
    Exercise 5: Combine Counters with Addition
    Problem Statement:
        Write a Python program that creates two Counter objects
        representing separate item inventories and combines them
         the + operator to produce a single merged total
         inventory.
    Purpose:
        Merging frequency maps is a common operation when aggregating
        data from multiple sources – such as combining sales figures
        from different stores, merging word counts from multiple
        documents, or consolidating log entries. The + operator on
        Counter handles this cleanly without manual looping.
    Given Input:
        warehouse_a = Counter({"apple": 50, "banana": 30, "cherry": 20}) and
        warehouse_b = Counter({"banana": 40, "cherry": 10, "date": 60})
    Expected Output:
        apple: 50, banana: 70, cherry: 30, date: 60
    """
    logger.info(f"Exercise 5: Combine Counters with Addition")
    warehouse_a = Counter({"apple": 50, "banana": 30, "cherry": 20})
    warehouse_b = Counter({"banana": 40, "cherry": 10, "date": 60})
    combined_warehouse_counts = warehouse_a + warehouse_b
    logger.info(f"  {combined_warehouse_counts}")
    pass



#########################################################################################
def exercise_06_group_words_by_first_letter():
    """
    Exercise 6: Group Words by First Letter
    Problem Statement:
        Write a Python program that takes a list of words and uses
        defaultdict(list) to group them alphabetically by their
        first letter, then prints each group.
    Purpose:
        Grouping items by a shared attribute is one of the most common
        data transformation tasks in programming. Using defaultdict(list)
        eliminates the need for repetitive if key not in dict checks
        before appending, resulting in cleaner and more readable
        grouping logic.
    Given Input:
        words = ["apple", "avocado", "banana", "blueberry", "cherry"
        , "apricot", "cranberry", "bluebell"]
    Expected Output:
        Each letter printed as a heading followed by the words
        starting with that letter, e.g. a: ['apple', 'avocado', 'apricot']
    """
    logger.info(f"Exercise 6: Group Words by First Letter")
    words = ["apple", "avocado", "banana", "blueberry", "cherry"
        , "apricot", "cranberry", "bluebell"]
    results = defaultdict(list)
    for word in words:
        results[word[0].lower()].append(word)
    for letter, items in sorted(results.items()):
        logger.info(f"  {letter}: {items} ")
    pass



#########################################################################################
def exercise_07_count_occurrences():
    """
    Exercise 7: Count Occurrences Without KeyError
    Problem Statement:
        Write a Python program that counts the occurrences of each item
        in a list using defaultdict(int), without any manual
        initialization of keys, and prints each item with its count.
    Purpose:
        Before Counter and defaultdict existed, counting with a plain
        dictionary required checking for key existence on every update.
        This exercise shows how defaultdict(int) solves that cleanly
        and helps you understand the underlying mechanism that
        Counter itself builds upon.
    Given Input:
        colours = ["red", "blue", "red", "green", "blue"
        , "blue", "red", "yellow"]
    Expected Output:
        red: 3, blue: 3, green: 1, yellow: 1
    """
    logger.info(f"Exercise 7: Count Occurrences Without KeyError")
    colours = ["red", "blue", "red", "green", "blue"
        , "blue", "red", "yellow"]
    results = defaultdict(int)
    for colour in colours:
        results[colour] += 1
    for color, count in results.items():
        logger.info(f"  {color}: {count} ")
    pass


#########################################################################################
def exercise_08_build_adjacency_list():
    """
    Exercise 8: Build an Adjacency List
    Problem Statement:
        Write a Python program that reads a list of directed edge
        pairs and uses defaultdict(list) to build and print an
        adjacency list representation of the graph.
    Purpose:
        The adjacency list is the most common way to represent graphs
        in software. It appears in network routing, social graph
        analysis, dependency resolution, and pathfinding algorithms.
        Using defaultdict(list) makes building one from a raw edge
        ist concise and free of key-existence boilerplate.
    Given Input:
        edges = [("A", "B"), ("A", "C"), ("B", "D")
        , ("C", "D"), ("D", "E")]
    Expected Output:
        Each node printed with its list of neighbours,
        e.g. A: ['B', 'C'], B: ['D'], C: ['D'], D: ['E']
    """
    logger.info(f"Exercise 8: Build an Adjacency List")
    edges = [("A", "B"), ("A", "C"), ("B", "D")
        , ("C", "D"), ("D", "E")]
    results = defaultdict(list)
    for src, tgt in edges:
        results[src].append(tgt)
    for k, v in results.items():
        logger.info(f"  {k}: {v} ")
    pass



#########################################################################################
def exercise_09_nested_defaultdict():
    """
    Exercise 9: Nested defaultdict
    Problem Statement:
        Write a Python program that uses a nested defaultdict to store a
        two-level dictionary representing departments and their employee
        names, then prints the full structure without manually creating
        any inner dictionaries.
    Purpose:
        Nested data grouping is a frequent requirement in reporting, configuration
        management, and data pipelines. A nested defaultdict eliminates the need
        to check whether an inner dictionary exists before writing to it,
        making multi-level data assembly significantly cleaner than with
        plain dictionaries.
    Given Input:
        A list of (department, employee) tuples: [("Engineering", "Alice")
        , ("Marketing", "Bob"), ("Engineering", "Charlie"), ("Marketing", "Diana")
        , ("HR", "Eve")]
    Expected Output:
        Each department printed as a heading followed by its employees
        and their placeholder data, e.g. Engineering: {'Alice': [], 'Charlie': []}
    """
    logger.info(f"Exercise 9: Nested defaultdict")
    results = defaultdict(lambda: defaultdict(list))
    department_info = [("Engineering", "Alice")
        , ("Marketing", "Bob"), ("Engineering", "Charlie"), ("Marketing", "Diana")
        , ("HR", "Eve")]
    # department_info_items = [(k, v) for k, v in department_info]
    # for k,v in department_info_items:
    # build the nested dictionary
    for k, v in department_info:
        results[k][v] = []
    # print the newly-created dictionary
    for k in sorted(results.keys()):
        logger.info(f"  {k}")
        for k, v in sorted(results[k].items()):
            logger.info(f"    {k}: {v}")

    pass


#########################################################################################
def exercise_10_use_set_with_default_dict():
    """
    Exercise 10: defaultdict with set
    Problem Statement:
        Write a Python program that takes a list of (student, subject) pairs
        and uses defaultdict(set) to collect all unique subjects each student
        is enrolled in, then prints each student’s subject list.
    Purpose:
        Using a set as the default value automatically deduplicates entries,
        which is ideal when the source data may contain repeated pairs. This
        pattern appears in access control systems, tag collections, and
        any scenario where you need to associate a key with a unique group
        of values rather than an ordered list.
    Given Input:
        enrolments = [("Alice", "Maths"), ("Bob", "Science"), ("Alice", "Science")
        , ("Alice", "Maths"), ("Bob", "Maths"), ("Charlie", "Science")]
    Expected Output:
        Each student with their unique subjects, e.g. Alice: {'Maths', 'Science'}
        , Bob: {'Science', 'Maths'}, Charlie: {'Science'}
    """
    logger.info(f"Exercise 10: defaultdict with set")
    results = defaultdict(set)
    enrollments = [("Thomas", "Physics"), ("Alice", "Maths"), ("Bob", "Science"), ("Alice", "Science")
        , ("Alice", "Maths"), ("Bob", "Maths"), ("Charlie", "Science")]
    for k, v in enrollments:
        results[k].add(v)
    for student, courses in sorted(results.items()):
        logger.info(f"  {student}: {sorted(courses)}")
    pass