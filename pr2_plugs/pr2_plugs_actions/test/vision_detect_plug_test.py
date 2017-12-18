#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import roslib
roslib.load_manifest('pr2_plugs_actions')

import rospy

import os
import sys
import time

from pr2_plugs_msgs.msg import *
from actionlib_msgs.msg import *
from pr2_common_action_msgs.msg import *
from std_srvs.srv import *

import actionlib


def main():
  rospy.init_node("vision_detect_plug_test")

  # Construct action ac
  rospy.loginfo("Starting action client...")
  action_client = actionlib.SimpleActionClient('vision_plug_detection', VisionPlugDetectionAction)
  action_client.wait_for_server()
  rospy.loginfo("Action client connected to action server.")

  # Call the action
  rospy.loginfo("Calling the action server...")
  action_goal = VisionPlugDetectionGoal()
  action_goal.camera_name = "r_forearm_camera"
  action_goal.prior.header.stamp = rospy.Time.now()
  action_goal.prior.header.frame_id = "base_link"
  if action_client.send_goal_and_wait(action_goal, rospy.Duration(10.0), rospy.Duration(5.0)) == GoalStatus.SUCCEEDED:
    rospy.loginfo('Call to action server succeeded')
  else:
    rospy.logerr('Call to action server failed')


if __name__ == "__main__":
  main()
