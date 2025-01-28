import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32


class Temp(Node):

    def __init__(self):
        super().__init__('Temp')
        self.publisher_ = self.create_publisher(Float32, 'data_temp', 10)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 29

    def timer_callback(self):
        msg = Float32()
        msg.data = float(input('Entrez une valeure'))
        self.publisher_.publish(msg)
        self.get_logger().info('Val Capteur Temperature : "%d"' % msg.data)
        


def main(args=None):
    rclpy.init(args=args)

    temp = Temp()

    rclpy.spin(temp)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    temp.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
