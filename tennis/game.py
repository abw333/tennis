class Game:
  '''
  Python class for objects that represent tennis games.

  :param int server_points: number of points scored by the server
  :param int returner_points: number of points scored by the returner
  :var server_points: number of points scored by the server
  :var returner_points: number of points scored by the returner
  '''
  def __init__(self, server_points=0, returner_points=0):
    self.server_points = server_points
    self.returner_points = returner_points

  '''
  :return: True if the server won the game, False if the returner won the game, and None
           otherwise
  '''
  def winner(self):
    if self.server_points >= 4 and self.server_points - self.returner_points >= 2:
      return True

    if self.returner_points >= 4 and self.returner_points - self.server_points >= 2:
      return False

  '''
  Advances the game's score by a point.

  :param bool server: True if the server won the point, and False otherwise
  :return: True if the server won the game, False if the returner won the game, and None
           otherwise
  :raises RuntimeError: if the game's score cannot be advanced because the game is over
  '''
  def point(self, server):
    if self.winner() is not None:
      raise RuntimeError('Cannot advance this game\'s score because the game is over.')

    if server:
      self.server_points += 1
    else:
      self.returner_points += 1

    return self.winner()

  '''
  :return: a string representation of the game
  '''
  def __str__(self):
    return '{}(server_points={}, returner_points={})'.format(
      type(self).__name__,
      self.server_points,
      self.returner_points
    )