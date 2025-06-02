import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class remote(Node):
    def __init__(self):
        super().__init__('remote')
        # self.publisher = self.create_publisher()
    
    def timer_callback(self):
        pass

    def read_keyboard():
        pass

    def throttle():
        pass


def main(args = None):
    rclpy.init(args=args)
    node = remote()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()