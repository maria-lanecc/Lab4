from boneyard import Boneyard
from domino import Domino

class BoneyardTest:
    @staticmethod
    def test_constructor():
        boneyard = Boneyard(max_dots=6)
        print(f"Testing constructor. Expect boneyard with 28 dominos. {boneyard}")
        print(f"Expect dominos_remaining property to be 28. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")

    @staticmethod
    def test_shuffle():
        boneyard = Boneyard(max_dots=6)
        boneyard.shuffle()
        print(f"Testing shuffle. Expect shuffled boneyard. {boneyard}")
        print(f"Expect dominos_remaining property to be 28. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")

    @staticmethod
    def test_draw():
        boneyard = Boneyard(max_dots=6)
        print(f"Testing draw. Expect boneyard with 28 dominos. {boneyard}")
        print(f"Expect dominos_remaining property to be 28. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")

        domino = boneyard.draw()
        print(f"After drawing a domino. Expect boneyard with 27 dominos. {boneyard}")
        print(f"Expect dominos_remaining property to be 27. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")
        print(f"Drawn domino: {domino}")

    @staticmethod
    def test_get_item():
        boneyard = Boneyard(max_dots=6)
        print(f"Testing __getitem__. Expect boneyard with 28 dominos. {boneyard}")
        print(f"Expect dominos_remaining property to be 28. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")

        domino = boneyard[4]
        print(f"Accessed domino at index 4. Expect boneyard to remain the same. {boneyard}")
        print(f"Expect dominos_remaining property to be 28. {boneyard.dominos_remaining}")
        print(f"Expect is_empty property to be false. {boneyard.is_empty}")
        print(f"Accessed domino: {domino}")

    @staticmethod
    def test_in_operator():
        boneyard = Boneyard(max_dots=6)
        domino1 = boneyard[0]
        domino2 = Domino(1, 1)
        print(f"Testing 'in' operator. {domino1} in boneyard? Expect True. {domino1 in boneyard}")
        print(f"{domino2} in boneyard? Expect False. {domino2 in boneyard}")

    @staticmethod
    def test_for_loop():
        boneyard = Boneyard(max_dots=6)
        print(f"Testing for loop. Iterating through the boneyard.")
        for domino in boneyard:
            print(domino)


