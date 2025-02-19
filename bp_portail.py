import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class ButtonService(Node):
    def __init__(self):
        super().__init__('data_bp')
        self.srv = self.create_service(Trigger, 'data_bp', self.handle_button_press)
        self.get_logger().info("Service 'button_service' prêt à recevoir des requêtes.")

    def handle_button_press(self, request, response):
        self.get_logger().info('Commande du portail active')
        response.success = True
        response.message = "Le portail s'ouvre "
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ButtonService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
