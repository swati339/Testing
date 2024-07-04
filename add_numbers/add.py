def add(a, b):
    return a + b

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument('a', type=int, help="The first number")
    parser.add_argument('b', type=int, help="The second number")

    args = parser.parse_args()
    result = add(args.a, args.b)
    print(f"The result is: {result}")

if __name__ == '__main__':
    main()
