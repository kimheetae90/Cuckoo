import asyncio
from ExecuteNode import ExecuteNode

class NodeManager:
    def __init__(self, start_node: ExecuteNode, finish_node: ExecuteNode):
        self.start_node = start_node
        self.finish_node = finish_node

    async def run(self) -> None:
        print("Start!")
        current_node = self.start_node
        while current_node != self.finish_node:
            next_node = await current_node.execute()
            if not next_node:
                break
            current_node = next_node
        print("Finish!")