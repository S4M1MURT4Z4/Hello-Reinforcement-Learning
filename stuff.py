from imports import *

class Algo:

    def __init__(self, env_name, log_path='training\\logs', ppo_path='training\\saved_models\\PPO_Model_CartPole') -> None:
        
        self.envname = env_name
        self.env = gym.make(env_name)
        self.log_path = log_path
        self.ppo_path = ppo_path 
        self.model = PPO('MlpPolicy', self.env, verbose=1, tensorboard_log=log_path)

    def save(self, ) -> None:
        pass

    def load(self, filename) -> None:
        self.model = PPO.load(self.ppo_path, env=self.env)
        
    def evaluate(self, n_eval_episodes=10, render=False) -> None:
        evaluate_policy(self.model, self.env, n_eval_episodes=n_eval_episodes, render=render)

    def learn(self, total_timesteps=20000):
        self.model.learn(total_timesteps=total_timesteps)

    def run(self, episodes=5, logs=True, render=True) -> None:
        
        for episode in range(1, episodes+1):
            obs = self.env.reset()
            done = False
            score = 0 

            while not done:

                if render:
                    self.env.render()

                action, _ = self.model.predict(obs)
                obs, reward, done, _ = self.env.step(action)
                score += reward
                
            if logs:
                print('Episode:{} Score:{}'.format(episode, score))
        
        self.env.close()

if __name__ == '__main__':
    stuff = Algo('CartPole-v1')
    stuff.learn(100000)
    stuff.run()

