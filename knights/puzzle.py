from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

base_knowledge = And(
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    base_knowledge,
    Or(And(AKnave, Not(And(AKnave, AKnight))), And(AKnight, AKnave, AKnight))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    base_knowledge,
    Or(And(AKnight, AKnave, BKnave), And(AKnave, Not(And(AKnave, BKnave))))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    base_knowledge,
    Or(And(AKnight, Biconditional(AKnight, BKnight)), And(AKnave, Not(Biconditional(AKnight, BKnight)))),
    Or(And(BKnight, Biconditional(AKnight, BKnave)), And(BKnave, Not(Biconditional(AKnight, BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    base_knowledge,
    Or(
        And(BKnight, AKnight, AKnave),
        And(BKnight, AKnave, Not(AKnave)),
        And(BKnave, Not(And(AKnight, AKnave))),
        And(BKnave, Not(And(AKnave, Not(AKnave))))
    ),
    Or(And(BKnight, CKnave), And(BKnave, Not(CKnave))),
    Or(And(CKnight, AKnight), And(CKnave, Not(AKnight))),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
