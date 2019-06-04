from task import Task
import numpy as np


class TakeOffTask(Task):
    def __init__(self, target_pos=None, runtime=5.):
        super().__init__(init_pose=[0.0, 0.0, 10.0, 0.0, 0.0, 0.0], init_velocities=None, init_angle_velocities=None, runtime=runtime, target_pos=target_pos)

    def get_reward(self, done):
        # close it gets to the target in z direction higher the reward.
        z_position_reward = 0.3 * (self.sim.pose[2] - self.target_pos[2])
        # further it gets from target x and y coordinated higher penalty is. Moreover, an agent is 
        # actually encouraged to keep close to the target x and y coordinates.
        xy_position_penalty = - 0.5 * (abs(self.sim.pose[:2] - self.target_pos[:2])).sum()
        # Penalizing velocity in the x and y directions and encourage for vertical velocity
        reward = 0.3 * self.sim.v[2]#- 0.3 * abs(self.sim.v[0]) - 0.3 * abs(self.sim.v[1])
        
        # puttin the reward function into the range (-1, 1) and making it smooth
        reward = np.tanh(reward)
        
        # penalize crush
        if done and self.sim.time < self.sim.runtime: 
            reward = -1

        return reward