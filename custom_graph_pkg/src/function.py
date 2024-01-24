import rospy
import math
import random
from custom_graph_pkg.msg import variable, Theta, Time, X, Y


def main():
    rospy.init_node('calculate_node', anonymous=False)

    pub = rospy.Publisher('points', formula, queue_size = 10)

    rate = rospy.Rate(1)

    msg = formula()

#header: time, / function

    while not rospy.is_shutdown():
	count = 0
 	var = variable()
	size = 100

	msg.time = 0.01
	msg.init_theta = random.randint(10,30)
	msg.yaw_rate = random.randint(-60,60)
	msg.acceleration = random.randint(-30,30)
	msg.init_x = random.randint(10,30)
	msg.init_y = random.randint(10,30)

	
	for i in range(size):

	    msg.theta = msg.init_theta
	    msg.theta += msg.yaw_rate * msg.time
	    var.Theta_values.append(msg.theta)

	    msg.velocity = msg.acceleration * msg.time
	    var.Velocity_values.append(msg.velocity)

	    msg.x = msg.init_x
	    msg.x += msg.velocity * math.cos(msg.theta) * msg.time
	    var.X_locations.append(msg.x)

            msg.y = msg.init_y
	    msg.y += msg.velocity * math.sin(msg.theta) * msg.time
	    var.Y_locations.append(msg.y)

	    var.Time_values.append(msg.time*(count+1))

	    pub.publish(msg)

	    rate.sleep()

	    count += 1

	for i in range(size);
	    print(f"Theta: {var.Theta_values[i]} | Velocity: {var.Velocity_values[i]} | X_location: {X_locations[i]} | Y_location: {Y_locations[i]} | Time: {var.Time_values[i]}")
	print("\n")

	# if count value exceeds 100
 	#del Theta_values[0:98]
	#del Velocity_values[0:98]
	#del X_locations[0:98]
	#del Y_locations[0:98]
	#del Time_values[0:98]


if __name__ == '__main__':
    try:
	main()
    except rospy.ROSInterruptException:
	pass
