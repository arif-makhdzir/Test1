#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


class KairosMoveitManager(object):

    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)

        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("arm")
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

    def move_end_effector(self, pose_target):


        self.group.set_pose_target(pose_target)

        plan1 = self.group.plan()

        self.group.go(wait=True)

    def __del__(self):

        moveit_commander.roscpp_shutdown()


if __name__ == "__main__":
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
    kairos = KairosMoveitManager()

    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.46
    pose_target.position.y = 0
    pose_target.position.z = 1.18

    kairos.move_end_effector(pose_target)
