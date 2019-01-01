import unittest

import tennis

class Set(unittest.TestCase):
  def test_init_no_args(self):
    zet = tennis.Set()

    self.assertEqual(zet.games, [tennis.Game(0, 0)])
    self.assertEqual(zet.tiebreak, True)

  def test_init_args(self):
    zet = tennis.Set([tennis.Game(1, 2)], False)

    self.assertEqual(zet.games, [tennis.Game(1, 2)])
    self.assertEqual(zet.tiebreak, False)

  def test_init_kwargs(self):
    zet = tennis.Set(tiebreak=False, games=[tennis.Game(3, 4)])

    self.assertEqual(zet.games, [tennis.Game(3, 4)])
    self.assertEqual(zet.tiebreak, False)

  def test_first_server_games(self):
    self.assertEqual(tennis.Set([]).first_server_games(), 0)

    self.assertEqual(tennis.Set().first_server_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(0, 4)]).first_server_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(4, 0)]).first_server_games(), 1)

    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game()]).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(0, 4)]).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0)]).first_server_games(),
      0
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 0, 7)]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 7, 7)]
      ).first_server_games(),
      0
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(7, 0, 7)]
      ).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game()]).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4)]).first_server_games(),
      2
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(4, 0)]).first_server_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 0, 7)]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 7, 7)]
      ).first_server_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(7, 0, 7)]
      ).first_server_games(),
      2
    )

  def test_first_returner_games(self):
    self.assertEqual(tennis.Set([]).first_returner_games(), 0)

    self.assertEqual(tennis.Set().first_returner_games(), 0)
    self.assertEqual(tennis.Set([tennis.Game(0, 4)]).first_returner_games(), 1)
    self.assertEqual(tennis.Set([tennis.Game(4, 0)]).first_returner_games(), 0)

    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game()]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(0, 4)]).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0)]).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 0, 7)]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(0, 7, 7)]
      ).first_returner_games(),
      3
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(0, 4), tennis.Game(4, 0), tennis.Tiebreak(7, 0, 7)]
      ).first_returner_games(),
      2
    )

    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game()]).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4)]).first_returner_games(),
      0
    )
    self.assertEqual(
      tennis.Set([tennis.Game(4, 0), tennis.Game(4, 0)]).first_returner_games(),
      1
    )

    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 0, 7)]
      ).first_returner_games(),
      1
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(0, 7, 7)]
      ).first_returner_games(),
      2
    )
    self.assertEqual(
      tennis.Set(
        [tennis.Game(4, 0), tennis.Game(4, 0), tennis.Tiebreak(7, 0, 7)]
      ).first_returner_games(),
      1
    )

  def test_winner(self):
    self.assertIsNone(tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 0, 7)]).winner())

    self.assertTrue(tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(7, 0, 7)]).winner())

    self.assertFalse(tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 7, 7)]).winner())

    self.assertIsNone(tennis.Set([tennis.Game(4, 0)] * 10 + [tennis.Game()], False).winner())

    self.assertIsNone(tennis.Set([tennis.Game(4, 0)] * 11 + [tennis.Game()], False).winner())

    self.assertIsNone(tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Game()], False).winner())

    self.assertIsNone(tennis.Set([tennis.Game(4, 0)] * 13 + [tennis.Game()], False).winner())

    self.assertTrue(tennis.Set([tennis.Game(4, 0)] * 13 + [tennis.Game(0, 4)], False).winner())

    self.assertIsNone(
      tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Game(0, 4), tennis.Game()], False).winner()
    )

    self.assertFalse(
      tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Game(0, 4), tennis.Game(4, 0)], False).winner()
    )

  def test_point(self):
    with self.assertRaises(
      RuntimeError,
      msg='Cannot advance this set\'s score because the set is over.'
    ):
      tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4)] * 3).point(True)

    zet = tennis.Set()
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(3, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game()]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 3)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game()]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(3, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game()]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 3)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game()]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(3, 0)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game()]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 3)]))
    self.assertTrue(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4)]))

    zet = tennis.Set()
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 3)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game()]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(3, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game()]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 3)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game()]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(3, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game()]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 1)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 2)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 3)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game()]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(1, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(2, 0)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(3, 0)]))
    self.assertFalse(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0), tennis.Game(0, 4), tennis.Game(4, 0)]))

    zet = tennis.Set([tennis.Game(4, 0)] * 11 + [tennis.Game(3, 0)])
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(1, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(2, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(3, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(4, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(5, 0, 7)]))
    self.assertIsNone(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(6, 0, 7)]))
    self.assertTrue(zet.point(True))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(7, 0, 7)]))

    zet = tennis.Set([tennis.Game(4, 0)] * 11 + [tennis.Game(3, 0)])
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 0, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 1, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 2, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 3, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 4, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 5, 7)]))
    self.assertIsNone(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 6, 7)]))
    self.assertFalse(zet.point(False))
    self.assertEqual(zet, tennis.Set([tennis.Game(4, 0)] * 12 + [tennis.Tiebreak(0, 7, 7)]))

  def test_str(self):
    self.assertEqual(str(tennis.Set([], True)), 'Set(games=[], tiebreak=True)')
    self.assertEqual(
      str(tennis.Set([tennis.Game(1, 2)], False)),
      'Set(games=[Game(server_points=1, returner_points=2)], tiebreak=False)'
    )
    self.assertEqual(
      str(tennis.Set([tennis.Game(1, 2), tennis.Tiebreak(3, 4, 7)], True)),
      'Set(games=[Game(server_points=1, returner_points=2), Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)], tiebreak=True)'
    )

  def test_repr(self):
    self.assertEqual(repr(tennis.Set([], True)), 'Set(games=[], tiebreak=True)')
    self.assertEqual(
      repr(tennis.Set([tennis.Game(1, 2)], False)),
      'Set(games=[Game(server_points=1, returner_points=2)], tiebreak=False)'
    )
    self.assertEqual(
      repr(tennis.Set([tennis.Game(1, 2), tennis.Tiebreak(3, 4, 7)], True)),
      'Set(games=[Game(server_points=1, returner_points=2), Tiebreak(first_server_points=3, first_returner_points=4, target_points=7)], tiebreak=True)'
    )

  def test_eq(self):
    self.assertEqual(tennis.Set([], True), tennis.Set([], True))
    self.assertEqual(
      tennis.Set([tennis.Game(1, 2)], False),
      tennis.Set([tennis.Game(1, 2)], False)
    )
    self.assertNotEqual(tennis.Set([], True), tennis.Set([], False))
    self.assertNotEqual(tennis.Set([], True), tennis.Set([tennis.Game(1, 2)], True))

if __name__ == '__main__':
  unittest.main()
