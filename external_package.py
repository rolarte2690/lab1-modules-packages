from colorama import Fore, Style, init


def main():
   
    init(autoreset=True)

    print(Fore.GREEN + "Success: The colorama package is installed and working!")
    print(Fore.CYAN + Style.BRIGHT + "External third-party libraries extend Python's capabilities.")
    print(Fore.YELLOW + "Warning example: Always verify your virtual environment before installing packages.")


if __name__ == "__main__":
    main()
