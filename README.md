# pySOCKS5-async
Easily extensible async SOCKS5 server.

Requirement: Python 3.5+

    pip install pySOCKS5-async

### Run from cmdline
    python3 -m pysocks5_async.pysocks5 8080

### Use in code:
```python
from pysocks5_async import SOCKS5Server, SimpleSOCKS5Handler

socks5d = SOCKS5Server('localhost', 8080, SimpleSOCKS5Handler)
await socks5d.start_server()
```

### Extend
```python
from pysocks5_async import SOCKS5Server, BaseSOCKS5Handler, SOCKS5Status

class MyHandler(BaseSOCKS5Handler):
    async def do_TCP_open(self):
        print(f'{self.client_host}:{self.client_port}
               request TCP open to {self.dest_host}:{self.dest_port}')
        print(f'dest_host has string representation {self.dest_host_str()}')
        self.response_status(SOCKS5Status.OK)
        content = await self.client_reader.read(10)
        self.client_writer.write(content)
        pass

    async def do_TCP_bind(self):
        self.response_status(SOCKS5Status.GENERAL_FAILURE)
        self.close()

    async def do_UDP_assoc(self):
        self.response_status(SOCKS5Status.CONN_REFUSED)
        self.close()


socks5d = SOCKS5Server('localhost', 8080, MyHandler)
await socks5d.start_server()
```
