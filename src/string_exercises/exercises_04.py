#
# Exercises found at web page https://pynative.com/python-string-exercise/
# Exercises 31 through 38
#
import string




#######################################################################################################
def exercise_31_remove_duplicate_characters():
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
    print("Exercise 31. Remove Duplicate Characters")
    str1 = "google"
    results = ""
    character_count_dict = {}
    for char in str1:
       if char not in character_count_dict:
           character_count_dict[char] = 1
           results += char

    print(results)
    pass



#######################################################################################################
def exercise_32_word_reversal():
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
    print("Exercise 32. Word Reversal")
    str1 = "Python is fun"
    results = ""
    word_list = str1.split()
    reversed_word_list = word_list[::-1]
    results = " ".join(reversed_word_list)
    print(results)
    pass



#######################################################################################################
def exercise_33_character_interleaving():
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
    def concatenate_string_equal_length(s1, s2):
        results = ""
        for i in range(len(s1)):
            results += s1[i]
            results += s2[i]
        return results

    def concatenate_string_unequal_length(s1, s2):
        pass

    print("Exercise 33. Character Interleaving")
    s1 = "ABC"
    s2 = "xyz"
    if len(s1) == len(s2):
        results = concatenate_string_equal_length(s1, s2)
    print(results)
    pass



#######################################################################################################
def exercise_34_longest_word():
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
    def find_longest_word(s1):
        word_list = s1.split()
        longest_length = 0
        longest_word = ""
        for word in word_list:
            if len(word) > longest_length:
                longest_length = len(word)
                longest_word = word
        return longest_word

    print("Exercise 34. Longest Word")
    str1 = "The quick brown fox jumps over the lazy dog"
    longest_word = find_longest_word(str1)
    print(f"Longest word: {longest_word}")

    str1 = "Round up the usual suspects"
    longest_word = find_longest_word(str1)
    print(f"Longest word: {longest_word}")
    pass



#######################################################################################################
def exercise_35_acronym_generator():
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
    def build_acronym(s1):
        acronym = ""
        word_list = s1.split()
        for word in word_list:
            acronym += word[0].upper()
        return acronym

    print("Exercise 35. Acronym Creator")
    str1 = "Random Access Memory"
    acronym = build_acronym(str1)
    print(acronym)

    str2 = "Burlington Northern Santa Fe"
    print(build_acronym(str2))
    pass



#######################################################################################################
def exercise_36_word_frequency():
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
    def remove_punctuation(input_text):
        output_text = ""
        for char in input_text:
            if char not in string.punctuation:
                output_text += char
        return output_text

    def build_frequency_map(s1):
        frequency_map = {}
        s1 = remove_punctuation(s1)
        word_list = s1.split()
        for word in word_list:
            if word.lower() not in frequency_map:
                frequency_map[word.lower()] = 1
            else:
                frequency_map[word.lower()] += 1
        # for key, value in frequency_map.items():
        #     text = key + ": " + str(value)
        return frequency_map

    print("Exercise 36. Word Frequency")
    str1 = "apple banana apple cherry banana apple"
    word_count_map = build_frequency_map(str1)
    print(word_count_map)
    print()

    # str2 = \
    #     "Of all tyrannies, a tyranny sincerely exercised for the good of its victims may be " \
    #     "the most oppressive. It would be better to live under robber barons than under omnipotent " \
    #     "moral busybodies. The robber baron's cruelty may sometimes sleep, his cupidity may at some " \
    #     "point be satiated; but those who torment us for our own good will torment us without end " \
    #     "for they do so with the approval of their own conscience."
    # word_count_map = build_frequency_map(str2)
    # print(word_count_map)
    pass



#######################################################################################################
def exercise_37_first_non_repeating_character():
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
    def build_frequency_map(s1):
        character_count_map = {}
        for char in s1:
            if char.lower() not in character_count_map:
                character_count_map[char.lower()] = 1
            else:
                character_count_map[char.lower()] += 1
        return character_count_map
    
    def find_first_unique_character(s1):
        first_unique_character = "?"
        character_count_map = build_frequency_map(s1)
        for key, value in character_count_map.items():
            if value == 1:
                first_unique_character = key
                break
        final_results = "No unique characters found."
        if first_unique_character != "?":
            final_results = first_unique_character
        return final_results

    print("Exercise 37. First Non-Repeating Character")
    str1 = "swiss"
    results = find_first_unique_character(str1)
    print(results)
    str1 = "Abraham"
    results = find_first_unique_character(str1)
    print(results)
    pass



#######################################################################################################
def exercise_38_string_rotation_check():
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
    def is_rotation(src, tgt):
        ##########################################################
        # from the pynative website... pretty innovative solution!
        ##########################################################
            # If you concatenate a string with itself (s1 + s1), it will contain every
            # possible rotation of that string. Then, simply check if s2 is a substring
            # of that doubled string.

            # # Double the first string
            # combined = tgt + tgt
            # # Check if src is inside the doubled version
            # return src in combined
        ##########################################################

        is_rotation = False
        # compare the 2 strings for equality before proceeding
        if src == tgt:
            is_rotation = True
        else:
            # for source move left-most byte to the end of the string
            # after each move, compare to target
            for i in range(len(src)):
                src = "".join([src[1:], src[0]])
                if src == tgt:
                    is_rotation = True
                    break
        return is_rotation

    def compare_strings_for_rotation(src, tgt):
        results = f"Is Rotation: {is_rotation(src, tgt)}"
        return results

    print("Exercise 38. String Rotation Check")
    print(compare_strings_for_rotation("waterbottle", "erbottlewat"))
    print(compare_strings_for_rotation("waterbottle", "ewaterbottl"))
    print(compare_strings_for_rotation("waterbottle", "erbottlwaat"))

    pass







