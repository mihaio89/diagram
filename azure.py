import os

from diagrams import Diagram, Edge

from diagrams.azure.integration import LogicApps, ServiceBus
from diagrams.azure.database import CosmosDb

path = os.path.join("images", "integration")

with Diagram(filename=path, show=False, outformat="png"):
    service_bus = ServiceBus("Service Bus")
    logic_app = LogicApps("Logic App")
    cosmos_db = CosmosDb("Cosmos DB")

    cosmos_db >> Edge() >> logic_app >> Edge() >> service_bus