import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class Portail(Node):

    def __init__(self):
        super().__init__('Portail')
        self.publisher_ = self.create_publisher(Int64, 'data_presence_portail', 10)
        timer_period = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        msg = Int64()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Valeur capteur Presence Portail : "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    portail = Portail()

    rclpy.spin(portail)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    portail.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
