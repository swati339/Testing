def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument('a', type=int, help="The first number")
    parser.add_argument('b', type=int, help="The second number")

    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.a, args.b)
    elif args.operation == 'subtract':
        result = subtract(args.a, args.b)
    else:
        raise ValueError("Invalid.")

    print(f"The result of {args.operation} operation is: {result}")
    print(f"The result is: {result}")

if __name__ == '__main__':
    main()
