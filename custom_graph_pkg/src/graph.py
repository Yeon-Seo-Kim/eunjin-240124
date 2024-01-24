import rospy
import math
from custom_graph_pkg.msg import variable, Theta, Time, X, Y


def Theta_callback(data):
    size = len(data.Time_values)
    for i in range(size):
    	#print(f"Theta: {var.Theta_values[i]} | Velocity: {var.Velocity_values[i]} | X_location: {X_locations[i]} | Y_location: {Y_locations[i]} | Time: {var.Time_values[i]}")
        print("Theta: ", Theta_values[i])
    print("\n")

def 



def main():
    rospy.init_node('print_node', anonymous = False)
    rospy.Subscriber("points", variable, print_topic_callback)
    rospy.Subscriber("points", Theta, print_topic_callback)
    rospy.Subscriber("points", Time, print_topic_callback)
    rospy.Subscriber("points", X, print_topic_callback)
    rospy.Subscriber("points", Y, print_topic_callback)
   
    rospy.spin()


if __name__ == '__main__':
    main()
