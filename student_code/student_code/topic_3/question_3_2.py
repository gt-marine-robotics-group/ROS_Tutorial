from geometry_msgs.msg import Pose
import numpy as np

class TutorialTopic_3_2:
    def __init__(self):
        ## TODO: Q3.2.a Linear Coordinate Conventions
        self.red_buoy_location = Pose()
        self.red_buoy_location.position.x = 2
        self.red_buoy_location.position.y = 3
        self.yellow_buoy_location = Pose()
        self.yellow_buoy_location.position.x = -3
        self.yellow_buoy_location.position.y = 1

        ## TODO: Q3.2.b Angular Coordinate Convention
        self.red_buoy_angle = np.arctan2(3,2)
        self.yellow_buoy_angle= np.arctan2(1,-3)

        ### STUDENT CODE HERE

        ### END STUDENT CODE
