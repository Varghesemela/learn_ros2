#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class number_publisher : public rclcpp::Node
{
    public:
        number_publisher() : Node("number_publisher")
        {
            RCLCPP_INFO(this->get_logger(), "Publisher node is initialised");
            publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
            timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&number_publisher::publish_number, this));
            
        }

    private:

        void publish_number(){
           auto msg = example_interfaces::msg::Int64();
           counter_ += 1;
           msg.data = counter_;
           publisher_->publish(msg);
        }

        rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_ = 0;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<number_publisher>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}