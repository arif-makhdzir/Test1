#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True, log_level=rospy.INFO)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")

rospy.loginfo("Reference frame: %s" % group.get_planning_frame())
rospy.loginfo("End effector: %s" % group.get_end_effector_link())
rospy.loginfo("Robot Groups:")
rospy.loginfo(robot.get_group_names())
rospy.loginfo("Current Joint Values:")
rospy.loginfo(group.get_current_joint_values())
rospy.loginfo("Current Pose:")
rospy.loginfo(group.get_current_pose())
rospy.loginfo("Robot State:")
rospy.loginfo(robot.get_current_state())

moveit_commander.roscpp_shutdown()