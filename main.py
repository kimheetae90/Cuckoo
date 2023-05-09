import asyncio
from ExecuteNode import EmptyNode
from NodeManager import NodeManager
from OpenChromeNode import OpenChromeNode

async def main():
    start_node = EmptyNode()
    finish_node = EmptyNode()

    openChromeNode = OpenChromeNode()
    start_node.add_next_node(openChromeNode)
    openChromeNode.add_next_node(finish_node)

    node_manager = NodeManager(start_node, finish_node)
    await node_manager.run()

if __name__ == "__main__":
    asyncio.run(main())