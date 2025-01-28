import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger
from std_msgs.msg import Int64
import sys
from std_msgs.msg import Float32

class Fusion(Node):

    def __init__(self):
        super().__init__('fusion')
        self.subscription = self.create_subscription(
            Float32,
            'data_temp',
            self.listener_callback_temp,
            10)
        self.subscription = self.create_subscription(
            Int64,
            'data_lum',
            self.listener_callback_lum,
            10)    
        self.subscription = self.create_subscription(
            Int64,
            'data_presence_portail',
            self.listener_callback_portail,
            10)  
        self.client = self.create_client(Trigger, 'data_bp')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('En attente du service ')
        key = sys.stdin.read(1)
        if key == 't':
             self.get_logger().info('Barre espace détectée, envoi de la requête...')
             req = Trigger.Request()
             future = self.client.call_async(req)
	          
        self.temp = 0
        self.lum = 0
        self.presence_portail = 0
        self.bp_portail = 0

    def listener_callback_temp(self, msg):
        self.temp = msg.data
        if self.temp > 22 :
            #allumage froid
            self.get_logger().info('allumage climatisation')
        elif self.temp < 19 : 
            #allumage chaud
            self.get_logger().info('allumage chauffage') 
    	    	
    def listener_callback_lum(self, msg):
        self.lum = msg.data
        if self.lum < 100 : 
            #Fermeture des volets
            self.get_logger().info('Fermeture des volets ') 
        
    def listener_callback_portail(self, msg):
        self.lum = msg.data
        if self.presence_portail == 1 : 
            #Allumage led
            self.get_logger().info('Led allumee vous pouvez ouvir le portail ') 
           	    
	
    def listener_callback_bp_portail(self, msg):
        self.bp_portail = msg.data
        if bp_portail == 1 : 
            #Utilisation servomoteur 
            self.get_logger().info('Ouverture du portail') 
        else :
            #utilisation servomoteur sens inverse
            self.get_logger().info('Fermeture du portail')
        	
            
            
            
def main(args=None):
    rclpy.init(args=args)

    fusion = Fusion()

    rclpy.spin(fusion)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    fusion.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
