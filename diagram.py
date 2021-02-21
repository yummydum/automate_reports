from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2, ECR, Batch
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.onprem.client import Users
from diagrams.onprem.container import Docker
from diagrams.onprem.workflow import Airflow

with Diagram("Report Generation"):

    with Cluster("workers"):
        with Cluster("worker1"):
            worker1 = Docker("Jupyter+Papermill") - EC2("EC2 instance")
        with Cluster("worker2"):
            worker2 = Docker("Jupyter+Papermill") - EC2("EC2instance")
        with Cluster("worker3"):
            worker3 = Docker("Jupyter+Papermill") - EC2("EC2instance")

    workers = [worker1, worker2, worker3]

    Batch("AWS Batch") >> workers >> SimpleStorageServiceS3("S3") >> Edge(
        label="Static Hosting") >> Users("Data analysts")
