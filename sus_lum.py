import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String  

class Lum(Node):

    def __init__(self):
        super().__init__('lum')

        # Souscription au topic de luminosité
        self.subscription_lum = self.create_subscription(
            Float32,
            'data_lum',
            self.listener_callback_lum,
            10)

        # Souscription au topic de contrôle des volets
        self.subscription_volets = self.create_subscription(
            String,
            'control_volets',
            self.listener_callback_volets,
            10)

        # Variable pour stocker l'état des volets
        self.volets_state = "CLOSE"  # Par défaut, les volets sont fermés

    def listener_callback_lum(self, msg):
        self.lum = msg.data
        if self.lum < 105:
            # Fermeture des volets si la luminosité est faible
            self.get_logger().info('Luminosité faible : Fermeture des volets')
            self.control_volets("CLOSE")
        else:
            # Ouverture des volets si la luminosité est élevée
            self.get_logger().info('Luminosité élevée : Ouverture des volets')
            self.control_volets("OPEN")

    def listener_callback_volets(self, msg):
        # Gestion des commandes manuelles pour les volets
        if msg.data == "OPEN" :
            self.get_logger().info(f'Ouverture des volets manuel')
        if msg.data == "Close" :
            self.get_logger().info(f'Fermeture des volets manuel')
        
        



def main(args=None):
    rclpy.init(args=args)
    node = Lum()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
