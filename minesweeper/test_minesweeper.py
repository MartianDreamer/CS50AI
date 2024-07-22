import unittest
import minesweeper

class MinesweeperAI_Test(unittest.TestCase):
    def test_make_random_move(self):
        ai = minesweeper.MinesweeperAI()
        move = ai.make_random_move()
        self.assertTrue(move[0] < 8 and move[0] >= 0 and move[1] < 8 and move[1] >= 0)
        for i in range(0, 8):
            for j in range(0, 7):
                ai.moves_made.add((i, j))
        move = ai.make_random_move()
        self.assertTrue(move[1] == 7)
        ai.moves_made.clear()
        for i in range(0, 8):
            for j in range(0, 7):
                ai.mines.add((i, j))
        move = ai.make_random_move()
        self.assertTrue(move[1] == 7)
        


if __name__ == "__main__":
    unittest.main()