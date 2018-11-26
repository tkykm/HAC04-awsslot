# -*- coding: utf-8 -*-

import random

class slot:
  AWS_SERVICES = [
    "s3",
    "cloudfront",
    "sns"
  ]
  def __init__(self):
    self._state = [[None for i in range(3)]] * 3
    return

  def game(self):
    for i in range(3):
      for j in range(3):
        self._state[i][j] = {'name': random.choice(AWS_SERVICES)}
 

