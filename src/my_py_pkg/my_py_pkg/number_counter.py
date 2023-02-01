#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_counter(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_counter, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.msg = Int64()
        self.get_logger().info("Counter node is initialised")

    def callback_counter(self, msg):
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    
    node = number_counter()
    
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()