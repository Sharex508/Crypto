import requests
import websockets
from wazirx_sapi_client.rest import Client
import asyncio
import time
import json
 
client = Client()
 
#api_key = "test_api_key"
api_key = "1Xdwd3vszGCIqQUrTOX2WPF6txeQg8pPb2Qkl5553XUuqEePJFOS2WDrxdpoFV3W"
#secret_key = "test_secret_key"
secret_key = "5pG94NHjWycxA5ljZ2oNYcX08utpUT7xJothuNjd"
#client = Client(api_key=api_key, secret_key=secret_key)
 
from wazirx_sapi_client.websocket import WebsocketClient


async def main():
    """
    For public streams, api_key,secret_key is not required i.e.
        ws_client = WebsocketClient()
    For private streams, api_key, secret_key are required while initialising WebsocketClient i.e.
        ws_client = WebsocketClient(api_key=api_key, secret_key=secret_key)
    """
    # Keys for private events
    api_key = "1Xdwd3vszGCIqQUrTOX2WPF6txeQg8pPb2Qkl5553XUuqEePJFOS2WDrxdpoFV3W"
    secret_key = "5pG94NHjWycxA5ljZ2oNYcX08utpUT7xJothuNjd"

    ws_client = WebsocketClient(api_key=api_key, secret_key=secret_key)

    asyncio.create_task(
        ws_client.connect(
        )
    )

    await ws_client.subscribe(
        events=["outboundAccountPosition"],
        id=2  # id param not mandatory
    )
    # await ws_client.unsubscribe(
    #     events=["outboundAccountPosition", "wrxinr@depth"],
    # )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
