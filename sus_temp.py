import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class Temp(Node):

    def __init__(self):
        super().__init__('fusion')
        self.subscription = self.create_subscription(
            Float32,
            'data_temp',
            self.listener_callback_temp,
            10)
        
        self.clim_subscription = self.create_subscription(
            String,
            'control_clim',
            self.listener_callback_clim,
            10)
        
        self.chauffage_subscription = self.create_subscription(
            String,
            'control_chauffage',
            self.listener_callback_chauffage,
            10)

    def listener_callback_temp(self, msg):
        self.temp = msg.data
        if self.temp > 22 :
            #allumage froid
            self.get_logger().info('allumage climatisation')
        elif self.temp < 19 : 
            #allumage chaud
            self.get_logger().info('allumage chauffage') 

    def listener_callback_clim(self, msg):
        if msg.data == "ON":
            self.get_logger().info('Climatisation allumée via interface web')
        else:
            self.get_logger().info('Climatisation éteinte via interface web')
    def listener_callback_chauffage(self, msg):
        if msg.data == "ON":
            self.get_logger().info('Chauffage allumé via interface web')
        else :
            self.get_logger().info('Chauffage éteint via interface web')

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
