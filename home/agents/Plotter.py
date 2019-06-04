import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plotter():
    def __init__(self):
        self.labels = ['time', 'x', 'y', 'z', 'phi', 'theta', 'psi', 'x_velocity',
          'y_velocity', 'z_velocity', 'phi_velocity', 'theta_velocity',
          'psi_velocity', 'rotor_speed1', 'rotor_speed2', 'rotor_speed3', 'rotor_speed4', 'reward']
        self.cache = {x : [] for x in self.labels}
        
    def add(self, data_to_log):
        for ii in range(len(self.labels)):
            self.cache[self.labels[ii]].append(data_to_log[ii])
            
    def plot_reward(self):
        plt.plot(self.cache['time'], self.cache['reward'], label='reward')
        plt.legend()
        _ = plt.ylim()
        
    def plot_trajectory(self, target_pose=None):
        fig = plt.figure(figsize=(7, 7))
        ax = fig.gca(projection='3d')
        ax.plot(self.cache['x'], self.cache['y'], self.cache['z'], label='trajectory')
        
        ax.scatter(self.cache['x'][0], self.cache['y'][0], self.cache['z'][0], c='g', marker='o', s=20, label='start')
        ax.scatter(self.cache['x'][-1], self.cache['y'][-1], self.cache['z'][-1], c='r', marker='o', s=20, label='end')
        
        if target_pose is not None:
            ax.scatter(target_pose[0], target_pose[1], target_pose[2], c='y', marker='o', s=20, label='target')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        ax.legend()
        plt.show()
        
        print("Start coordinates: x={:7.3f} y={:7.3f} z={:7.3f}".format(self.cache['x'][0], self.cache['y'][0], self.cache['z'][0]))
        print("End coordinates: x={:7.3f} y={:7.3f} z={:7.3f}".format(self.cache['x'][-1], self.cache['y'][-1], self.cache['z'][-1]))
        
    def plot_all(self):
        plt.subplots(figsize=(15, 10))
        
        plt.subplot(2, 3, 1)
        plt.plot(self.cache['time'], self.cache['reward'], label='reward')
        plt.xlabel('time, seconds')
        plt.ylabel('reward')
        plt.legend()
        _ = plt.ylim()
        
        plt.subplot(2, 3, 2)
        plt.plot(self.cache['time'], self.cache['x'], label='x')
        plt.plot(self.cache['time'], self.cache['y'], label='y')
        plt.plot(self.cache['time'], self.cache['z'], label='z')
        plt.xlabel('time, seconds')
        plt.ylabel('position')
        plt.legend()
        _ = plt.ylim()

        plt.subplot(2, 3, 3)
        plt.plot(self.cache['time'], self.cache['phi'], label='phi')
        plt.plot(self.cache['time'], self.cache['theta'], label='theta')
        plt.plot(self.cache['time'], self.cache['psi'], label='psi')
        plt.xlabel('time, seconds')
        plt.ylabel('angle')
        plt.legend()
        _ = plt.ylim()
        
        plt.subplot(2, 3, 4)
        plt.plot(self.cache['time'], self.cache['rotor_speed1'], label='r_1')
        plt.plot(self.cache['time'], self.cache['rotor_speed2'], label='r_2')
        plt.plot(self.cache['time'], self.cache['rotor_speed3'], label='r_3')
        plt.plot(self.cache['time'], self.cache['rotor_speed4'], label='r_4')
        plt.xlabel('time, seconds')
        plt.ylabel('rotor revolutions')
        plt.legend()
        _ = plt.ylim()
        
        plt.subplot(2, 3, 5)
        plt.plot(self.cache['time'], self.cache['x_velocity'], label='x_velocity')
        plt.plot(self.cache['time'], self.cache['y_velocity'], label='y_velocity')
        plt.plot(self.cache['time'], self.cache['z_velocity'], label='z_velocity')
        plt.xlabel('time, seconds')
        plt.ylabel('velocity')
        plt.legend()
        _ = plt.ylim()
        
        plt.subplot(2, 3, 6)
        plt.plot(self.cache['time'], self.cache['phi_velocity'], label='phi_velocity')
        plt.plot(self.cache['time'], self.cache['theta_velocity'], label='theta_velocity')
        plt.plot(self.cache['time'], self.cache['psi_velocity'], label='psi_velocity')
        plt.xlabel('time, seconds')
        plt.ylabel('angle velocity')
        plt.legend()
        _ = plt.ylim()
        
    def plot_position2d(self):
        plt.plot(self.cache['time'], self.cache['x'], label='x')
        plt.plot(self.cache['time'], self.cache['y'], label='y')
        plt.plot(self.cache['time'], self.cache['z'], label='z')
        plt.legend()
        _ = plt.ylim()
        
    def plot_velocity(self):
        plt.plot(self.cache['time'], self.cache['x_velocity'], label='x_hat')
        plt.plot(self.cache['time'], self.cache['y_velocity'], label='y_hat')
        plt.plot(self.cache['time'], self.cache['z_velocity'], label='z_hat')
        plt.legend()
        _ = plt.ylim()
        
    def plot_euler_agnels(self):
        plt.plot(self.cache['time'], self.cache['phi'], label='phi')
        plt.plot(self.cache['time'], self.cache['theta'], label='theta')
        plt.plot(self.cache['time'], self.cache['psi'], label='psi')
        plt.legend()
        _ = plt.ylim()
        
    def plot_rotor_revs(self):
        plt.plot(self.cache['time'], self.cache['rotor_speed1'], label='r_1')
        plt.plot(self.cache['time'], self.cache['rotor_speed2'], label='r_2')
        plt.plot(self.cache['time'], self.cache['rotor_speed3'], label='r_3')
        plt.plot(self.cache['time'], self.cache['rotor_speed4'], label='r_3')
        plt.legend()
        _ = plt.ylim()