from imports import *

environment_name = 'CartPole-v1'
env = gym.make(environment_name)

episodes = 25 
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))
#env.close()
