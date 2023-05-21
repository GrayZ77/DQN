# DQN
NJU ML homework - DQN

第一次使用，直接运行main.py

运行结束之后，将argument.py中的--evaluate和--load_model均改为True，将runner.py 中
第 102 行 self.env.render()解除注释
随后，将model_log/MountainCar-v0中的模型拷贝到evaluate_model中，再次运行即可得到结果
