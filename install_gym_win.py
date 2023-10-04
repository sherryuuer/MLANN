# 现在在win10可以这样安装gym
# pip3 install swig
# pip3 install box2d
# pip3 install gymnasium
# pip3 install gymnasium[box2d]

# 然后python代码如下
import gymnasium as gym

if __name__ == '__main__':
    env = gym.make("Taxi-v3", render_mode="human")

    observation, info = env.reset(seed=42)
    for _ in range(1000):
        env.render()
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        print(observation, reward, terminated, truncated, info)

    if terminated or truncated:
        observation, info = env.reset()
    
env.close()

# 但是中途学习中图形界面又卡顿dead
