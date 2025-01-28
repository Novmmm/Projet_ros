import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class Lum(Node):

    def __init__(self):
        super().__init__('Lum')
        self.publisher_ = self.create_publisher(Int64, 'data_lum', 10)
        timer_period = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 101

    def timer_callback(self):
        msg = Int64()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Valeur capteur luminosite : "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    lum = Lum()

    rclpy.spin(lum)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    lum.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
