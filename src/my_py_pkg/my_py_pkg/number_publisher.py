#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_publisher(Node):
    def __init__(self):
        super().__init__("number_publisher")

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.msg_ = Int64()
        self.counter_ = 0
        self.create_timer(1/3, self.callback_counterloop)
        self.get_logger().info("number publisher node initialised")
        
    def callback_counterloop(self):
        self.counter_ += 1
        self.msg_.data = self.counter_
        self.publisher_.publish(self.msg_)

def main(args=None):
    rclpy.init(args=args)

    node = number_publisher()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()