from mypackage import utilities


def main():
    greeting_message = utilities.greet("Alex")
    print(f"Greeting Output: {greeting_message}")

    number = 5
    fact_result = utilities.factorial(number)
    print(f"Factorial Output ({number}!): {fact_result}")


if __name__ == "__main__":
    main()
