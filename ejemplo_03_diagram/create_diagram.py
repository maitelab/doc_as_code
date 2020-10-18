"""
Example taken from: https://towardsdatascience.com/create-beautiful-architecture-diagrams-with-python-7792a1485f97

In linux you may need to install this:     sudo apt-get install graphviz
"""
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda, EC2
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Architecture For Queue System ABC", show=False):
    source = EC2("Backend")

    with Cluster("Event Flows"):
        queue = SQS("event queue")

        with Cluster("Processing"):
            handlers = [Lambda("proc1"),
                        Lambda("proc2"),
                        Lambda("proc3")]

    store = S3("events store")
    dw = Redshift("analytics")

    source >> queue >> handlers
    handlers >> store
    handlers >> dw