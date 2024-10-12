from controller import Robot, Camera, GPS, InertialUnit, Motor, LED
from typing import Tuple, List

class Mavic:
    def __init__(self):
        # Initialize the Robot
        self.drone = Robot()
        self.timestep = int(self.drone.getBasicTimeStep())

        # Enable Camera
        self.camera = self.drone.getDevice("camera")
        self.camera.enable(self.timestep)

        # Enable IMU (Inertial Measurement Unit)
        self.imu = self.drone.getDevice("inertial unit")
        self.imu.enable(self.timestep)

        # Enable Gyroscope
        self.gyro = self.drone.getDevice("gyro")
        self.gyro.enable(self.timestep)

        # Enable GPS
        self.gps = self.drone.getDevice("gps")
        self.gps.enable(self.timestep)

        # Initialize Propellers (Motors)
        motor_names = [
            "front left propeller", "front right propeller", 
            "rear left propeller", "rear right propeller"
        ]
        
        self.motors = [self.drone.getDevice(motor_name) for motor_name in motor_names]
        
        for motor in self.motors:
            motor.setPosition(float('inf'))  # Set motors to velocity control mode
            motor.setVelocity(0.0)  # Initialize motor velocity to zero

    def get_imu_values(self) -> Tuple[float, float, float]:
        """Returns the roll, pitch, and yaw values from the IMU."""
        return self.imu.getRollPitchYaw()

    def get_gps_values(self) -> Tuple[float, float, float]:
        """Returns the x, y, and z coordinates from the GPS."""
        return self.gps.getValues()

    def get_gyro_values(self) -> Tuple[float, float, float]:
        """Returns the angular velocity around x, y, and z axes from the gyro."""
        return self.gyro.getValues()

    def get_time(self) -> float:
        """Returns the current simulation time."""
        return self.drone.getTime()

    def set_rotor_speed(self, speeds: Tuple[float, float, float, float]) -> None:
        """Sets the velocity for each rotor."""
        for motor, speed in zip(self.motors, speeds):
            motor.setVelocity(speed)

    def get_image(self) -> List[List[List[int]]]:
        return self.camera.getImage()