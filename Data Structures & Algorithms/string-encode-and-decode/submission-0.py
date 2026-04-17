class Solution:

    def encode(self, words: List[str]) -> str:
        pieces = []

        for word in words:
            size = len(word)
            pieces.append(f"{size}:{word}")

        return "".join(pieces)

    def decode(self, data: str) -> List[str]:
        result = []
        pos = 0

        while pos < len(data):
            split = pos

            while data[split] != ":":
                split += 1

            word_length = int(data[pos:split])
            start = split + 1
            end = start + word_length

            result.append(data[start:end])
            pos = end

        return result