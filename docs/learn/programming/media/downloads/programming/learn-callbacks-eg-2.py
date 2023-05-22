#!/usr/bin/env python

"""Threading in Python Example #1"""

import threading
import time


def callback_thread_current_count(arg_final_count, arg_current_count):
    print('[Callback] [Count to {} Thread] Current Count: {}'.format(
        arg_final_count, arg_current_count))


def callback_thread_compelte(arg_final_count):
    print('[Callback] [Count to {} Thread] Thread is complete.'.format(
        arg_final_count))


def count_to(arg_callback_complete, arg_callback_counting, arg_final_number, arg_sleep_duration):
    """Count to a number with sleep inbetween.

    Args:
            arg_final_number (int): Final number to count to.
            arg_sleep_duration (int): Sleep duration.
    """

    for i in range(1, arg_final_number + 1):
        arg_callback_counting(arg_final_number, i)
        time.sleep(arg_sleep_duration)

    arg_callback_complete(arg_final_number)


def main():
    """Main"""

    print("** Threading with Callbacks Example **")

    # 1. Create two threads
    t1 = threading.Thread(target=count_to, args=(
        callback_thread_compelte, callback_thread_current_count, 5, 1))
    
    t2 = threading.Thread(target=count_to, args=(
        callback_thread_compelte, callback_thread_current_count, 10, 0.25))

    # 2. Start the two threads
    t1.start()
    t2.start()

    # 3. Wait for the two threads to complete before moving to the next line.
    t1.join()
    t2.join()

    print("** Threading with Callbacks Done. **")


if __name__ == "__main__":
    main()
