import rclpy
from rclpy.node import Node
from std_msgs.msg import Char

class drone_motors(Node):
    def __init__(self):
        super().__init__('drone_motors')

        self.throttle = 0

        self.motors_sub = self.create_subscription(
            Char,
            'control_signal',
            self.receive_msg,
            10
        )
    
    def receive_msg(self, signal):
        if signal.data == 'w':
            return self.throttle_up()
        elif signal.data == 's':
            return self.throttle_down()
    
    def throttle_up(self):
        if self.throttle <100:
            self.throttle += 2
        else:
            self.throttle = self.throttle

    def throttle_down(self):
        if self.throttle == 0:
            self.throttle = self.throttle
        else:
            self.throttle -= 2

def main(args=None):
    rclpy.init(args=args)
    node = drone_motors()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()