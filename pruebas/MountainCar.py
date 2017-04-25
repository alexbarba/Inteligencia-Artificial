import gym
env = gym.make('MountainCar-v0')
while (1):
	env.reset()
	for _ in range(100000000):
		env.render()
		env.step(env.action_space.sample()) # take a random action
