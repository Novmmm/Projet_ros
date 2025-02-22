import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import Trigger  

class PresenceSubscriber(Node):
    def __init__(self):
        super().__init__('presence_subscriber')
        self.subscription = self.create_subscription(
            Int64,
            'data_presence_portail',
            self.presence_callback,
            10
        )
        self.client = self.create_client(Trigger, 'data_bp')

    def presence_callback(self, msg):
        if msg.data == 1:
            self.get_logger().info('Présence détectée. Appel du service bouton...')
            req = Trigger.Request()
            future = self.client.call_async(req)
            future.add_done_callback(self.response_callback)
 
    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Réponse du service: {response.message}")
        except Exception as e:
            self.get_logger().error(f"Erreur du service: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = PresenceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
