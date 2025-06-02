import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class drone(Node):
    def __init__(self):
        super().__init__('drone')
        self.throttle_sub = self.create_subscription(
            Float32,
            'throttle',
            self.throttle_callback,
            10
        )

    def throttle_callback(self):
        # self.get_logger().info()
        pass

def main(args = None):
    rclpy.init(args=args)
    node = drone()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
