import helpers

print(helpers.is_even(4)) # True
print(helpers.average([1, 2, 3, 4, 5])) # 3.0

def main():
    numbers = [10, 15, 20, 25, 30]
    even_numbers = [num for num in numbers if helpers.is_even(num)]
    avg = helpers.average(numbers)

    print(f"Even numbers: {even_numbers}")
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()