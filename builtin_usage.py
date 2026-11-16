import math
import random
import platform


def main():
     rand_num = random.randint(1, 100)

    floored_sqrt = math.floor(math.sqrt(rand_num))

    os_name = platform.system()
    python_version = platform.python_version()

    print(f"Random Number: {rand_num}")
    print(f"Square Root (floored): {floored_sqrt}")
    print(f"Operating System: {os_name}")
    print(f"Python Version: {python_version}")


if __name__ == "__main__":
    main()
