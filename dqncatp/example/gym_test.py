import gym

env = gym.make('CartPole-v1')
env.reset()

while True:
    env.render()
    action = env.action_space.sample()
    env.step(action)
    