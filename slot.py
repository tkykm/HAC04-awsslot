# -*- coding: utf-8 -*-

import random

class Slot:
  AWS_SERVICES = [
    "s3",
    "cloudfront",
    "lambda",
    "iam"
  ]
  def __init__(self):
    self._state = [
      [None,None,None],
      [None,None,None],
      [None,None,None]
    ]
  
    return

  def game(self):
    for i in range(3):
      for j in range(3):
        self._state[i][j] = {'name': random.choice(Slot.AWS_SERVICES)}
        print(self._state)
    return self._state

if __name__ == "__main__":
  slot = Slot()
  print(slot.game())
  

