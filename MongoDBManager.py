import requests
import json

class MongoDBManager:
    
    def __init__(self):
        """
        Initializes a MongoDBManager object.

        Parameters:
        None

        Returns:
        None
        """
        self.url = "https://us-east-1.aws.data.mongodb-api.com/app/data-ungvu/endpoint/data/v1/action"
        self.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': "lOkN1jaeeVuyff56UPtVY5iqMB8lcSv5jdLdQVXCifSJs8e06zdvdHGxyQCDlkn0",
        }
        self.collection_name = "<COLLECTION_NAME>"
        self.database_name = "<DATABASE_NAME>"
        self.data_source = "Cluster0"

    def write(self, data):
        """
        Writes the specified data to the MongoDB collection.

        Args:
            data: The data to be written.

        Returns:
            The JSON response from the MongoDB server.
        """
        payload = json.dumps({
            "collection": self.collection_name,
            "database": self.database_name,
            "dataSource": self.data_source,
            "filter": {"_id": {"$oid": "65655325e4b7353a268caf89"}},
            "replacement": data  # This replaces the entire document
        })
        response = requests.request("POST", self.url + "/replaceOne", headers=self.headers, data=payload)
        return response.json()

    def read(self):
            """
            Read a specific document from the collection using its insertedId.

            Returns:
                dict: The document retrieved from the collection.
            """
            payload = json.dumps({
                "collection": self.collection_name,
                "database": self.database_name,
                "dataSource": self.data_source,
                "filter": {"_id": {"$oid": "65655325e4b7353a268caf89"}}
            })
            response = requests.request("POST", self.url + "/findOne", headers=self.headers, data=payload)
            document = response.json()['document']
            document.pop('_id')
            return document
