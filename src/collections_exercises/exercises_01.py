import logging
#
# https://pynative.com/python-collections-module-exercises/
# Exercises 11 through 20
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#########################################################################################
def exercise_11_preserve_insertion_order():
    """
    Exercise 11: Preserve Insertion Order
    Problem Statement:
        Write a Python program that creates an OrderedDict from a list
        of key-value pairs and demonstrates that iteration always
        reflects the original insertion order, even after accessing
        individual keys.
    Purpose:
        While Python 3.7 and later guarantee insertion order for regular
        dicts, OrderedDict remains relevant because it makes the ordering
        guarantee explicit in the code’s intent, supports additional
        order-aware methods like move_to_end(), and behaves differently
        in equality comparisons – as shown in Exercise 14. This exercise
        builds the foundation for the more advanced OrderedDict
        exercises that follow.
    Given Input:
        pairs = [("banana", 3), ("apple", 5), ("cherry", 1)
               , ("date", 8), ("elderberry", 2)]
    Expected Output:
        Keys and values printed in insertion order:
            banana: 3, apple: 5, cherry: 1, date: 8, elderberry: 2
    """
    logger.info(f"Exercise 11: Preserve Insertion Order")
    pass


#########################################################################################
def exercise_12_move_to_end():
    """
    Exercise 12: Move to End
    Problem Statement:
        Write a Python program that creates an OrderedDict of tasks, then
        uses move_to_end() to promote one task to the front and demote
        another to the back, printing the order before and after
        each operation.
    Purpose:
        Repositioning elements within an ordered collection is central to
        priority queues, recently-used lists, and scheduling systems.
        move_to_end() performs this in-place in O(1) time, making it far
        more efficient than deleting and re-inserting a key in a plain
        dictionary.
    Given Input:
        tasks = [("task_1", "Write tests"), ("task_2", "Fix bug")
        , ("task_3", "Deploy"), ("task_4", "Code review")
        , ("task_5", "Update docs")]
    Expected Output:
        The task list printed three times: original order,
        after moving task_3 to the front, and after
        moving task_1 to the back.
    """
    logger.info(f"Exercise 12: Move to End")
    pass



#########################################################################################
def exercise_13_implement_single_cache():
    """
    Exercise 13: Implement a Simple LRU Cache
    Problem Statement:
        Write a Python program that implements a basic Least Recently
        Used (LRU) cache using OrderedDict. The cache should store up
        to a fixed number of entries and automatically evict the least
        recently used item when the limit is exceeded.
    Purpose:
        LRU caches are used in web browsers, database query caches,
        CDN layers, and CPU memory management to keep frequently
        accessed data in fast storage while discarding stale entries.
        Building one with OrderedDict is a classic interview question
        that demonstrates mastery of both data structure selection
        and cache eviction logic.
    Given Input:
        A cache with capacity = 3, followed by a sequence of get
        and put operations that triggers at least one eviction.
    Expected Output:
        Cache state printed after each operation showing
        which items are present and which was evicted.
    """
    logger.info(f"Exercise 13: Implement a Simple LRU Cache")
    pass


#########################################################################################
def exercise_14_compare_ordered_dicts():
    """
    Exercise 14: Compare Two OrderedDicts
    Problem Statement:
        Write a Python program that demonstrates the difference in
        equality behaviour between two regular dicts and two OrderedDict
        objects that contain the same keys and values but in different
        insertion orders.
    Purpose:
        Understanding how equality works for OrderedDict versus dict
        prevents subtle bugs in code that compares configurations,
        serialised records, or cached results where insertion order
        may differ. This is one of the most commonly misunderstood
        behaviours of OrderedDict.
    Given Input:
        Two dictionaries and two OrderedDict objects,
        each containing {"a": 1, "b": 2, "c": 3}
        but constructed in different key orders.
    Expected Output:
        dict equality: True and OrderedDict equality: False
    """
    logger.info(f"Exercise 14: Compare Two OrderedDicts")
    pass



#########################################################################################
def exercise_15_reverse_ordered_dict():
    """
    Exercise 15: Reverse an OrderedDict
    Problem Statement:
        Write a Python program that creates an OrderedDict and iterates over
        it in reverse order using reversed(), printing key-value pairs
         last inserted to first inserted.
    Purpose:
        Reverse iteration over an ordered collection is useful when displaying
        recent history, processing a stack of operations in reverse, or
        presenting results in descending insertion sequence. OrderedDict
        supports reversed() directly, whereas reversing a plain dict
        requires converting it to a list first in older Python versions.
    Given Input:
        steps = [("step_1", "Load data"), ("step_2", "Clean data")
        , ("step_3", "Analyse"), ("step_4", "Visualise")
        , ("step_5", "Export")]
    Expected Output:
        Steps printed in reverse insertion order from
        step_5 down to step_1.
    """
    logger.info(f"Exercise 15: Reverse an OrderedDict")
    pass


#########################################################################################
def exercise_16_basic_deque_operations():
    """
    Exercise 16: Basic deque Operations
    Problem Statement:
        Write a Python program that creates a deque from a list and demonstrates
        the four core operations: append(), appendleft(), pop(), and popleft(),
        printing the deque state after each operation.
    Purpose:
        A deque (double-ended queue) supports O(1) insertions and removals from
        both ends, unlike a list where inserting or removing from the front is O(n).
        Understanding the four core operations is essential before using deque in
        queues, stacks, sliding windows, and history buffers covered
        in subsequent exercises.
    Given Input:
        initial = [2, 3, 4]
    Expected Output:
        The deque state printed after each of the six operations showing
        how items enter and leave from both ends.
    """
    logger.info(f"Exercise 16: Basic deque Operations")
    pass



#########################################################################################
def exercise_17_implement_fifo_queue():
    """
    Exercise 17: Implement a Queue (FIFO)
    Problem Statement:
        Write a Python program that simulates a customer service queue
        using a deque, where customers join at the back and are served
        from the front, printing the queue state after each operation.
    Purpose:
        A queue (First In, First Out) is one of the most fundamental data
        structures in computer science. It models real-world waiting lines,
        task schedulers, breadth-first search frontiers, and message
        buffers. Using deque instead of a list gives O(1) performance
        at both ends, making it the correct tool for queue implementation
        in Python.
    Given Input:
        A sequence of customer arrivals and service operations
        applied to an initially empty queue.
    Expected Output:
        The queue state printed after each arrival and each service event
        , showing customers entering at the back and leaving from the front.
    """
    logger.info(f"Exercise 17: Implement a Queue (FIFO)")
    pass


#########################################################################################
def exercise_18_implement_stack():
    """
    Exercise 18: Implement a Stack (LIFO)
    Problem Statement:
        Write a Python program that uses a deque to implement a stack
        where items are pushed onto and popped from the same end,
        simulating a browser back-navigation history.
    Purpose:
        A stack (Last In, First Out) underpins function call frames,
        expression evaluation, undo systems, and depth-first search.
        Although a plain Python list supports stack operations, using
        deque makes the intent explicit and consistent with the queue
        implementation, reinforcing the idea that deque can model
        both structures depending on which end is used.
    Given Input:
        A sequence of page visits and back-navigation
        events applied to an initially empty history stack.
    Expected Output:
        The stack state printed after each push and pop,
        showing pages added and removed from the same end.
    """
    logger.info(f"Exercise 18: Implement a Stack (LIFO)")
    pass



#########################################################################################
def exercise_19_rotate_deque():
    """
    Exercise 19: Rotating a deque
    Problem Statement:
        Write a Python program that creates a deque of tasks and uses
        deque.rotate(n) to shift the elements right by 2 positions and
        then left by 2 positions, printing the state after each rotation.
    Purpose:
        Rotation is useful in round-robin scheduling, circular buffer simulations,
        and any algorithm that needs to cycle through a fixed collection
        repeatedly. deque.rotate() performs the operation in O(n) time in a
        single method call, without needing to manually slice, concatenate,
        or reassign elements.
    Given Input:
        tasks = ["Design", "Develop", "Test", "Review", "Deploy"]
    Expected Output:
        Task list printed in original order, after
        rotating right by 2, and after rotating left by 2.
    """
    logger.info(f"Exercise 19: Rotating a deque")
    pass
    pass


#########################################################################################
def exercise_20_bounded_deque():
    """
    Exercise 20: Bounded deque for Recent History
    Problem Statement:
        Write a Python program that creates a deque with maxlen=5
        to simulate a recent browsing history buffer, demonstrating
        that adding a sixth item automatically discards the oldest
        entry.
    Purpose:
        A bounded deque is the simplest way to maintain a fixed-size
        sliding window of recent events without manually checking
        length or removing old entries. It appears in terminal
        command history, log tail buffers, moving average
        calculations, and any feature that shows “last N items”
        to the user.
    Given Input:
        A sequence of six page URLs added one at a time to a deque(maxlen=5).
    Expected Output:
        History buffer state after each addition, showing the
        oldest URL being dropped when the sixth is added.
    """
    logger.info(f"Exercise 20: Bounded deque for Recent History")
    pass