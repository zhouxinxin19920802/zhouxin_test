import numpy as np
import torch as T
import gym
from gym.spaces import Box, Discrete, Dict, Tuple, MultiBinary, MultiDiscrete,Sequence
from  gym.spaces.utils import  flatdim
# space = Dict({"position": Discrete(2), "velocity": Discrete(3)})
# print(flatdim(space))

# state = np.array([])
# a = np.array([1,2,3,4])
# b = np.array([1,2,5,4])
# cons = np.concatenate([state,a])
# cons = np.concatenate([cons,b])
# print(cons)

cons = T.rand(5)
print(cons)