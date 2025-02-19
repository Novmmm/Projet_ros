import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Lum(Node):

    def __init__(self):
        super().__init__('Lum')
        self.publisher_ = self.create_publisher(Float32, 'data_lum', 10)
        timer_period = 10 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 101.2

    def timer_callback(self):
        msg = Float32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Valeur capteur luminosite : "%.2f"' % msg.data)


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
