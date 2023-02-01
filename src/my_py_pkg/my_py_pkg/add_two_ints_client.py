#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial


class add_two_ints_client(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints_client(6, 7)
        self.call_add_two_ints_client(4, 9)
        self.call_add_two_ints_client(2, 1)

    def call_add_two_ints_client(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for server to be online...")
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed! %r" % (e,))


def main(args=None):
    rclpy.init(args=args)

    node = add_two_ints_client()

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
