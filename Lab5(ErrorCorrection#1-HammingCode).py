def chunks(l, n):
    """Розділяє послідовність `l` на невеликі фрагменти розміром `n` і генерує їх послідовно."""
    for i in range(0, len(l), n):
        yield l[i: i + n]  # Повертає фрагмент послідовності.

def encode(text: str) -> str:
    """Кодує вхідний рядок `text` у рядок бітів."""
    return ''.join(
        ''.join(b * 3 for b in f"{ord(c):08b}")  # Потроєння бітів
        for c in text
    )

def decode(bits: str) -> str:
    """Декодує рядок бітів у текст."""
    bit_items = []
    for tripled_bits in chunks(bits, 3):
        sums = sum(map(int, tripled_bits))

        # Приклад: 110 або 111 -> 1 і 000 -> 0 або 001 -> 0
        bit_items.append('1' if sums == 2 or sums == 3 else '0')

    binary = ''.join(bit_items)

    items = []
    for byte in chunks(binary, 8):
        items.append(chr(int(byte, 2)))

    return ''.join(items)
