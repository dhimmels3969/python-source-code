import logging
import time
import functools


#
# https://pynative.com/python-exception-handling-exercises/
# Exercises 18
#
# Code copied from
# https://dwickyferi.medium.com/python-decorators-from-zero-to-hero-with-a-powerful-auto-retry-use-case-51e7bf73caae
#


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)




def auto_retry(retries=3, delay=1):
    """
    A decorator factory for retrying a function on failure.

    :param retries: The maximum number of attempts.
    :param delay: The delay in seconds between retries.
    """

    def decorator(func):
        """The actual decorator."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """The wrapper function that implements the retry logic."""

            # Start a loop for the number of retries
            for i in range(retries):
                try:
                    # Try to execute the original function
                    return func(*args, **kwargs)

                except Exception as e:
                    # If it fails, log the attempt
                    attempt = i + 1
                    logger.error(f"Attempt {attempt}/{retries} failed for '{func.__name__}': {e}")

                    # If this wasn't the last attempt, wait and try again
                    if attempt < retries:
                        # print(f"Retrying in {delay} second(s)...")
                        time.sleep(delay)
                    else:
                        # If this was the last attempt, log it and re-raise
                        logger.info("All retry attempts failed.")
                        raise e  # Re-raise the last exception

        return wrapper

    return decorator