def find_packet(stream, length: int) -> int:
    for i in range(len(stream)):
        packet = set()
        for x in range(length):
            packet.add(stream[i+x])
        if len(packet) == length:
            return i + length


with open("input.txt") as file:
    stream = file.read()


print(find_packet(stream, 4))
print(find_packet(stream, 14))
