import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici_node')
        self.declare_parameter('esik_degeri', 30.0)
        self.subscription = self.create_subscription(
            Float32,
            '/sicaklik',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        sicaklik = msg.data
        esik = self.get_parameter('esik_degeri').get_parameter_value().double_value
        
        if sicaklik > esik:
            self.get_logger().warn(f'DİKKAT! Sıcaklık yüksek: {sicaklik:.2f} (Eşik: {esik})')
        else:
            self.get_logger().info(f'Sıcaklık normal: {sicaklik:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
