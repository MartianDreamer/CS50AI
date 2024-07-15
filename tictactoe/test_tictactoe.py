from unittest import TestCase, main
from tictactoe import initial_state, player, actions, result, winner, X, O, EMPTY


class Tictactoe(TestCase):
    def test_player(self):
        board = initial_state()
        self.assertEqual(X, player(board))
        board[0][0] = X
        self.assertEqual(O, player(board))

    def test_action(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [X, O, X],
                 [O, X, O]]
        avail_actions = actions(board)
        self.assertListEqual([(0, 0), (0, 1), (0, 2)], avail_actions)

    def test_result(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [X, O, X],
                 [O, X, O]]
        self.assertRaises(ValueError, lambda: result(board, (-1, 0)))
        self.assertRaises(ValueError, lambda: result(board, (0, 4)))
        self.assertRaises(ValueError, lambda: result(board, (1, 0)))
        new_board = result(board, (0, 0))
        self.assertEqual(X, new_board[0][0])

    def test_winner(self):
        board = [[EMPTY, EMPTY, EMPTY],
                 [X, X, X],
                 [O, EMPTY, O]]
        the_winner = winner(board)
        self.assertEqual(X, the_winner)


if __name__ == "__main__":
    main()
