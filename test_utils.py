import asyncio
import pysocks5
import ipaddress

async def test_udp(server_host, server_port, assoc_host, assoc_port: int):
    reader, writer = await asyncio.open_connection(server_host, server_port)
    print('conn opened')
    writer.write(pysocks5._ACCEPTED_VERSION)
    writer.write(b'\x01')
    writer.write(b'\x00')
    resp = await reader.read(2)
    print(resp)

    writer.write(pysocks5._ACCEPTED_VERSION)
    writer.write(pysocks5._CMD_UDP_ASSOC)
    writer.write(b'\x00')
    writer.write(pysocks5._ADDR_TYPE_IPV4)
    writer.write(ipaddress.IPv4Address(assoc_host).packed)
    writer.write(assoc_port.to_bytes(2, 'big'))
    resp = await reader.read(10)
    print(resp)


async def test_tcp(server_host, server_port, bind_host, bind_port: int):
    reader, writer = await asyncio.open_connection(server_host, server_port)
    print('conn opened')
    writer.write(pysocks5._ACCEPTED_VERSION)
    writer.write(b'\x01')
    writer.write(b'\x00')
    resp = await reader.read(2)
    print(resp)

    writer.write(pysocks5._ACCEPTED_VERSION)
    writer.write(pysocks5._CMD_TCP_BIND)
    writer.write(b'\x00')
    writer.write(pysocks5._ADDR_TYPE_IPV4)
    writer.write(ipaddress.IPv4Address(bind_host).packed)
    writer.write(bind_port.to_bytes(2, 'big'))
    resp = await reader.read(10)
    print(resp)

    resp = await reader.read()
    print(resp)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_tcp('localhost', 8080, '0.0.0.0', 0))
    loop.run_forever()
