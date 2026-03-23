def main():
    print("Hello from Python!")
    print("This script is executed by Jenkins.")

    total = 0
    for i in range(1, 6):
        total += i

    print(f"Sum of numbers from 1 to 5 is: {total}")

if __name__ == "__main__":
    main()
