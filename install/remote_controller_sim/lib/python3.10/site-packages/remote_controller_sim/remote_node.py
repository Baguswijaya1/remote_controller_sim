# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Char
# import keyboard

# class remote(Node):
#     def __init__(self):
#         super().__init__('remote')
#         self.controller = self.create_publisher(Char, 'control_signal', 10)
#         self.timer = self.create_timer(0.3, self.read_keyboard)

#     def read_keyboard(self):
#         # baca keyboard
#         keys = ['w', 's']
#         for key in keys:
#             if keyboard.is_pressed(key):
#                 signal = Char()
#                 signal.data = key
#                 self.controller.publish(signal.data) # publish
#                 self.get_logger().info(f'remote signal : {signal}')
#                 break
            


# def main(args = None):
#     rclpy.init(args=args)
#     node = remote()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from evdev import InputDevice, categorize, ecodes

class KeyboardController(Node):
    def __init__(self):
        super().__init__('keyboard_controller')
        self.publisher_ = self.create_publisher(String, 'key_input', 10)

        # Ganti dengan path device-mu
        device_path = '/dev/input/event3'
        try:
            self.device = InputDevice(device_path)
            self.get_logger().info(f'Listening to {device_path}')
        except Exception as e:
            self.get_logger().error(f'Failed to open device {device_path}: {e}')
            exit(1)

        self.run()

    def run(self):
        for event in self.device.read_loop():
            if event.type == ecodes.EV_KEY:
                key_event = categorize(event)
                if key_event.keystate == key_event.key_down:
                    keycode = key_event.keycode
                    msg = String()
                    msg.data = str(keycode)
                    self.publisher_.publish(msg)
                    self.get_logger().info(f'Key pressed: {keycode}')

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()