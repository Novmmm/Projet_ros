import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class BP(Node):

    def __init__(self):
        super().__init__('data_bp')
        self.srv = self.create_service(Trigger, 'data_bp', self.bp_callback)

    def bp_callback(self,request,response):
    	self.log('le bp a ete presse')
    	response = 1 
    	return response


def main(args=None):
    rclpy.init(args=args)

    portail = BP()

    rclpy.spin(portail)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    portail.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
