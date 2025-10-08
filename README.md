# Robotics Coding Tutorial
In this repo, you will learn the basics of ROS2 and robotics fundamentals. The goal of this tutorial is start with the basics and slowly progress to creating your own full autonomy stack for the stinger tugs. Throughout this tutorial, you will fill out code blocks, answer questions, and write code. After completing each section, there will be a provided autograder that will verify your work. Only by passing all the required autograder tests should you move onto the next section. If you are having a hard time passing some tests, please reach out! We are more than happy to help.

## Prerequisites
- **Some base knowledge of coding/python** If you are not yet familiar with python, you can still attempt to go through this tutorial but it is highly recommended that you learn python first. Some great tutorials are:
  - https://www.w3schools.com/python/
  - https://docs.python.org/3/tutorial/index.html
- Basics of Navigating Linux

## Repo Setup

For this tutorial, you will need to fork two repositories [ROS_Tutorial](https://github.com/gt-marine-robotics-group/ROS_Tutorial) and [stinger-software](https://github.com/gt-marine-robotics-group/stinger-software). We will show how to fork the `stinger-software` repo which will be the same steps for the `ROS_Tutorial` repo. First go to the repo.

<img src="assets/stinger_software_git_landing.png" alt="git landing" width="800"/>

Then click fork.

<img src="assets/stinger_software_fork_box.png" alt="git fork box" width="800"/>

If prompted, name the repository `stinger-software` (or whatever the original repository was called). Make sure the select owner is under your github username.

<img src="assets/stinger_software_fork_page.png" alt="git fork page" width="800"/>

Then click `Create Fork`. Repeat this process for the `ROS_Tutorial` repo as well.


## Environment Setup 

### Personal Computer Setup

<details> <summary><strong>Mac</strong></summary>

First, install Docker Desktop. [Installation Instructions](https://docs.docker.com/desktop/setup/install/mac-install/). Make sure that any time you want to work, you have Docker Desktop running in the background.

**Note:** You will have to select the correct installation based on your macbook chip set (Intel/ Apple Silicone). If you have a M1, M2, M3, etc macbook, you are Apple Silicone.

To setup your environment (one time step), run:

```
curl -O https://raw.githubusercontent.com/Jeff300fang/MRG_Docker/tutorial/mrg_tutorial_startup_mac.sh && bash mrg_tutorial_startup_mac.sh
```

You will be prompted to enter your github username. Please enter the github username 

Reboot your machine.

</details>

<details> <summary> <strong> Windows</strong></summary>

<hr>

Open PowerShell or Windows Command Prompt in admin mode, run:
```
wsl --install
```

Launch Ubuntu by running `wsl` in PowerShell.

For some computers, you may need to manually install Docker Desktop. [Installation Instructions](https://docs.docker.com/desktop/setup/install/windows-install/). If you are unsure if you need it, we recommend to install it anyways.

Then, follow the steps in the Ubuntu setup guide.

<hr>

</details>

<details> <summary> <strong> Ubuntu</strong></summary>

<hr>

To setup your environment (one time step), run:

```
curl -O https://raw.githubusercontent.com/Jeff300fang/MRG_Docker/tutorial/mrg_tutorial_startup.sh && bash mrg_tutorial_startup.sh
```

You will be prompted to enter your github username. Please enter the github username you forked the repositories with.

Once the above command successfully finishes. Run

```
source ~/.bashrc && newgrp docker
```
<hr>

</details>

## Topic 0: Editing, Building, Testing Instructions

<details>  <summary> <strong> 0.1 Running the Container and GUI</strong></summary>

<hr>

To start the docker container, run

```
start_tutorial_docker
```

Then to bootstrap the workspace, run

```
bootstrap_ws
```

This command only needs to be run for the first time OR when new packages are introduced OR when the docker container is rebuilt.

To access the container's GUI, open `localhost:6080` in your local browser.

To start a 6 pane terminal (recommended), run `tmuxp load /root/.tmuxp/tmuxp_config.yaml`. To exit, run `tmux kill-session`

<hr>

</details>

<details>
<summary> <strong> 0.2 Editing Code</strong></summary>

<hr>

We **highly** recommend using Visual Studio Code (VSCode) for all coding. All senior members will be familiar with working in VSCode. The following instructions will assume that you are using VSCode.

If you haven't already, install VSCode. [Instructions Here](https://code.visualstudio.com/). Make sure your container is running. See **Section 0.1** if you do not. Then, open VSCode.

<img src="assets/vscode_home.png" width="800"/>

Click the extensions page on the left hand side and ensure Docker is installed. If not, install it.

<img src="assets/extensions.png" width="800"/>

Then, click the blue icon in the bottom left corner. It should bring up this page.

<img src="assets/attach_to_container.png" width="800"/>

Click on attach to running container. You should see something like this.

<img src="assets/select_mrg_tutorial.png" width="800"/>

Click `/mrg_tutorial`. If prompted to open a folder, select mrg_ws -> src. You should have something like this (without the answer folders).

<img src="assets/code_ws.png" width="800"/>

You can now click through each folder and see each file.

<hr>

</details>

<details> <summary> <strong> 0.3 Building and Autograder Testing </strong></summary>

<hr>

Each topic will give a rough description of the task and there will be an associated file in ```ROS_Tutorial/student_code/student_code/topic_{topic #}/question_{topic #}_{section #}.py```. So for example, if you were working on ```Topic 1.2```, you would be accessing the file ```ROS_Tutorial/student_code/student_code/topic_1/question_1_2.py```

Each section will also have an associated autograder. At any point you want to test your code, you will need to run these commands in your workspace directory. For this tutorial, the workspace directory refers to the folder location of ```ROS_Tutorial/```.
```
colcon build
source install/setup.bash
ros2 run autograder test_topic_{topic_number}_{topic_subsection}
```
For example, to run the tests for ```topic 1.2```, you should run `ros2 run autograder test_topic_1_2`. 

**Note:** Make sure nothing is running in the background when running the autograder tests. Any background processes may mess up the autograder.

**Note:** Building your code is super important for ensuring that your latest changes are reflected when you execute your code.

<hr>

</details>

## Topic 1: ROS2 Basics
<details>
<summary><strong>1.1 Understanding Nodes and Topics</strong></summary>

<hr>

The goal of this section is to familiarize yourself with the concept of nodes and topics. We will be using ROS2 CLI (Command Line Interface) throughout this section.

#### 1.1.a Nodes
**Nodes:** A node in ROS2 represents a process that performs computation, such as sensing, control, planning, or actuation, and typically communicates with other nodes using the ROS2 communication framework. 

First in your terminal, run `ros2 node list`. This will list all running nodes. You should currently have 0 running nodes. Now, in the terminal, run `ros2 run helpers node_q_1_1`. After you run the node, how many nodes are now running? Change the value of `num_nodes` (in ```question_1_1.py```) to the new number of nodes. 

#### 1.1.b Node Names
Change the value of `first_node_name` to the name of the first node. Make sure you include the starting ```/```.

**Note:** When we ran the node, we used the command `ros2 run helpers node_q_1_1`. As you can see, the name `node_q_1_1` will not always 
match the name of the node. Here, `node_q_1_1` refers to the executable name, which is defined in `setup.py`.

#### 1.1.c Topics

**Topics:** A topic is a communication channel that allows for messages to be sent between nodes.
**Messages**: A message is an object that contains information such as an image, a velocity, etc.

Stop the node. This can be done by going into the terminal where you ran the node and press `CTRL + c`. Once you have killed the node,
run `ros2 topic list`. You should see two topics, namely `/parameter_events` and `/rosout`. These are system-generated topics and you do not have to worry about these topics for now. Again, run `ros2 run helpers node_q_1_1`. Change the value of `num_topics` to the new number of topics. 

#### 1.1.d Topic Info
Sometimes you may want to find information about a topic. You can use `ros2 topic info TOPIC_NAME` to do so. First, run `ros2 topic info /tutorial/OdometryPub`. Note the fields `Type`, `Publisher count`, and `Subscription count`. One of the other topics is called `/tutorial/MysteryPub`. We want to find what type of message this topic publishes. Change the value of `topic_message_type` to the correct message type of the topic `/tutorial/MysteryPub`. Write your answer as a string. For example, the answer for ```/tutorial/OdometryPub``` would be ```"nav_msgs/msgs/Odometry"```. 

#### 1.1.e Topic Echo
When debugging, it sometimes important to check out what messages are being published to a topic. A useful command for this is `ros2 topic echo TOPIC_NAME`. Change the value of `string_message` to the string that is being published to the topic `/tutorial/StringPub`. 

**Note:** do not include ```"data: "``` in your answer.

<hr>

</details>

<details>
<summary><strong>1.2 Coding Subscriber and Publishers</strong></summary>

<hr>

The goal of this section is to understand what a publisher and subscriber is within ROS2 and how to create them. Please look at file `question1_2.py`. You may run ```ros2 run helpers node_q_1_2.py``` to debug your answer.

#### 1.2.a Creating a subscriber to a topic

**Subscribers/Subscription:** A subscriber is a component of a node that allows the node to receive information and data from a topic.

For this question, fill in the blanks to create a subscriber.
This subscriber should
- Take in a message type `String`
- Subscribe to the topic `/tutorial/basic_topic`
- Have its callback be `self.topic_callback`
- Qos profile of 10

**HINT:** There should be four parameters that you fill

#### 1.2.b Creating a publisher
**Publishers:** A publisher is a component of a node that allows the node to send information and data to a topic.

For this question, fill in the blanks to create a publisher.
This publisher should
- Publish a message type `String`
- Publish to a topic `/tutorial/new_topic`
- Qos profile of 10

**HINT:** There should be three parameters that you fill

#### 1.2.c Message Data
Please see what the String message type consists of: https://docs.ros.org/en/melodic/api/std_msgs/html/msg/String.html.
For this question, access the string field from the variable `msg` and store it into the variable `self.topic_string_message`

#### 1.2.d Publishing Data
For this question, take the value from `topic_string_message` and append the string ` ROS` (don't forget the space). The new string should look like `Hello World! ROS`. Then use the variable `new_message` to publish this new string using the publisher from **Q1.1.b**.

<hr>

</details>

<details>
<summary><strong>1.3 Counter Node</strong></summary>

<hr>

This question is designed to test your knowledge on this topic. Take a look at `question_1_3.py`. The goal of this node is to publish to a topic called `/tutorial/counter25` with numbers of type `Int32` starting from 0 incrementing to 25 inclusive. A rough outline has been provided for you. Fill in the blanks to complete this question.

**HINT:** It may be useful to debug your node using `ros2 run student_code question_1_3` and `ros2 topic echo /tutorial/counter25`.

<hr>
</details>

<details>
<summary><strong>1.4 Services</strong></summary>

<hr>

**Services** are another type of communication mechanism. It consists of a **client** that sends a request to a **service**, which then returns a response. 
Some examples of where services may be used are:
- Querying information
- Setting parameters
- Simple one time calculations
 
For example, I may have a client that requests the position of a buoy from a mapping service.

In this question, you will be coding exactly the scenario described above. The relevant files you will be editing are `question_1_4_client.py` and `question_1_4_service.py` in `student_code` and `GetBuoyLocation.srv` in `tutorial_msgs/srv`.

#### 1.4.a Creating a Custom Message
Services require a custom message to work. Take a look at `tutorial_msgs/srv/GetBuoyLocation.srv`. You'll notice that there are two fields in this message seperated by a `---`. The first field represents the request data the client sends to the service. The second field represents the response data that the service sends back to the client.

For this message, we want the request to be a variable of type `string` with the name `buoy_name`. For the response, we want three variables, two of type `float32` and one of type `bool`. The first `float32` should be called `x_pos` and the second one called `y_pos`. The `bool` should be called `found`, Fill out the blanks in the provided file.

**HINT:** Take a look at `TemplateServiceMessage.srv` to see a template service message.

#### 1.4.b Creating a Serivce

Create the service. This should use the `GetBuoyLocation` service message, use the service topic `/tutorial/get_buoy_location`, and have its handler be `self.handle_get_buoy_location`.

#### 1.4.c Handling a request from a Client

Go to the file `question_1_4_service.py`. Complete the `handle_get_buoy_location` function. An example of how to access the request component of the service is provided for you. Following this example, fill out the response. If the requested buoy is not in the map, set the `found` parameter to `False`, else if found set the parameter to `True`.

#### 1.4.d Sending a request to a Service

Go to the file `question_1_4_client.py`. Correctly request a `yellow_buoy` from the service. 

<hr>
</details>

## Topic 2: Simulation + Useful Tools

**Note:** There are no tests for this section.

<details>
<summary><strong>2.1 Using VNC</strong></summary>

<hr>

**VNC (Virtual Network Computing)** is a graphical desktop-sharing system that allows you to access another desktop's enviornment over a network.

In our case, we will be accessing the docker container's generated desktop environment. To do so, go into your web browser and type `localhost:6080`. This should bring you to a webpage that looks something like the below image.

<img src="assets/vnc_weblanding.png" alt="VNC web landing" width="800"/>

Press connect and you should have access to your docker container's VNC.

<hr>
</details>

<details>
<summary><strong>2.2 Running Simulation</strong></summary>

<hr>

In your terminal, run `ros2 launch stinger_bringup vehicle_sim.launch.py`. You should see something along the following:

<img src="assets/sim_startup.png" alt="Sim start up" width="800"/>

If you zoom out, you should be able to see a stinger tug model.

<img src="assets/sim_stinger_tug.png" alt="Sim stinger tug" width="800"/>

Later in this tutorial, you will be developing different algorithms for perception, control, and autonomy. You may want to test these out in different environments. To do so, you can run the sim launch command with the `world:=` parameter. For example, if you wanted to run a different world called `secondary.world`, you would run the following

```
ros2 launch stinger_bringup vehicle_sim.launch.py world:=secondary.world
```

All of the available worlds can be found in `stinger-software/stinger_sim/worlds`.
<hr>
</details>

<details>
<summary><strong>2.3 rqt_image_view</strong></summary>

<hr>

**rqt_image_view** is a tool used to see images being published over topics.

First start the simulation `ros2 launch stinger_bringup vehicle_sim.launch.py`.

Then, in a separate terminal, run `ros2 run rqt_image_view rqt_image_view`. You should see something like this:

<img src="assets/rqt_image_view_opened.png" alt="Opened rqt_image_view" width="800"/>

Select the dropdown.

<img src="assets/rqt_image_view_dropdown.png" alt="Dropdown rqt_image_view" width="800"/>

**Note:** If nothing pops up in the dropdown, click the refresh button right next to the dropdown a couple of times and try again.

Then select the camera topic you want to visualize. In our case, select `/stinger/camera_0/image_raw`. You should see something like the following.

<img src="assets/rqt_image_view_image.png" alt="Image rqt_image_view" width="800"/>

<hr>

</details>

<details>
<summary><strong>2.4 Rviz2</strong></summary>

<hr>

**rivz2** is a 3D visualization tool for various parts of the robot that include sensor data, transformations, markers, robot models, etc.

Make sure the simulation is launched. Then in another terminal, type `rviz2`. You should see something like this:

**Note:** sometimes we refer to `rviz2` as simply `rviz`.

<img src="assets/rviz2.png" alt="Rviz2" width="800"/>

We are going to display the data coming from the lidar sensor. First, click add in the bottom left corner.

<img src="assets/rviz2_add.png" alt="Rviz2 add" width="800"/>

This will list out the different type of information you can visualize using rviz. Next, click the `By topic` tab.

<img src="assets/rviz2_by_topic.png" alt="Rviz2 by topic" width="800"/>

This will list out the current topics from the robot that can be visualized. We want to visualize the lidar, so click the dropdown `/scan` and then select `LaserScan`

<img src="assets/rviz2_topic_dropdown.png" alt="Rviz2 topic dropdown" width="800"/>

Next we need to change the `Fixed Frame` from `map` to `base_link`. We will learn more about what these mean in a later section.

<img src="assets/rviz2_fixed_frame.png" alt="Rviz2 fixed frame" width="800"/>

Now, you should see some extremely small red dots in the grid. To make them more visible, we can select the `LaserScan` dropdown and increase the `size` to `0.1`.

<img src="assets/rviz2_bigger.png" alt="Rviz2 bigger" width="800"/>

Now you should be able to see these red squares. We will learn more about what a Lidar sensor is in a later section.


<hr>

</details>

## Topic 3: Conventions

<details>

<summary><strong>3.1 Unit Conventions</strong></summary>

<hr>

**Distance:** meters (m)<br>
**Angle:** radians (rad)<br>
**Time:** seconds (s)

</details>

<details>

<hr>

<summary><strong>3.2 Coordinate Conventions</strong></summary>

Coordinate conventions are used to ensure consistent interpretation of spatial data (like position, velocity, etc.) across different systems. So for example, if I said a point was at position `(2, -3, 0.5)` relative to me, coordinate conventions would define which variable means "forward", which variable means "up" or "down", does the negative mean "left" or "right" etc.

ROS uses the right-handed coordinate system. The most important coordinate convention is the relative-to-body convention.

We will use your right hand to demonstrate the relative-to-body convention.

#### 3.2.a Linear Coordinate Conventions
For this topic, we will cover the convention for linear coordinate frames (such as position, velocity, acceleration, etc). Following the example, say I give you a point at position `(2, -3, 0.5)` relative to you. Make this gesture with your right hand with your pointer finger pointing forward.

<img src="assets/right_hand_rule.jpg" alt="right hand rule" width="800"/>

Your index finger represents `x`(forward/backward) and the direction your finger is pointing is considered the positive direction. So, `x = 2` means the object is 2 meters in front of you. Your middle finger represents `y`(left/right). So, `y = -3` means 3 meters to the right of you. Your thumb represents `z`(up/down). So, `z = 0.5` means 0.5 meters above you.

**Note:** In aerospace we use different terms instead of `x`, `y`, `z` when representing linear motion, namely, `surge`, `sway`, `heave`.

In a terminal, run `ros2 launch stinger_bringup vehicle_sim.launch.py world:=grid.world`. You should see a simulation with a grid overlayed on top of the world. Each box represents 1 meter by 1 meter. Look at `question 3.2.a` in `question_3_2.py`. Assign each variable with the correct pose of each buoy using the relative to body convention to the stinger tug.

**Note** For this question, ignore the z-axis and all orientation axes.

**Hint**: [Pose definition](https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Pose.html)

#### 3.2.b Angular Coordinate Conventions

The 3 rotational degrees of freedom in the body frame are `roll`, `pitch`, and `yaw`, which represent the rotation about the X-axis, Y-axis, and Z-axis respectively. The image below gives a good visual representation of these rotational axes.

<img src="assets/Yaw_Axis_Corrected.svg" alt="rotational axes" width="800"/>

To determine the directionality of an angle, we must use the right hand rotation convention. For example, say we want to determine the positive direction of the roll axis. To do so, make this gesture with your right hand.

<img src="assets/RotationConvention.jpeg" alt="rotational convention" width="800"/>

Since the roll axis corresponds with the X-axis, point your thumb forward (where your pointer finger would have pointed with the right hand rule). Then, curl your hand in the direction that your fingers point (use the figure as reference). This corresponds to the positive direction.

**Note:** The directionality of the angular axes in the plane diagram are wrong.

Again, in a terminal, run `ros2 launch stinger_bringup vehicle_sim.launch.py world:=grid.world`. Look at `question 3.2.b` in `question_3_2.py`. Assign each variable with the correct yaw angle of each buoy w.r.t (with respect to) the stinger-tug using the above convention.

**Hint** Use your answers from question `3.2.a` and `np.arctan2`.

<hr>

</details>

<details>
<summary><strong>3.3 TF Frame Conventions</strong></summary>

<hr>

TF (transform) Frames define how different components move relative to each other. 

In a terminal, run `rviz2` and `ros2 launch stinger_bringup vehicle_sim.launch.py`. 

In `rviz`, first ensure that you have the `base_link` frame selected.

<img src="assets/rviz2_baselink.png" alt="rviz2 base link" width="800"/>

Then click `Add` -> `TF`. Expand the `TF` on the side bar and enable `Show Names`. You should see something along the following.

<img src="assets/tf_frames.png" alt="tf frames" width="800"/>

What you are seeing are the current TF frames being displayed. Go to `Frames` and disable all the frames except for `base_link`. You should see something like this:

<img src="assets/tf_baselink.png" alt="tf base link" width="800"/>

The most basic frame is called the `base_link`. This is the robot's base frame and typically represents the center of the robot. As you can see, the `base_link` follows the right hand coordinate convention, with red representing `x`, green representing `y`, and blue representing `z`. 

All components, such as sensors and thrusters, are defined w.r.t the `base_link`. Enable the `camera_0` frame. You should see something like the following:

<img src="assets/camera_frame.png" alt="tf base link" width="800"/>

Notice that the camera frame falls infront of the `base_link` frame. This is because the camera is positioned forward of the center of the stinger tug. It is important to define these TF Frames because we can use these to properly transform any data coming from the camera into the relative body frame (`base_link`).

Two other very important coordinate frames are the `odom` and `map` frame. The `odom` frame is typically used to represent where the robot thinks it has moved to w.r.t where it started. The odom frame is always centered to where the robot started. The `map` frame is typically used to represent the robot's position in the environment and is supposed to be a global fixed frame. The `map` frame does not have to be centered to where the robot started.

<hr>

</details>

## Topic 4: Localization

<details> <summary> <strong> 4.0 Localization </strong></summary>

<hr>

In the context of robotics, localization refers to the process by which a robot determines its pose (position and orientation) within its environment. The robot may use sensors such as an IMU, GPS, or cameras to do so.

<hr>

</details>

<details> <summary> <strong> 4.1 Odometry </strong> </summary>

<hr>

When dealing with localization, we commonly use the [Odometry Message Type ](https://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html) to encapsulate our localization information. This message contains a `pose` (position) and a `twist` (velocity) field with a covariance matrix. The covariance matrix represents the uncertainty in our estimation for that field. So for example, a high covariance for our `pose` would mean that we have high uncertainty about the accuracy of our estimated position. We will see the covariance matrix's importance in a later section.

<hr>

</details>

<details> <summary> <strong> 4.2 IMU</strong></summary>

<hr>

An Inertial Measurement Unit (IMU) is a sensor used to measure a robot's acceleration (accelerometer), angular velocity (gyroscope), and orientation (magnetometer). They usually look something like the following.

<img src="assets/gx4.jpg" alt="imu" width="800"/>

For the following sections, we will be breaking down the standard IMU message type. See [here](https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html).

#### 4.2.a IMU Message: Linear Acceleration

The linear acceleration field of the IMU is composed of a 3D vector, representing the linear acceleration captured by the IMU in the `x`, `y`, and `z` directions in the IMU frame. 

**Note:** The IMU will usually capture the effet of gravity. Because of this, even when the IMU is stationary, we will see a linear acceleration of +9.81 m/s^2 in the heave direction of the robot.

In seperate terminals, run the following:

```
ros2 launch stinger_bringup vehicle_sim.launch.py
ros2 topic echo /stinger/imu/data --field linear_acceleration --no-arr --once
```

Notice how when displaying the linear acceration for the IMU the acceleration in the `z` direction is around `-9.81`, when it should be `+9.81`. This is because the IMU measures data in its local coordinate frame which may not match up directly with the robots coordinate frame. We will explain this in the next section.

#### 4.2.b IMU Message: TF Frames

Reference the above picture of the IMU. In the bottom right corner, you can see that there are 2 arrows representing the `x` and `y` directions. The `z` direction is denoted by an cross symbol to represent that the `z` axis is pointed into the plane. See the below as reference.

<img src="assets/in_out_plane.png" alt="in out plane" width="800"/>

The left represents a vector into the plane, the right represents a vector out of the plane. 

Notice that the IMU's coordinate axes follow the right hand rule. These axes represent the IMU's local sensor frame. Look at the TF frames of the stinger tug in the picture below.

<img src="assets/baselink_frame.png" width="800"/>

As a reminder, this is what the base_link frame looks like w.r.t to the stinger tug.

<img src="assets/imu_to_baselink.png" width="800"/>

Notice that the imu frame is upside down w.r.t to the base_link frame. This is because of how the IMU is mounted inside of the stinger tug and explains why we were seeing a negative gravity acceleration when we should have seen a positive one.

In `question_4_3.py`, look at the `transfrom_imu(self, msg: Imu)` function. It is okay if you do not completely understand everything in the function. If you ever find yourself needing to do something similar in the future, you can copy paste this function and modify it to fit your needs. This function will take an incoming IMU message in its local frame, and convert all of its data to be in the base_link frame.

In seperate terminals, run the following:

```
ros2 launch stinger_bringup vehicle_sim.launch.py
ros2 run student_code question_4_3
ros2 topic echo /debug --field linear_acceleration --no-arr --once
```

Now, notice how the linear acceleration in the `z` direction correctly outputs `+9.81`.

By converting the IMU into the base_link frame, it is now easier to use the IMU to localize the stinger tug. It is common for sensors to be in a different frame than the base link frame. To make the data more useful, you will usually have to go through a similar process to convert it into the base link frame.

#### 4.2.b IMU Message: Orientation

Look at the orientation field of the IMU message. Notice that the field type is an Quaternion. A quaternion is a different way of representing angles compared to euler angles (your standard roll, pitch, yaw, [-pi, pi]). Quaternions are often preferred over euler angles in robotics since they have some nice mathematical properties and avoid some common problems with euler angles. If you want a more in depth explanation see [here](https://en.wikipedia.org/wiki/Quaternion). 

Quaternions are reprenseted in a 4D space, which is difficult for us to interpret. This is why we commonly convert quaternions back into euler angles when needing to work with them for intuitive tasks, such as, what angle is the buoy from my stinger tug.

A useful tool for visualizing quaternions is to use `plotjuggler`. In seperate terminals, run the following:

```
ros2 launch stinger_bringup vehicle_sim.launch.py world:=empty.world
ros2 run student_code question_4_3
ros2 run plotjuggler plotjuggler
```

When you open it up, you should see something like this:

<img src="assets/plotjuggler.png" width="800"/>

Click `Start`

<img src="assets/pj_start.png" width="800"/>

Select the `debug` topic to visualize and press `Ok`.

<img src="assets/pj_topic.png" width="800"/>

Expand the `debug` field and expand orientation.

<img src="assets/pj_orientation.png" width="800"/>

Right click the empty space.

<img src="assets/pj_right.png" width="800"/>

Select the `Split Vertically` option. Do this again and you should have something like this. 

<img src="assets/pj_3_frames.png" width="800"/>

Then from the left hand side under orientation, drag the `roll` field into the top plot, `pitch` into the middle plot, and `yaw` into the bottom plot. You should see something like this:

<img src="assets/pj_orientation_frames.png" width="800"/>

Each plot displays each euler angle as a function of time. 

Keep everything running, in a seperate terminal, run:

```
ros2 run helpers node_q_4_2
```

Notice that as the stinger turns left, the yaw positively increases, which correctly follows the relative to body convention.

<img src="assets/pj_yaw.png" width="800"/>

#### 4.2.c IMU Message: Angular Velocity

The last part of the IMU message is the angular velocity. There are three values, representing the angular velocity in the `x`, `y`, and `z` direction in radians/second.

<hr>

</details>

<details><summary><strong>4.3 Dead Reckoning</strong></summary>

<hr>

Dead reckoning is a navigation technique used to localize a vehicle by calculating its position by tracking speed, direction, and time traveled.

#### 4.3.a Odom Frame

Run the following:

```
ros2 launch stinger_bringup vehicle_sim.launch.py world:=empty.world
ros2 run student_code question_4_3
ros2 run plotjuggler plotjuggler
```

Select the `/debug` topic to visualize and plot the linear acceleration in the `x` and `y` directions. You should see something like this.

<img src="assets/imu_base.png" width="800"/>

Then in a terminal, run

```
ros2 run helpers node_q_4_2
```

Take a look at your `plotjuggler` graph, you should see something like this:

<img src="assets/imu_going.png" width="800"/>

Now look at the simulation, you should see that the stinger tug is going forward and to the left. However, our plot juggler graphs are showing us that our stinger tug is accelerating to the right. This must mean that even after transforming our IMU into the 
`base_link` frame, there is something still wrong.

This is where the `odom` frame comes in. If you don't remember its definition, check out `3.3 TF Frame Conventions`. When we talk about localization, we always discuss it in the `odom` frame. This `odom` frame will origin its coordinate frame where the `base_link` frame starts (where the robot initializes). To better outline the difference between the `base_link` frame and the `odom` frame, follow this example of an IMU transformed to the `base_link` frame vs the `odom` frame.

| English     | base_link POV | odom POV |
|-------------|-------------|-------------|
| Robot moves forward 1 meter     | Robot moves 1 meter along its x-axis  | (0, 0) -> (1, 0)  |
| Robot turns 90 degrees to the left  | Robot turns 90 degrees to the left  | Robot faces 90 degrees to the left  |
| Robot moves forward 2 meters | Robot moves 2 meters along its x-axis  | (1, 0) -> (1, 2)  |
| Robot turns 45 degrees to the left  | Robot turns 45 degrees to the left  | Robot faces 135 degrees to the left|

To correctly localize ourselves, we must convert our `base_link` measurements into the `odom` frame. With an IMU, this involves using the IMU's orientation to rotate the `linear_acceleration` and `angular_velocity`. Look at `question_4_3.py`, complete `4.3.a Odom Frame IMU` by rotating the `linear_acceleration` and `angular_velocity` from `msg_base_link` with `msg_base_link.orientation`. 

**Hint:** Use the code in `transform_imu` as reference.

#### 4.3.b IMU Dead Reckoning

As you might recall from physics, acceleration is the change in velocity (derivative) and velocity is the change in position. Therefore, given the linear acceleration from the IMU, we can integrate the linear acceleration to get velocity and integrate the velocity to get position. As a reminder,

<img src="assets/position_acceleration.png" alt="position acceleration" width="800"/>

Look at `question_4_3.py`, complete `4.3.b IMU Dead Reckoning`. For this question, we want to publish to the topic `/stinger/odometry` an odometry message containing the following fields:
- frame_id
- child_frame_id
- twist
- pose

For all fields relating to heave, you can set it to 0. Also, disregard the covaraince fields. A topic called `/ground_truth/odometry` is given to you which you should use to verify your computation. 


To run your code and verify, run in seperate terminals:

```
ros2 launch stinger_bringup vehicle_sim.launch.py world:=empty.world
ros2 topic echo /ground_truth/odometry --no-arr
ros2 run student_code question_4_3
ros2 topic echo /stinger/odometry --no-arr
ros2 run helpers node_q_4_2
```

You may also find it useful to use `plotjuggler` to visualize your output.

**Hint:** Use the variables defined in the constructor.

**Note:** IMU's are rarely solely used to localize a vehicle. This is because IMU's typically experience something called IMU drift, where over time, the IMU will accumulate error that gets exponentiated through integration in the velocity and position estimates. The reason it works in simulation is because the IMU's are almost ideal and errorless.

<hr>

</details>

<details> <summary> <strong> 4.4 robot_localization</strong></summary>

<hr>

#### 4.4.a Integrating IMU in robot_localization

In section 4.3, we estimated our odometry using only one odometry source (the imu). Now what if we have multiple IMUs and other odometry sources (such as a GPS) each in their own frame. For example, at a given time our IMU might think that we are at position (3.0, 4.2), while our GPS thinks that we are at position (3.1, 4.0). So how should we fuse this data together?

`robot_localization` is a package that provides a node called `ekf_node`. If you're interested in deeply understanding what an Extended Kalman Filter is, a good resource is [MIT Tutorial: Kalman Filter](https://web.mit.edu/kirtley/kirtley/binlustuff/literature/control/Kalman%20filter.pdf) (not mandatory). The general idea is that the `ekf_node` will fuse a set of unreliable/weak odometry sources and form a stronger estimate of our odometry. It will also take care of all tf transforms as long as they are defined and broadcasted.    

Take a look at `stinger-software/stinger_bringup/config/ekf.yaml`. This config file will define the parameters for the `ekf_node`. The most important parameter in this config file is defining which fields (see below) from each odometry source should be used in our estimate. This is important because for example, our IMU doesn't natively report our `x_pos` or `y_pos`. Because of this, the `ekf_node` needs to know to ignore these fields.

```
[x_pos   , y_pos    , z_pos,
 roll    , pitch    , yaw,
 x_vel   , y_vel    , z_vel,
 roll_vel, pitch_vel, yaw_vel,
 x_accel , y_accel  , z_accel]
```

In the `ekf.yaml`, look at the `4.4.a Example`. This array defines which fields should be used. Each boolean value in the array corresponds to an odometry field in the above array. So in this example configuration, we enable feeding the `x_pos`, `y_pos`, and `yaw` into the ekf (this configuration is not right, just an example).

Look at `TODO: 4.4.a Integrating IMU in robot_localization`. Following from the example, correctly define which odometry fields should be fed into the ekf from the IMU.

**Note:** Exclude linear acceleration (among other things). This means your last 3 values should be false.

**Hint:** What fields are defined in the IMU message? You should be using all of them.

To run the tests:

```
ros2 launch autograder test_4_4.launch.py
```

#### 4.4.b GPS and Navsat Node

Launch the simulation and run

```
ros2 topic echo /stinger/gps/fix
```

The message over this topic is of type [NavSatFix](https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/NavSatFix.html). Notice how our position is given in terms of longitude and latitude. Out of the box, this isn't useful to us because we need our position in terms of x and y in meters. To handle this, `robot_localization` provides a node called `navsat_transform` that will transform a `NavSatFix` message from a gps into an `Odometry` message that we can more easily use.

The `navsat_transform` node requires the following topics: `/imu`, `/gps/fix`, and `/odometry/filtered` (you can ignore this one for now). But, the topics for our sensors are `/stinger/imu/data` and `/stinger/gps/fix`. This is where topic remapping comes into use.  

Look at `stinger_bringup/launch/localization.launch.py` `TODO: 4.4.b Navsat Node`. In the arguments of the second `Node` definition, there is a parameter named `remappings`, which is an array of tuples. An example is given of how to remap a topic. For this question, correctly remap the imu and gps topics.


To run the tests:

```
ros2 launch autograder test_4_4.launch.py
```

#### 4.4.c Everything Together

Now with our GPS converted into odometry, we want to fuse this with our IMU to form a strong odometry estimate. 

In seperate terminals, run:


```
ros2 launch stinger_bringup vehicle_sim.launch.py
ros2 launch stinger_bringup localization.launch.py
ros2 topic echo /odometry/gps
```

Publish commands to the motors using `rqt` and take note of which odometry fields from `/odometry/gps` are relevant. This is important because some fields (such as orientation) are left 0 and we do not want to include these invalid fields into our ekf.

Again, take a look at `stinger-software/stinger_bringup/config/ekf.yaml`. Following the structure of the IMU config, add the config for the GPS with only the relevant odometry fields.

<hr>

</details>

<details> <summary> <strong> 4.5 Localization Wrap-up</strong></summary>

<hr>

Take a look at `stinger_bringup/launch/vehicle_sim.launch.py`. Follow the instructions and uncomment the code block.

Then, in seperate terminals run,

```
ros2 launch stinger_bringup vehicle_sim.launch.py
ros2 run plotjuggler plotjuggler
rqt
```

In plotjuggler, click `Start` and select these two topics.

<img src="assets/localization.png" width="800"/>

Vertically split the plots.

<img src="assets/vertically_split_plots.png" width="800"/>

Then, expand the `ground_truth` topic until you see `position x y`. Shift click `x` and `y`.

<img src="assets/shift_click.png" width="800"/>

Then, right-click the fields. While continuing to hold down the right-click, drag the fields onto a plot. Then click OK.

<img src="assets/curve.png" width="800"/>

You should see something like this.

<img src="assets/truth_plot.png" width="800"/>

Repeat this process for `/odometry/filtered`. You should see something like this.

<img src="assets/two_plots.png" width="800"/>

Now, using rqt, publish anything to the motors. You should see that the two curves are roughly the same.

<img src="assets/two_curves_moving.png" width="800"/>

If everything looks good, congratulations! You just localized the stinger-tug.

<hr>

</details>

## Topic 5: Control

<details>
<summary><strong>5.0 Overview</strong></summary>
<hr>

Control refers to how our robot should command its motors to achieve a desired motion (i.e. going forward in a straight line). In this section, we'll cover the most fundamental **feedback** controller called PID. A feedback controller uses sensor measurements of the robot’s motion to continuously adjust its motor commands, keeping the robot’s actual behavior close to the desired one.

For example, say we wanted to go 1 m/s forward. From the previous section, we coded a robust way to localize our stinger tug. With this information, we can constantly see our current velocity. Say we try to command our motors to push us forward with 1 N. From our localization, we see that we are only going 0.3 m/s. Since we are pretty far off from our desired velocity (0.7 m/s below our desired), we decide to really increase our throttle and instead command 2 N of force to our motors. Again, from our localization we see that we are now going 0.9 m/s. This time, we're only off by 0.1 m/s, so we slightly increase our throttle to 2.3 N of force. This is the backing idea behind a PID feedback controller, where you apply a motor thrust, compare the current velocity with the desired velocity, and adjust our commanded motor thrust based on this difference.

If at any point, you are not vibing with the way information is taught in this section, feel free to refer to this fantastic video: https://www.youtube.com/watch?v=wkfEZmsQqiA. 

</details>
<details>
<summary><strong>5.1 PID Controller</strong></summary>
<hr>

All code will be in `stinger_controller/velocity_controller.py`. Tests for this section can be run with:

`ros2 launch autograder test_5_1.launch.py`

A PID controller has 3 parts: a (P)roportional term, a (I)ntegral term, and a (D)errivative term. Each of these terms has a specific use case. The general PID controller can be formulated as:

<img src="assets/pid_diagram.png" width="800"/>

Here, the terms `K_p`, `K_i`, `K_d` are the "gains" to the controller. These are just numbers that influence the affect of each term. Usually, with PID controllers, they need to be "tuned", which means adjusting these values. We will come back to these values in a later section.

#### 5.1.a Velocity Controller Setup
<hr>

Create a subscription to the topic `cmd_vel` and use the callback function `cmd_vel_callback`. We intentionally are not telling you the message type, see if you can figure it out!

Create a subscription to the topic `/odometry/filtered` and use the callback `odometry_callback`.

Create a publisher to `/cmd_wrench`. **Hint:** Looking at `throttle_controller.py` may be useful for this.

#### 5.1.b Error Calculation
<hr>

In the overview, we provided a quick example of the general idea of a PID controller. We made one very important calculation: the error. This error is what we are "feeding back" into the controller and lets the controller how much to adjust to get to our desired velocity. This calculation will make more sense in later sections when we introduce the proportional, integral and derivative terms.

For this question, calculate the error of the robot's velocity in the surge direction. For proper sign convention, do `error = commanded - current`.

#### 5.1.c Proportional Calculation
<hr>

The idea of the proportional term is "the greater the error the more I correct, the smaller the error the less I correct." For example, imagine a situtation where you are driving a car on the highway and your sole goal is to stay in your lane. In this scenario, the "error" would be the distance your car is from the center of your lane. You will have high error if you are really out of your lane, and you will have low error if you are roughly staying in your lane.

In this scenario, lets say your only control is your steering. When your error is large (when you are really far off your lane), you need to turn your car a lot to get back into your lane. When your error is small (when you are roughly in your lane), you will only need to smake small adjustments to center your car in your lane.

This is the overall idea behind the Proportional term. The higher your error, the more drastic your control needs to change. The smaller your error, the less your control needs to change.

For this question, calculate the proportional term. It should look something like this: `P = K_p * error`.

#### 5.1.d Integral Calculation
<hr>

The integral term says: “If I’ve been off for a while, I should keep nudging harder until the long-term error is gone.” Back to the highway example, imagine your car loves to drift to the right even when you try to steer straight. Over time, you'll realize that your car tends to drift to the right, so from then on you remember to always turn slightly to the left to stay centered. This is the idea behind the integral term for the controller.

The integral term will add up accumulated error from the past and counteract it.

For this question, calculate the integral term like:

```
I_total += e_k * Δt
I = K_i * I_total
```

#### 5.1.e Derivative Calculation
<hr>

The derivative term is in charge of smoothing your control output. In the highway example, imagine you're going 100mph. If you drastically steer to the left to center yourself in the lane, you'll lose control of the car quickly and swerve (and potentially crash).

The derivative term is in charge of looking at the rate of change of the error, essentially "looking into the future" (through the derivative). If the rate of change of the error is decreasing, we can infer that we are approaching our desired control. Because of this, we should dampen our control output to prevent us from overshooting. 

For this question, calculate the integral term like:

```
D = K_d * (change in error) / dt
```

#### 5.1.f Yaw Control
<hr>

Now apply the same concepts from `5.1.b - 5.1.e` to calculate the correct yaw control output.

#### 5.1.g Controller Tuning
<hr>

Each term has an associated gain (constant value) that affects the influence of each term. For example, if you want a system to react super quickly, you may want a high proportional gain. If you instead prefer system stability, you might want to have a higher derivative term. Tuning/changing these values are an important step to make your system react the way you want it to. This is often called "tuning" the controller.

For this section, override the default gain values and tune the controller. The autograder will pass if for 350 iterations, your controller on average can control the robot's velocity to be within the desired velocity by `0.075 m/s`.

Tips on tuning values:

1. Increase `K_p` first until the control starts oscillating
2. Increase `K_d` until the control stabilizes
3. Repeat steps 1-2
4. Increase `K_i` if needed 

**Tip:** Use plot juggler! Very useful to see whats happening in the back.

</details>

## Topic 6: Perception
<details>
<summary><strong>6.0 Overview</strong></summary>

<hr>

Human cannot walk around fully blind. Same thing goes for robots. To see, Stinger has a simple web camera. Our job is to make use of the video stream input, and make sense of what we are seeing. You can do perception the traditional or modern way. Tesla's Full Self Driving system uses an end-to-end neural network to process visual inputs. For Stinger, a Raspberry Pi does not have the compute to do that. Using traditional computer vision method is the way to go. 

Our main job here is to recognize the pair of buoy by: 
- isolate the target from the background
- make sure the isolation resemble the shape of the buoy
- output location of the pair of gate
Fortunately, OpenCV has libraries that can help us do that. 

<hr>

</details>

<details>
<summary><strong>6.1 Traditional Computer Vision</strong></summary>

<hr>

Student code is in `stinger_perception/detection.py`

#### 6.1.a Understanding HSV

To isolate the target from the background, we would first need to find the color mask. The image from the web camera is in RGB format. For example, [240,243,162] is the RGB code for the color butter yellow. The 3 numbers are in the range of 0 - 255. 

However, butter yellow RGB color-code differs under different lighting conditions. That's where HSV model comes in. 
- H (Hue): The base color
- S (Saturation): The intensity of the color
- V (Value): The brightness of the color

Hue is expressed in degrees, from 0° to 360°. Approximately 0 is red, 120° is green, and so on.

Saturation is expressed from 0 to 100%. At 0%, everything is basically gray. As it increases, the color becomes more solid. The percentage will get multipled by 255 

Value is also expressed from 0 to 100%. At 0%, it is dark so color will appear black. As it increases, the color becomes more visible.

Here is a picture for visualization (credit Dijin Dominic on Medium):
<img src="assets/hsv.png" width="800"/>

However , we are using the OpenCV library to convert RGB to HSV. The range is expressed differently. Do some google searches and find the upper and lower thershold of the color red and green in HSV format. We will need it in the next section for masking. 

#### 6.1.b Masking

Now that we have our color mask, we can use that range of value to isolate the object. 

For the picture below, imagine the apple is red, and the trophy is green. This is what you have after applying masking. Look for the OpenCV library that helps you do that!

<img src="assets/bnw_mask.jpg" width="800"/>

#### 6.1.c Contours

Contours are curves that join all the continuous points along the boundary. Just like the bottom left image, the green lines are outlining the contours of those shapes. Having these contours helps the robot get the (x, y)coordinates the object. Look for the OpenCV library that does that!

<img src="assets/contours.png" width="800"/>

#### 6.1.d Understanding and tuning pixel radius

Sometimes the robot sees many "red" objects, that could be noises, and these could make their way into our candidate coordinates of the red buoy. We would want to filter them out by size, in theory, the buoy should only over a certain size. We figure out the size of the object by counting the pixels. This is a variable that you would need to tune. What is the minimium pixel value to pass as a buoy?

<img src="assets/pixels.svg" width="800"/>

<hr>

</details>

## Topic 7: Autonomy
<details>
<summary><strong>7.0 Overview</strong></summary>

<hr>

The Tug is trying to find and pass through a pair of red-and-green buoy gate. The `state` that the robot is in determines its behaviors. The primary states of the Tug is outline below. Our job is to define what needs to happen inside each state and what are the transition condition when moving from one state to another. 

<img src="assets/states.svg" width="800"/>

<hr>

</details>

<details>
<summary><strong>7.1 Finite State Machine</strong></summary>

<hr>

Take a look at `stinger_autonomy/state.py`. This node handles robot state transition depending on the information from the perception package. The logic in this code is quite advanced, so feel free to just briefly skim over this node.

Overall, the Tug is moving based on where the gate is located relative to itself. The angle that the Tug needs to turn is determined by the aligment of the percevied center of the gate to the actual center of the gate. 

#### 7.1.a Transition Condition of Search State

Read through the logic in the `search` function. Determine the transition condition to `approaching`. Think about how much misalignment are you willing to tolerate.

#### 7.1.b Transition Condition of Approach State

Read through the logic in the `approaching` function. Determine the transition condition to`passing through`. Think about what the boat will be perceving when it is almost through the gate.

<hr>

</details>

## Topic 8: Setting up the Stinger Tug
<details>
<summary><strong>8.1 Configuring the Raspberry PI</strong></summary>

<hr>

The goal of this section is to setup the Pi on Stinger and make sure the sensors can communicate with the embedding computer.

To start, you will need the following compute hardware:
- Raspberry PI 4b
- microSD card
- A desktop monitor, mouse, and keyboard
- Raspberry PI power supply
- microHDMI to HDMI cable

This section goes through configuring the OS by flashing the microSD card with Ubuntu 22.04 64-bit operating system, setting up ssh permission, and installing ROS2. 

#### 8.1.a Operating system in the PI
  1. Follow the instructions from the following link to flash Ubuntu 22.04 onto the microSD card: [https://ubuntu.com/download/raspberry-pi](url). Follow the `Desktop` tutorial. You need your laptop to do this.
  2. Insert the flashed microSD card into the Raspberry Pi and connect the Pi to a monitor, keyboard, and mouse. Power the Pi, and the monitor will turn on automatically. 
  3. Set the username to `tugxx`, with `xx` be you team number. If you are team 5, it will be `tug05`. Please set the password to `boats0519`.
  4. To give the tug a static IP address, we need to be talking to a travel router that talks to GTother (for example). We have router GLiNet AX3000 in lab. So basically, `GTother` (if you needs internet) -> `Router` -> both your laptop and tug is connected to `Router` -> can `ssh`
  5. The router is set up for you already. Connect to wifi on your laptop: `GL-MT3000-0a9`  OR  `GL-MT3000-0a9-5G`
  - Password: `boats0519`
  6. Admin password for logging in from the web (DNS should be the correct IP): `@boats0519`
  7. If steps 4-6 are too much for you right now - just connect to gtother following this website: [https://auth.lawn.gatech.edu/key/](url)
  8. Type `ifconfig` in the terminal and note the IP address.
  9. To enable SSH on the Pi, enter the following in the terminal:
      ```
        sudo apt install raspi-config
        sudo apt install openssh-server
        sudo raspi-config
      ```
  10. After the UI pops up, select Interfacing Options, then `ssh`, click Yes. 
  11. Also under Interfacing Options, select `I2C`, and enable it as well. Repeat and select `Serial Port`, disable console but enable hardware.

#### 8.1.b SSH
  1. On your laptop, type `ssh <username>@<ip address>` on the terminal. Make sure you can ping the PI before ssh.
  2. After logging into the Pi, follow the link to install ROS2 Humble: [https://roboticsbackend.com/install-ros2-on-raspberry-pi/](url)
  3. You should have installed `colcon` if you followed till the end of the tutorial. One more thing: `sudo apt install build-essential`

<hr>

</details>

<details>
<summary><strong>8.2 Custom Setup in Pi</strong></summary>

<hr>

#### 8.2.a git CLI
  You are on your laptop that is ssh-ed into the Stinger Raspberry Pi.

  On the Raspberry Pi, set up Github CLI if you want conviently push your edits while field testing. You will need to log in to your account.
  
  Follow this link for setup: [https://github.com/cli/cli/blob/trunk/docs/install_linux.md#debian](url)

  If you do not want you team member to commit to github on your behalf (since the group is sharing a Pi), remember to log out after using git. 

#### 8.2.b Setup the Stinger Workspace
  First, setup the workspace by typing this in the terminal: `mkdir {workspace name}/src`

  (inside src) `git clone -b {branch name} --single-branch https://github.com/gt-marine-robotics-group/stinger-software.git`

  Navigate to the directory where the `requirements.txt` is located. This will install all the python library is that needed: `pip3 install -r requirements.txt`

  Follow `INSTALL.md` to make sure all the install from source dependencies are installed in Pi. 

  Run `source /opt/ros/humble/setup.bash` at your workspace directory.

  Before running `colcon build`, remember to install all dependencies using `rosdep install --from-paths src -y --ignore-src`

#### 8.2.c Other setup that makes your life easier
  In the terminal, do the following so the terminal source ROS every time it starts. 
      ```
      nano ~/.bashrc
      source /opt/ros/humble/setup.bash
      ```
      Add `source /home/username/{workspace}/install/setup.bash` to the script
  - tmux (You don't need tmux if you prefer terminal in VSCode, see next step)
  - Enable editing in VSCode while in ssh
  - Use a router instead of dealing with eduroam

<hr>

</details>

<details>
<summary><strong>8.3 Stinger Firmware</strong></summary>

<hr>

#### 8.3.a IMU
IMU communicates with the Pi via I2C protocal. Make sure to follow the steps below to ensure successful transfer of data. 

Topic name: `/stinger/imu/data`

Node name: `imu-node` (will not directly run this node, but you can run this independently if you want to check IMU data.) 

```
    sudo groupadd i2c
    sudo usermod -aG i2c tug1
    sudo chmod 666 /dev/i2c-1
    sudo nano /etc/udev/rules.d/99-i2c.rules
    add line: \textit{SUBSYSTEM=="i2c-dev", GROUP="i2c", MODE="0660"}
    sudo udevadm control --reload-rules
    sudo reboot
```

Check I2C permission is granted: `ls -l /dev/i2c-1` You should see something similar `>> crw-rw---- 1 root i2c 89, 1 Feb 8 10:20 /dev/i2c-1`

#### 8.3.b GPS
The GPS sends data to Pi via serial port. To ensure necessary privilege is granted, follow the steps below to get started. Refer to [https://receiverhelp.trimble.com/alloy-gnss/en-us/NMEA-0183messages_MessageOverview.html](url) for more information on GPS formatting.

Topic name: `/stinger/gps/fix`

Node name: `gps-node` (will not directly run this node, but you can run this independently if you want to check GPS data.) 
    
Make sure you have enabled serial port data transmission following step 4 in Sec \ref{pi-setup}
    `sudo chmod 666 /dev/serial0`

Check GPS Data Format - `ls /dev/serial*`
    `sudo cat /dev/serial0` (change serial port if needed) -- you will see NMEA messages printing on the terminal if GPS is configure correctly. Likely the information needed is `GPGGA`.
    
Adjust the code in GPS node if needed.

#### 8.3.c Localization
Localization is done by fusing IMU and GPS data using Extended Kalman Filter. Check out [https://docs.ros.org/en/melodic/api/robot_localization/html/index.html](url) for more information on how the data are fused together. Using both `ekf_filtered_node` and `navsat_transform_node` at the same time. Remember, drifting is inevitable, edit the `ekf.yaml` file in `/stinger_bringup/config` if needed.

Topic name: `/odometry/filtered`

Node name: `ekf_filtered_node`, `navsat_transform_node`

Note that the data flow should be:

- GPS data (`/stinger/gps/fix`) + IMU data (`/stinger/imu/data`) → NavSat transform node → `/odometry/gps`

- `/odometry/gps` + IMU data (`/stinger/imu/data`) → EKF → `/odometry/filtered`

#### 8.3.d Camera
Camera communicates with the Pi via USB. Check which port the camera is sending data through. The stinger is communicating with the camera via customize node, you can refer to this Medium post for camera drivers that are available out there: [https://jeffzzq.medium.com/ros2-image-pipeline-tutorial-3b18903e7329](url)

Topic name: `/stinger/camera_0/image_raw`

Node name: `camera-node`
- `sudo v412-ctl --list-devices` - check which channel the image is coming in, typically is 0
- `sudo chmod 666 /dev/video0` - to allow permission. Assuming video0 is the camera stream, if not, remember to change to correct channel.
- `rqt` - visualize it in ROS2 (make sure the node is running)

#### 8.3.e LiDAR
An external driver is used to communicate between LiDAR and ROS2. Clone the driver here: [https://github.com/Slamtec/sllidar_ros2/tree/main?tab=readme-ov-file#compile--install-sllidar_ros2-package](url)

Topic name: `/stinger/laser/scan`

Node name: `sllidar_node`
- Remember to navigate to `/src` before doing git clone
- To visualize LiDAR scans, type `ros2 launch sllidar_ros2 view_sllidar_c1_launch.py` in the terminal. Remember RPLIDAR C1 LiDAR is being used. You will need RViz2 for visualization. 
- If visualization is not the focus and only the topic `/stinger/laser/scan` is concerned, run `ros2 launch sllidar_ros2 sllidar_c1_launch.py` instead.

#### 8.3.f Motors
The motor node controls two ESCs using pigpio, based on the thrust commands from autonomy. The thrust values are turned into PWM pulse width that drives the port and starboard motor. 

Topic name: `/stinger/thruster_port/cmd_thrust`; `/stinger/thruster_stbd/cmd_thrust`

Node name: `motor-node`
- Before running the node, remember to initialize the gpio module by running `sudo pigpiod`
- You should hear a beep sound if the motor is connected correctly and ready to run.

<hr>

</details>
