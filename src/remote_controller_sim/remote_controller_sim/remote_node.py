import rclpy
from rclpy.node import Node
from std_msgs.msg import Char
import keyboard

class remote(Node):
    def __init__(self):
        super().__init__('remote')
        self.controller = self.create_publisher(Char, 'control_signal', 10)
        self.timer = self.create_timer(0.3, self.read_keyboard)

    def read_keyboard(self):
        # baca keyboard
        keys = ['w', 's']
        for key in keys:
            if keyboard.is_pressed(key):
                signal = Char()
                signal.data = key
                self.controller.publish(signal.data) # publish
                self.get_logger().info(f'remote signal : {signal}')
                break
            


def main(args = None):
    rclpy.init(args=args)
    node = remote()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()