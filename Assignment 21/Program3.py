"""
Design a Python application where multiple threads update a shared variable.
- Use a Lock to avoid race conditions.
- Each thread should increment the shared counter multiple times.
- Display the final value of the counter after all threads complete execution.
"""

import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter(num_increments):
    global counter
    for _ in range(num_increments):
        with counter_lock:
            counter += 1

def main():
    num_threads = 3
    increments_per_thread = 500

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(increments_per_thread,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")

if __name__ == "__main__":
    main()
