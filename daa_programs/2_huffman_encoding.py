"""
Assignment 2: Huffman Encoding using a greedy strategy.

Greedy choice: always merge the two nodes with the lowest frequency.
Time complexity : O(n log n)  (n = number of distinct characters)
Space complexity: O(n)
"""
import heapq
from collections import Counter


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right


def build_tree(text):
    freq = Counter(text)
    # (frequency, tie-breaker, node) - the tie-breaker keeps heapq from
    # comparing Node objects when frequencies are equal.
    heap = [(f, i, Node(f, ch)) for i, (ch, f) in enumerate(sorted(freq.items()))]
    heapq.heapify(heap)
    counter = len(heap)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)    # smallest
        f2, _, right = heapq.heappop(heap)   # second smallest
        heapq.heappush(heap, (f1 + f2, counter, Node(f1 + f2, None, left, right)))
        counter += 1

    return heap[0][2], freq


def generate_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node.char is not None:            # leaf
        codes[node.char] = prefix or "0"  # single distinct character case
    else:
        generate_codes(node.left, prefix + "0", codes)
        generate_codes(node.right, prefix + "1", codes)
    return codes


def decode(encoded, root):
    if root.char is not None:            # only one distinct character
        return root.char * len(encoded)
    result, node = [], root
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)


def main():
    text = input("Enter text to encode: ")
    if not text:
        print("Empty input")
        return

    root, freq = build_tree(text)
    codes = generate_codes(root)

    print(f"\n{'Char':<8}{'Freq':<8}Code")
    for ch in sorted(codes, key=lambda c: (len(codes[c]), c)):
        print(f"{repr(ch):<8}{freq[ch]:<8}{codes[ch]}")

    encoded = "".join(codes[ch] for ch in text)
    print("\nEncoded :", encoded)
    print("Decoded :", decode(encoded, root))

    original_bits = len(text) * 8
    print(f"\nOriginal size  : {original_bits} bits (8 bits per char)")
    print(f"Encoded size   : {len(encoded)} bits")
    print(f"Space saved    : {100 * (1 - len(encoded) / original_bits):.2f} %")


if __name__ == "__main__":
    main()
