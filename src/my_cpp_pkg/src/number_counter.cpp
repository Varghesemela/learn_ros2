#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

class number_counter : public rclcpp::Node
{
    public:
        number_counter() : Node("number_counter")
        {
            RCLCPP_INFO(this->get_logger(), "Publisher node is initialised");
            subscriber_ = this->create_subscription<example_interfaces::msg::Int64>("number", 10, std::bind(&number_counter::callback_counter, this, std::placeholders::_1));
            publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number_count", 10);
            
        }

    private:

        void callback_counter(const example_interfaces::msg::Int64 msg){
           publisher_->publish(msg);
        }

        rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
        rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_ = 0;
};

int main(int argc, char **argv)
{

    rclcpp::init(argc, argv);
    auto node = std::make_shared<number_counter>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}