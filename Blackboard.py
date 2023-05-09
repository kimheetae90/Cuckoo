from typing import Any, Dict, Union

class Blackboard:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.data = {}
        return cls.__instance

    def set(self, key: str, value: Any):
        self.data[key] = value

    def get(self, key: str) -> Any:
        return self.data.get(key)
    
blackboard = Blackboard()