import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class Portail(Node):

    def __init__(self):
        super().__init__('Presence')
        self.publisher_ = self.create_publisher(Bool, 'data_presence_portail', 10)
        timer_period = 2 # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = True
        
    def timer_callback(self):
        msg = Bool()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Valeur capteur Presence Portail : "%s"' % msg.data)

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
