import random


def generate_random_numbers(count, start, end):

    return [random.randint(start, end) for _ in range(count)]


def calculate_average(numbers):

    return sum(numbers) / len(numbers)



def main():

    random_numbers = generate_random_numbers(15, 1, 100)


    average = calculate_average(random_numbers)


    print("Generated numbers:", random_numbers)
    print("Average:", average)


if __name__ == "__main__":
    main()