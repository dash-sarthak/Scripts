import json


class JsonReader:
    """Reads json files"""

    def __init__(self, location: str) -> None:
        self.location = location

    def return_json(self) -> dict:
        """Returns a dict from json file

        Returns:
            dict: dict containing json data
        """
        with open(self.location, encoding="utf-8") as json_file:
            data = json.load(json_file)

        return data
