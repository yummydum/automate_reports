from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2, ECR, Batch
from diagrams.aws.storage import SimpleStorageServiceS3,EFS
from diagrams.onprem.client import Users
from diagrams.onprem.container import Docker
from diagrams.onprem.workflow import Airflow

with Diagram("Report Generation"):

    with Cluster("workers"):
        with Cluster("worker1"):
            worker1 = Docker("Jupyter+Papermill") - EC2("Agent1")
        with Cluster("worker2"):
            worker2 = Docker("Jupyter+Papermill") - EC2("Agent2")
        with Cluster("worker3"):
            worker3 = Docker("Jupyter+Papermill") - EC2("Agent3")

    workers = [worker1, worker2, worker3]

    Airflow("Airflow") >> Edge(
        label="Schedule notebook execution") >> Batch("AWS Batch") >> workers >> SimpleStorageServiceS3("S3") >> Edge(
        label="Commuter") >> Users("End users")

    Users("Data analysts") >> EC2("Adhoc workstation") >> Edge(
        label="Mount") >> EFS("EFS") >> Edge(label="Commuter") >> Users("End users")
