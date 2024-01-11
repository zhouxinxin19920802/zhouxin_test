[toc] 

##### **记录科研、生活**

2023年8月23日11:42:58

下午继续谋划无人集群运动模型小论文

This sentence uses `$` delimiters to show math inline:  $$ \sqrt{3x-1}+(1+x)^2 $$

##### **2023年8月23日15:33:54:**

通过上述代码验证出了github上也可以显示出公式

##### **2023年8月24日19:17:04**

今天晚上主要工作是完善简历。



1.基于战场、基于对手、基于联合作战的战区军事需求生成流程

1.1 军事需求结构化描述

1.2 军事需求体系视图建模

 	1.2.1 安全威胁视图

​	 1.2.2 制胜策略视图

​	 1.2.3 任务能力视图

​     1.2.4 能力到装备视图

1.3 基于作战环的军事需求生成方法

1.4 基于多目标优化的军事需求生成方法

##### **2023年8月25日10:36:57：**

还是不查了吧，踏踏实实做好现在的任务和科研

就是怕发现错误，所以不想看，其实就是怕面对错误

发现了markdown的一个优点

##### **2023年8月28日09:46:23:**

看下无人机的项目

关键词:集群对抗160

多域集群架构抗毁性与韧性研究:



智能集群

- 个体运动模型-
- 智能集群个体攻击模型
- 集群协同协作
- 态势评估
- 对抗策略

陆地域和空域对抗模型

空地协同 空域给陆域提供信息

**实现方式:**

Anylogic

场景：

- 多智能体仿真方法
  	- 对抗智能体
  	- 侦察智能体
  	- 固定智能体
  
  - 空域
    - 捣毁敌方基地
    - 争夺制空权

对于经常需要移动过来过去的，还是word更好点，word可以直接图片嵌入。

工作的时候还是不要带耳机的好，戴耳机影响工作效率。主要问题在于:听了音乐会切换音乐。



新建***Python3.5***的***conda***环境，执行如下命令：

```python
1.conda create -n py35 python=3.5.4

2.pip install gym==0.10.5

3.pip install pyglet==1.2.4

4.pip install tensorflow==1.8.0

5.python train.py
```

掌握多智能体强化学习 DQN算法，DDPG算法，Q-Learning算法

```python
parser.add_argument("--display", action="store_true", default=False)
```

控制动画显示，此代码能够控制模型，使其不训练

这段代码是一个用于训练多智能体强化学习模型的实现，特别是用于深度确定性策略梯度（DDPG）方法的多智能体版本，通常称为MADDPG（Multi-Agent Deep Deterministic Policy Gradients）。以下是代码的主要部分的功能解释：

1. `MADDPGAgentTrainer`类是一个智能体训练器，负责训练一个特定的智能体。

2. 初始化方法`__init__`接受一系列参数，包括智能体的名称（`name`）、模型（`model`）、观察空间形状（`obs_shape_n`）、动作空间大小（`act_space_n`）、智能体索引（`agent_index`）、训练参数（`args`）、是否使用本地Q函数（`local_q_func`）等。

   

3. 在初始化过程中，首先创建了观察输入占位符（`obs_ph_n`），用于接收智能体的观察信息。

4. 接下来，通过调用`q_train`和`p_train`函数创建了用于训练Q网络和策略网络的相关函数和操作。这些函数的输入包括智能体的名称、观察输入占位符、动作空间大小、Q函数和策略函数模型、优化器等。

5. 创建了经验缓冲区（`replay_buffer`），用于存储智能体的经验。缓冲区的最大长度由参数指定。

6. `action`方法接受一个观察输入，并返回智能体的动作。

7. `experience`方法用于将智能体的经验（包括观察、动作、奖励、下一个观察、是否完成等）存储到经验缓冲区中。

8. `preupdate`方法在每次更新之前进行一些准备工作，但在提供的代码中没有具体实现。

9. `update`方法是整个训练过程的核心。它在每个时间步骤（`t`）被调用，但只有在满足一定条件（缓冲区大小足够大且每100个时间步骤进行一次更新）时才执行。在这个方法中，执行以下操作：

   - 从经验缓冲区中随机采样一批经验数据。
   - 计算目标Q值，用于训练Q网络。
   - 计算Q网络的损失（`q_loss`）和策略网络的损失（`p_loss`）。
   - 执行Q网络和策略网络的训练更新操作。
   - 返回一些训练过程中的信息，如Q值损失、策略损失、目标Q值均值、奖励均值、目标Q值的均值和标准差。

总之，这段代码是一个用于训练多智能体MADDPG模型的训练器实现，它定义了智能体的行为、经验存储和训练更新等功能。在训练过程中，它通过最小化Q网络和策略网络的损失来优化智能体的策略，以实现多智能体协同决策的目标

```python
env.action_space   		
# 查看这个环境中可用的action有多少个，返回Discrete()格式
env.observation_space   
# 查看这个环境中observation的特征，返回Box()格式
n_actions=env.action_space.n 
# 查看这个环境中可用的action有多少个，返回int
n_features=env.observation_space.shape[0] 
# 查看这个环境中observation的特征有多少个，返回int
```

agent.experience 添加

```python
def experience(self, obs, act, rew, new_obs, done, terminal):
    # Store transition in the replay buffer.
    self.replay_buffer.add(obs, act, rew, new_obs, float(done))
def add(self, obs_t, action, reward, obs_tp1, done):
    data = (obs_t, action, reward, obs_tp1, done)

    if self._next_idx >= len(self._storage):
        self._storage.append(data)
    else:
        self._storage[self._next_idx] = data
        self._next_idx = (self._next_idx + 1) % self._maxsize
```

World类定义在core.py中，

```python
class World(object):
    def __init__(self):
        # list of agents and entities (can change at execution-time!)
        self.agents = []
        self.landmarks = []
        # communication channel dimensionality
        self.dim_c = 0
        # position dimensionality
        self.dim_p = 2
        # color dimensionality
        self.dim_color = 3
        # simulation timestep
        self.dt = 0.1
        # physical damping
        self.damping = 0.25
        # contact response parameters
        self.contact_force = 1e+2
        self.contact_margin = 1e-3
   def step(self):
        # set actions for scripted agents 
        for agent in self.scripted_agents:
            agent.action = agent.action_callback(agent, self)
        # gather forces applied to entities
        p_force = [None] * len(self.entities)
        # apply agent physical controls
        p_force = self.apply_action_force(p_force)
        # apply environment forces
        p_force = self.apply_environment_force(p_force)
        # integrate physical state
        self.integrate_state(p_force)
        # update agent state
        for agent in self.agents:
            self.update_agent_state(agent)
```

环境特性的一些定义

----------------------------------------------

$Trainer.step$ 里面包含World里step的更新

World类在core.py

其中  **self.update_agent_state(agent)**

World是在env = make_env(arglist.scenario, arglist, arglist.benchmark)确定环境

该算法在make_world()，在每个场景的代码中。，

```python
class Scenario(BaseScenario):
    def make_world(self):
        world = World()
        # set any world properties first
        world.dim_c = 2
        num_good_agents = 1
        num_adversaries = 3
        num_agents = num_adversaries + num_good_agents
        num_landmarks = 2
        # add agents
        world.agents = [Agent() for i in range(num_agents)]
        for i, agent in enumerate(world.agents):
            agent.name = 'agent %d' % i
            agent.collide = True
            agent.silent = True
            agent.adversary = True if i < num_adversaries else False
            agent.size = 0.075 if agent.adversary else 0.05
            agent.accel = 3.0 if agent.adversary else 4.0
            #agent.accel = 20.0 if agent.adversary else 25.0
            agent.max_speed = 1.0 if agent.adversary else 1.3
        # add landmarks
        world.landmarks = [Landmark() for i in range(num_landmarks)]
        for i, landmark in enumerate(world.landmarks):
            landmark.name = 'landmark %d' % i
            landmark.collide = True
            landmark.movable = False
            landmark.size = 0.2
            landmark.boundary = False
        # make initial conditions
        self.reset_world(world)
        return world
```

Agent和Entity的关系

Agent继承Entity并添加一些属性。

Environment是通过四个回调函数，来和scenario结合在一起。

 U.initialize()

```python
def initialize():
    """Initialize all the uninitialized variables in the global scope."""
    new_variables = set(tf.global_variables()) - ALREADY_INITIALIZED
    get_session().run(tf.variables_initializer(new_variables))
    ALREADY_INITIALIZED.update(new_variables)
```

```python
    self.action_space = [] // 动作空间  
    self.observation_space = [] // 观察空间
        for agent in self.agents:
            total_action_space = []
            # physical action space
            if self.discrete_action_space:
                u_action_space = spaces.Discrete(world.dim_p * 2 + 1)
            else:
                u_action_space = spaces.Box(low=-agent.u_range, high=+agent.u_range, shape=(world.dim_p,), dtype=np.float32)
            if agent.movable:
                total_action_space.append(u_action_space)
            # communication action space
            if self.discrete_action_space:
                c_action_space = spaces.Discrete(world.dim_c)
            else:
                c_action_space = spaces.Box(low=0.0, high=1.0, shape=(world.dim_c,), dtype=np.float32)
            if not agent.silent:
                total_action_space.append(c_action_space)
            # total action space
            if len(total_action_space) > 1:
                # all action spaces are discrete, so simplify to MultiDiscrete action space
                if all([isinstance(act_space, spaces.Discrete) for act_space in total_action_space]):
                    act_space = MultiDiscrete([[0, act_space.n - 1] for act_space in total_action_space])
                else:
                    act_space = spaces.Tuple(total_action_space)
                self.action_space.append(act_space)
            else:
                self.action_space.append(total_action_space[0])
            # observation space
            obs_dim = len(observation_callback(agent, self.world))
            self.observation_space.append(spaces.Box(low=-np.inf, high=+np.inf, shape=(obs_dim,), dtype=np.float32))
            agent.action.c = np.zeros(self.world.dim_c)
```

simple.py

```python
  def observation(self, agent, world):
        # get positions of all entities in this agent's reference frame
        entity_pos = []
        for entity in world.landmarks:
            entity_pos.append(entity.state.p_pos - agent.state.p_pos)
        //  当前个体的速度以及和周边路标之间的距离
        return np.concatenate([agent.state.p_vel] + entity_pos)
```

dim_c: 通讯通道

obs_n = env.reset()

 \# position dimensionality

 self.dim_p = 2  位置尺寸

```python
def reset(self):
        # reset world
        self.reset_callback(self.world)
        # reset renderer
        self._reset_render()
        # record observations for each agent
        obs_n = []
        self.agents = self.world.policy_agents
        for agent in self.agents:
            obs_n.append(self._get_obs(agent))
        return obs_n
// 实际是这个位置
def observation(self, agent, world):
        # get positions of all entities in this agent's reference frame
        entity_pos = []
        for entity in world.landmarks:
            entity_pos.append(entity.state.p_pos - agent.state.p_pos)
        return np.concatenate([agent.state.p_vel] + entity_pos)    
```

action是Trainer的方法，在maddpg.py文件中

obs是个体的速度和位置

obs_n和obs_shape_n是两个东西

env在进行step时在计算reward时，会利用到环境的reward，在每个step时，每个个体都会包含环境计算的信息。

environment属于多智能体环境







思路:目标倾向权重、可视角、加速度的自学习

env 就是couzin模型，计算下一个个体的位置。

强化学习流程(可视角w、可视角、速度)

////////////////////////////////////////////////

1.环境包含的信息，环境初始化信息，observation函数，reward函数，环境还需要包含动作空间，观察空间。

​    环境定义了各智能体的初始位置，速度等，要观测的是什么数据，要怎么奖励，奖励函数是什么？观测数据怎么存？奖励数据怎么存？

2.Trainer包含的信息

   神经网络模型，policy 神经网络用于输出动作，Q用于输出价值

####################

**Q函数和环境的reward函数是什么关系？**

  



多智能体强化学习流程:

1.给每个个体初始化动作空间倾向权重w，可视角$\theta $ , 加速度a的动作空间，w为[0,1]

2.个体初始工作空间 obs=[邻域内个体位置和速度]

3.初始化神经网络结构

4.动作空间执行后，根据(空间连通度，空间相关度、时间相关度，防撞效果)进行reward，到达率reward 设置

for 循环

​     各个个体根据当前状态计算action_n ,action_n = [每个个体w，可视角，加速度系数] 第一次的动作是根据初始化的环境状态计算出来的, 现在的act没搞明白是怎么搞的？这个act是怎么计算出来的？

​     // 计算一个step

​     env 计算所有个体的速度位置，共享奖励[奖励和]

​     执行experience，**用Trainer的relay buffer存储，存储每个[之前所有的观察状态，之前所有的动作状态，之前所 有个体的奖励，执行动作后所有个体的状态]**

​     清空每个个体的index空间

​     为每个trainer更新 

-------------------------------------------

接下来需要搞清楚的，trainer是怎么更新的

obs_n 和 newobs_n

--------------------------------------

1.每100个step更新一次

2.批采样报告

3.采样

4.for 

​	   计算所有个体动作序列

​       计算所有个体的的q值

​       奖励值 = 当前奖励值  + 衰减的q预测值 

​       计算平均奖励值

​       q_train 计算 loss

​       p_train 计算 loss

​       更新p网络参数

​       更新q网络参数

​       返回[q_loss, p_loss, 平均目标q值，当前状态奖励，下一个状态的平均目标q值]



 搞清楚relay buffer里面到底存的是什么？

 relay_buffer的长度 为1000000

为每个智能体创造一个relaybuffer，每一个step更新一次。

[agent1,agent2,agent3,agent1,agent2,agent3]

 batch-size是1024个

Word类在core.py文件中

action_space  存储的是数值空间

observation_space空间 存储的是Box类

```PYthon
obs_n = env.reset()
logging.info("obs_n:{}".format(obs_n))
2023-09-21 14:15:20,618 - train.py[line:142] - INFO: obs_n:[array([0.        , 0.        , 1.33978714, 0.58702214])]
速度为0，所有个体的位置结合
```

所以p_train和q_train最主要的功能是定义函数，









P_train函数

loss函数的设计:

```python
loss = pg_loss + p_reg * 1e-3
```

pg_loss是q网络的输出取负，p_reg是p网络的输出

p_train函数

1.返回值

act:动作函数(输入的是观察空间，输入policy函数的输出)

Train:函数(输入的是观察空间+动作空间，输出的是loss函数)

update_target_p: 目标网络参数

p_values:  p 网络的输出

target_act:  目标网络的输出



q_train函数

Train:函数(输入的是观察空间+动作空间，输出的是loss函数)

update_target_q: 目标q网络参数

'q_values': q网络参数(输入的是观察空间+动作空间，输入的是Q值)

‘target_q_values:’ q网络参数(输入的是观察空间+动作空间，输入的是Q值)







x x ：小车在轨道上的位置（position of the cart on the track）
θ \theta ：杆子与竖直方向的夹角（angle of the pole with the vertical）
x ˙ \dot{x} ：小车速度（cart velocity）
θ ˙ \dot{\theta } ：角度变化率（rate of change of the angle）

{小车在轨道位置，杆子与竖直方向夹角，小车速度，角度变化率}


$$
H ( p , q ) = − ∑ i P ( i ) log ⁡ Q ( i ) H\left( {p,q} \right) = - \sum\limits_i {P\left( i \right)\log Q\left( i \right)} 
$$








大论文架构

1.绪论

2.无人集群运动模型/速度、最小路集指标家族

3.无人集群韧性评估框架/无人集群韧性评估指标

4.考虑不完全失效的无人集群韧性评估

​	4.1 无人集群个体失效模型

​	3.2 无人集群失效策略

​	3.3 考虑速度为核心的无人集群韧性评估

​	3.4 考虑通信的无人集群韧性评估

   	  3.4.1 最小路集快速搜索方法

​    	 3.4.2 考虑通信的无人集群韧性评估

​    3.5 速度韧性与通讯韧性关系分析

5.基于韧性重要度的无人集群优化

6.基于强化学习的无人集群优化

​	6.1  无人集群模型的自适应机制

​    6.2  强化学习模型设计

​    6.3  不同参数下的模型表现

​    6.4  讨论

7.总结



​     

​     



**2023年9月13日21:22:37**

1. 需求案例报告
2. 多智能体强化学习代码
3. 纪念堂

2023年9月20日19:02:58

1.追击模型

2.逃跑模型

   







2023年11月14日10:21:32:

maddpg算法的地址:

1. reinforc_couzin

​       E:\zhouxin\reinforce_couzin

2. Maddpg包括maddpg tensorflow版本，pytorch版本，多粒子环境

​      E:\zhouxin\test\maddpg



三个问题:

1.average score 520的问题，单个个体到达的奖励为50，所以

2.到达终点大规模奖励

3.步长怎么设置，要设多长？

在原始的Maddpg算法中，其中包含了两种角色:



Gpu版本的pytorch安装

```
pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0 -f https://download.pytorch.org/whl/cu116/torch_stable.html
```

Cpu版本的pytorch安装

```
pip install torch==1.13.0+cpu torchvision==0.14.0+cpu torchaudio==0.13.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html
```

记住pytorch安装的一个关键网址：

```
https://download.pytorch.org/
```



**2024年1月10日16:51:47**

1.多状态网络可靠性评估软件的设计

多状态网络可靠性评估软件运行起来
