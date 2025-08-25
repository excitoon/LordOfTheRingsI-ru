def decode(data: bytes, indices: bytes) -> list[bytes]:
    lengths = [int.from_bytes(indices[i:i+2], 'little') for i in range(0, len(indices), 2)]

    chunks = []
    offset = 0
    for length in lengths:
        chunk = data[offset:offset+length]
        chunks.append(chunk)
        offset += length

    assert offset == len(data), f"Warning: {len(data) - offset} bytes unused in data"

    return chunks
