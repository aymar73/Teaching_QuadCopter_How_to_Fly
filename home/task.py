import numpy as np
from physics_sim import PhysicsSim

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 1
        self.action_high = 1000
        self.action_size = 4

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self, done):
        """Uses current pose of sim to return reward."""
        reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        reward = np.clip(reward, -1, 1 )
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward(done) 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state
    


class TakeOffTask(Task):
    def __init__(self, target_pos=None, runtime=5.):
        super().__init__(init_pose=[0.0, 0.0, 100.0, 0.0, 0.0, 0.0], init_velocities=None, init_angle_velocities=None, runtime=runtime, target_pos=target_pos)

    def get_reward(self, done):
        # close it gets to the target in z direction higher the reward.
        # z_position_reward = 1 - 0.3 * (self.sim.pose[2] - self.target_pos[2])
        # further it gets from target x and y coordinated higher penalty is. Moreover, an agent is 
        # actually encouraged to keep close to the target x and y coordinates.
        # xy_position_penalty = - 0.5 * (abs(self.sim.pose[:2] - self.target_pos[:2])).sum()
        # Penalizing velocity in the x and y directions and encourage for vertical velocity
        reward = 0.3 * self.sim.v[2] 
 
        
        # puttin the reward function into the range (-1, 1) and making it smooth
        reward = np.tanh(reward)
        
        # penalize crush
        if done and self.sim.time < self.sim.runtime: 
            reward = -1

        return reward