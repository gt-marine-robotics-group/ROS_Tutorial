import rclpy
from rclpy.node import Node
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from tutorial_msgs.srv import GetBuoyLocation

class TutorialTopic_1_4_Client(Node):
    def __init__(self):
        super().__init__('topic_1_4_client_node')
        self.get_buoy_client = self.create_client(
            GetBuoyLocation,
            '/tutorial/get_buoy_location',
        )
        while not self.get_buoy_client.wait_for_service(timeout_sec=3.0):
            self.get_logger().info("Waiting for get buoy location service")
        self.result = None
        self.call_service()

    def call_service(self):
        request = GetBuoyLocation.Request()
        # TODO: Q1.4.d 
        ### STUDENT CODE HERE
        request.buoy_name = "yellow_buoy"
        ### END STUDENT CODE
        # Send request to service
        future = self.get_buoy_client.call_async(request)
        future.add_done_callback(self.handle_response)
    
    def handle_response(self, future):
        self.result = future.result()

def main(args=None):
    rclpy.init(args=args)
    node = TutorialTopic_1_4_Client()
    rclpy.spin(node)