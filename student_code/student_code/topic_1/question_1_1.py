class TutorialTopic_1_1:
    def __init__(self):
        ## TODO: Q1.1.a Nodes
        self.num_nodes = None

        ## TODO: Q1.1.b Node Names
        self.first_node_name = None

        ## TODO: Q1.1.c Topics
        self.num_topics = None

        ## TODO: Q1.1.d Topic Info
        self.topic_message_type = None

        ## TODO: Q1.1.e Topic Echo
        self.string_message = None

        # Enter your answer like this (5 is not the right answer)
        self.num_nodes = 5

        ### STUDENT CODE HERE
        self.num_nodes = 1
        self.first_node_name = "/mock_node_q1_1"
        self.num_topics = 5
        self.topic_message_type = "geometry_msgs/msg/Twist"
        self.string_message = "mrg"
        ### END STUDENT CODE
