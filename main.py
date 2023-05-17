from boneyardTests import *

def main():
    print("Running Boneyard Test Cases\n")

    print("Test Case: Constructor")
    BoneyardTest.test_constructor()
    print()

    print("Test Case: Shuffle")
    BoneyardTest.test_shuffle()
    print()

    print("Test Case: Draw")
    BoneyardTest.test_draw()
    print()

    print("Test Case: Get Item")
    BoneyardTest.test_get_item()
    print()

    print("Test Case: In Operator")
    BoneyardTest.test_in_operator()
    print()

    print("Test Case: For Loop")
    BoneyardTest.test_for_loop()

if __name__ == '__main__':
    main()
