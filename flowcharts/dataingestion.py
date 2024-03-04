from diagrams import Diagram, Cluster
from diagrams.aws.storage import S3
from diagrams.onprem.database import MongoDB
from diagrams.custom import Custom

with Diagram("Excel File Storage Architecture", show=False):
    with Cluster("Data Ingestion"):
        excel_file = Custom("Excel File", "./Data Ingestion.png")

    with Cluster("Database"):
        mongodb = MongoDB("MongoDB")

    with Cluster("File Storage"):
        s3 = S3("AWS S3")

    excel_file >> mongodb
    excel_file >> s3