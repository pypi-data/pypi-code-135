from pierl.agents.Actor_critics import A2C
from pierl.agents.DQN_based import DDQN, DQN, DQN_RS, DQN_TN
from pierl.agents.Policy_gradients import REINFORCE
from pierl.environments import easy, trumps
from pierl.networks import *


__all__ = ['A2C', 'DDQN', 'DQN', 'DQN_RS', 'DQN_TN', 'REINFORCE', 'easy', 'trumps']