import numpy as np
import torch
from algorithm.dqn import DQN

class DQN_Agent:
    def __init__(self, args):
        self.args = args
        self.policy = DQN(args)

    def select_action(self, states, epsilon):
        # TODO: 补全epsilon_greedy代码实现
        if np.random.uniform() < epsilon:
            action = np.random.randint(len(states))
        else:
            inputs = torch.tensor(states, dtype=torch.float32).unsqueeze(0)
            if self.args.cuda:
                inputs = inputs.cuda()
            q_value = self.policy.q_network(inputs)
            action = q_value.max(1)[1].item()
        return action

    def learn(self, transitions, logger):
        self.policy.train(transitions, logger)