from typing import Dict, List
import asyncio
from ValueNode import ValueNode

class ExecuteNode:
    def __init__(self):
        self.inputs: Dict[str, ValueNode] = {}
        self.outputs: Dict[str, ValueNode] = {}
        self.next_nodes: List[ExecuteNode] = []

    def set_input(self, key: str, value_node: ValueNode) -> None:
        self.inputs[key] = value_node

    def set_output(self, key: str, value_node: ValueNode) -> None:
        self.outputs[key] = value_node

    def add_next_node(self, next_node: 'ExecuteNode') -> None:
        self.next_nodes.append(next_node)

    async def execute(self) -> 'ExecuteNode':
        raise NotImplementedError

class EmptyNode(ExecuteNode):
    def __init__(self):
        super().__init__()

    async def execute(self) -> 'ExecuteNode':
        return self.next_nodes[0] if self.next_nodes else None