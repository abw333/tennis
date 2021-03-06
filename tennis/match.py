import tennis

class Match:
  '''
  Python class for objects that represent tennis matches.

  :param list sets: list of sets played in the match
  :param int target_sets: number of sets required to win the match
  :param int target_games: number of games required to win each set
  :param bool deciding_point: whether to play a deciding point at deuce
  :param int tiebreak_games: number of games each player must have before a tiebreak is played, or
                             None if a tiebreak is not to be played
  :param int tiebreak_points: number of points required to win a tiebreak, or None if a tiebreak is
                              not to be played
  :param int final_set_target_games: number of games required to win the final set
  :param bool final_set_deciding_point: whether to play a deciding point at deuce in the final set
  :param int final_set_tiebreak_games: number of games each player must have before a tiebreak is
                                       played in the final set, or None if a tiebreak is not to be
                                       played in the final set
  :param int final_set_tiebreak_points: number of points required to win a tiebreak in the final
                                        set, or None if a tiebreak is not to be played in the final
                                        set
  :var sets: list of sets played in the match
  :var target_sets: number of sets required to win the match
  :var target_games: number of games required to win each set
  :var deciding_point: whether to play a deciding point at deuce
  :var tiebreak_games: number of games each player must have before a tiebreak is played, or None if
                       a tiebreak is not to be played
  :var tiebreak_points: number of points required to win a tiebreak, or None if a tiebreak is not to
                        be played
  :var final_set_target_games: number of games required to win the final set
  :var final_set_deciding_point: whether to play a deciding point at deuce in the final set
  :var final_set_tiebreak_games: number of games each player must have before a tiebreak is played
                                 in the final set, or None if a tiebreak is not to be played in the
                                 final set
  :var final_set_tiebreak_points: number of points required to win a tiebreak in the final set, or
                                  None if a tiebreak is not to be played in the final set
  :var first_server_served_first: a tuple with a boolean for each set that indicates whether the
                                  player that served first in the first set also served first in
                                  that set
  :var winner: True if the first server won the match, False if the first returner won the match,
               and None otherwise
  '''
  def __init__(
    self,
    *,
    sets=None,
    target_sets=2,
    target_games=6,
    deciding_point=False,
    tiebreak_games=6,
    tiebreak_points=7,
    final_set_target_games=6,
    final_set_deciding_point=False,
    final_set_tiebreak_games=6,
    final_set_tiebreak_points=7
  ):
    # TODO(abw333): validate sets

    if target_sets < 1:
      raise RuntimeError('target_sets must be at least 1.')

    if min(target_games, final_set_target_games) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if (tiebreak_games is None) != (tiebreak_points is None):
      raise RuntimeError('tiebreak_games and tiebreak_points must both be None or non-None.')

    if (final_set_tiebreak_games is None) != (final_set_tiebreak_points is None):
      raise RuntimeError(
        'final_set_tiebreak_games and final_set_tiebreak_points must both be None or non-None.'
      )

    if tiebreak_games is not None and min(tiebreak_games, tiebreak_points) < 0:
      raise RuntimeError('Point scores must be non-negative.')

    if final_set_tiebreak_games is not None:
      if min(final_set_tiebreak_games, final_set_tiebreak_points) < 0:
        raise RuntimeError('Point scores must be non-negative.')

    if sets is not None:
      self.sets = sets
    elif target_sets == 1:
      self.sets = [tennis.Set(
        games=None,
        target_games=final_set_target_games,
        deciding_point=final_set_deciding_point,
        tiebreak_games=final_set_tiebreak_games,
        tiebreak_points=final_set_tiebreak_points
      )]
    else:
      self.sets = [tennis.Set(
        games=None,
        target_games=target_games,
        deciding_point=deciding_point,
        tiebreak_games=tiebreak_games,
        tiebreak_points=tiebreak_points
      )]

    self.target_sets = target_sets
    self.target_games = target_games
    self.deciding_point = deciding_point
    self.tiebreak_games = tiebreak_games
    self.tiebreak_points = tiebreak_points
    self.final_set_target_games = final_set_target_games
    self.final_set_deciding_point = final_set_deciding_point
    self.final_set_tiebreak_games = final_set_tiebreak_games
    self.final_set_tiebreak_points = final_set_tiebreak_points
    self.first_server_served_first = tuple(self._compute_first_server_served_first())
    self.winner = self._compute_winner()

  '''
  :return: yields a boolean for each set that indicates whether the player that served first in the
           first set also served first in that set
  '''
  def _compute_first_server_served_first(self):
    for i, zet in enumerate(self.sets):
      if not i:
        served_first = True
      elif len(self.sets[i - 1].games) % 2:
        served_first = not served_first

      yield served_first

  '''
  :return: the number of sets won by the player who served first
  '''
  def first_server_sets(self):
    return len([
      0 for fssf, s in zip(self.first_server_served_first, self.sets) if fssf == s.winner
    ])

  '''
  :return: the number of sets won by the player who returned first
  '''
  def first_returner_sets(self):
    return len([
      0 for fssf, s in zip(self.first_server_served_first, self.sets) if (not fssf) == s.winner
    ])

  '''
  :return: True if the first server won the match, False if the first returner won the match, and
           None otherwise
  '''
  def _compute_winner(self):
    if self.first_server_sets() == self.target_sets:
      return True

    if self.first_returner_sets() == self.target_sets:
      return False

  '''
  :return: True if the first server is to serve the next point, and False if the first returner
           is to serve the next point
  :raises RuntimeError: if no server is to serve the next point because the match is over
  '''
  def first_server_to_serve(self):
    if self.winner is not None:
      raise RuntimeError('No server is to serve the next point because the match is over.')

    return self.first_server_served_first[-1] == self.sets[-1].first_server_to_serve()

  '''
  Advances the match's score by a point.

  :param bool first_server: True if the first server won the point, and False otherwise
  :return: True if the first server won the match, False if the first returner won the match, and
           None otherwise
  :raises RuntimeError: if the match's score cannot be advanced because the match is over
  '''
  def point(self, *, first_server):
    if self.winner is not None:
      raise RuntimeError('Cannot advance this match\'s score because the match is over.')

    set_winner = self.sets[-1].point(
      first_server=list(self.first_server_served_first)[-1] == first_server
    )
    if set_winner is None:
      return None

    self.winner = self._compute_winner()

    if self.winner is not None:
      return self.winner

    if len(self.sets) == 2 * (self.target_sets - 1):
      self.sets.append(tennis.Set(
        games=None,
        target_games=self.final_set_target_games,
        deciding_point=self.final_set_deciding_point,
        tiebreak_games=self.final_set_tiebreak_games,
        tiebreak_points=self.final_set_tiebreak_points
      ))
    else:
      self.sets.append(tennis.Set(
        games=None,
        target_games=self.target_games,
        deciding_point=self.deciding_point,
        tiebreak_games=self.tiebreak_games,
        tiebreak_points=self.tiebreak_points
      ))

    self.first_server_served_first = tuple(
      list(self.first_server_served_first) + [
        self.first_server_served_first[-1] != bool(len(self.sets[-2].games) % 2)
      ]
    )

  '''
  :return: a string representation of the match
  '''
  def __str__(self):
    return ('{}('
      'sets={}, '
      'target_sets={}, '
      'target_games={}, '
      'deciding_point={}, '
      'tiebreak_games={}, '
      'tiebreak_points={}, '
      'final_set_target_games={}, '
      'final_set_deciding_point={}, '
      'final_set_tiebreak_games={}, '
      'final_set_tiebreak_points={}'
    ')').format(
      type(self).__name__,
      self.sets,
      self.target_sets,
      self.target_games,
      self.deciding_point,
      self.tiebreak_games,
      self.tiebreak_points,
      self.final_set_target_games,
      self.final_set_deciding_point,
      self.final_set_tiebreak_games,
      self.final_set_tiebreak_points,
    )

  '''
  :return: a string representation of the match
  '''
  def __repr__(self):
    return str(self)

  '''
  :param object other: object to compare to the match
  :return: True if the input object is equal to the match, and False otherwise
  '''
  def __eq__(self, other):
    return isinstance(other, type(self)) and self.__dict__ == other.__dict__
