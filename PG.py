"""
@ Author: Peter Xiao
@ Date: 2020.7.20
@ Filename: PG.py
@ Brief: 使用 蒙特卡洛策略梯度Reinforce训练CartPole-v0
"""

import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import random
import time
from collections import deque
import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='test_log.txt',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

# Hyper Parameters for PG Network
GAMMA = 0.95  # discount factor
LR = 0.01  # learning rate

# Use GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# torch.backends.cudnn.enabled = False  # 非确定性算法


class PGNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PGNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, 20)
        self.fc2 = nn.Linear(20, action_dim)

    def forward(self, x):
        out = F.relu(self.fc1(x))
        out = self.fc2(out)
        return out

    def initialize_weights(self):
        for m in self.modules():
            nn.init.normal_(m.weight.data, 0, 0.1)
            nn.init.constant_(m.bias.data, 0.01)
            # m.bias.data.zero_()


class PG(object):
    # dqn Agent
    def __init__(self, env):  # 初始化
        # 状态空间和动作空间的维度
        self.state_dim = env.observation_space.shape[0]
        self.action_dim = env.action_space.n

        # init N Monte Carlo transitions in one game
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []

        # init network parameters
        self.network = PGNetwork(state_dim=self.state_dim, action_dim=self.action_dim).to(device)
        self.optimizer = torch.optim.Adam(self.network.parameters(), lr=LR)

        # init some parameters
        self.time_step = 0

    def choose_action(self, observation):
        # logging.info("observation  :{}".format(observation))
        observation = torch.FloatTensor(observation)
        network_output = self.network.forward(observation)
        # logging.info("network_output:{}".format(network_output))
        with torch.no_grad():
            prob_weights = F.softmax(network_output, dim=0).numpy()
        # logging.info("prob_weights:{}".format(prob_weights))
        # prob_weights = F.softmax(network_output, dim=0).detach().numpy()
        action = np.random.choice(range(prob_weights.shape[0]),
                                  p=prob_weights)  # select action w.r.t the actions prob
        # logging.info("action:{}".format(action))
        return action

    # 将状态，动作，奖励这一个transition保存到三个列表中
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)

    def learn(self):
        self.time_step += 1

        # Step 1: 计算每一步的状态价值
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        logging.info("self.ep_rs:{}".format(self.ep_rs))
        logging.info("discounted_ep_rs:{}".format(discounted_ep_rs))
        running_add = 0
        # 注意这里是从后往前算的，所以式子还不太一样。算出每一步的状态价值
        # 前面的价值的计算可以利用后面的价值作为中间结果，简化计算；从前往后也可以
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * GAMMA + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        logging.info("discounted_ep_rs:{}".format(discounted_ep_rs))

        discounted_ep_rs -= np.mean(discounted_ep_rs)  # 减均值
        discounted_ep_rs /= np.std(discounted_ep_rs)  # 除以标准差
        discounted_ep_rs = torch.FloatTensor(discounted_ep_rs).to(device)
        logging.info("discounted_ep_rs:{}".format(discounted_ep_rs))

        # Step 2: 前向传播
        softmax_input = self.network.forward(torch.FloatTensor(self.ep_obs).to(device))
        # all_act_prob = F.softmax(softmax_input, dim=0).detach().numpy()
        logging.info("softmax_input:{}".format(softmax_input))
        logging.info("self.ep_as:{}".format(self.ep_as))
        neg_log_prob = F.cross_entropy(input=softmax_input, target=torch.LongTensor(self.ep_as).to(device),
                                       reduction='none')
        logging.info("neg_log_prob:{}".format(neg_log_prob))
        # Step 3: 反向传播
        logging.info("discounted_ep_rs:{}".format(discounted_ep_rs))
        loss = torch.mean(neg_log_prob * discounted_ep_rs)
        logging.info("loss:{}".format(loss))
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # 每次学习完后清空数组
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []


# ---------------------------------------------------------
# Hyper Parameters
ENV_NAME = 'CartPole-v1'
EPISODE = 3000  # Episode limitation
STEP = 300  # Step limitation in an episode
TEST = 10  # The number of experiment test every 100 episode


def main():
    # initialize OpenAI Gym env and dqn agent
    env = gym.make(ENV_NAME)
    N_ACTIONS = env.action_space.n  # 杆子动作个数 (2个)
    logging.info("N_ACTIONS :{}".format(N_ACTIONS))
    N_STATES = env.observation_space.shape[0]  # 杆子状态个数 (4个)
    logging.info("N_STATES  :{}".format(N_STATES))
    agent = PG(env)

    for episode in range(EPISODE):
        # initialize task
        state = env.reset()

        observation = state[0]
        state = np.array(observation, dtype=np.float32)
        # Train
        # 只采一盘？N个完整序列
        for step in range(STEP):
            # logging.info("state:{},{}".format(state,STEP))
            action = agent.choose_action(state)  # softmax概率选择action
            # logging.info("action:{}".format(action))
            # logging.info("env.step(action):{}".format(env.step(action)))
            next_state, reward, done, _ , _ = env.step(action)
            agent.store_transition(state, action, reward)  # 新函数 存取这个transition
            state = next_state
            if done:
                print("stick for ",step, " steps")
                agent.learn()  # 更新策略网络
                break

        # Test every 100 episodes
        if episode % 100 == 0:
            total_reward = 0
            for i in range(TEST):
                state = env.reset()
                observation = state[0]
                state = np.array(observation, dtype=np.float32)
                for j in range(STEP):
                    env.render()
                    action = agent.choose_action(state)  # direct action for test
                    state, reward, done, _, _ = env.step(action)
                    total_reward += reward
                    if done:
                        break
            ave_reward = total_reward / TEST
            print('episode: ', episode, 'Evaluation Average Reward:', ave_reward)


if __name__ == '__main__':
    time_start = time.time()
    main()
    time_end = time.time()
    print('The total time is ', time_end - time_start)

