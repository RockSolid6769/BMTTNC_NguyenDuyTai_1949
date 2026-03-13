class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix = []
        seen = set()

        for char in key:
            if char not in seen and char in alphabet:
                seen.add(char)
                matrix.append(char)

        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        playfair_matrix = []
        for i in range(0, 25, 5):
            playfair_matrix.append(matrix[i:i+5])

        return playfair_matrix


    def prepare_text(self, text):
        text = text.upper().replace("J", "I")
        text = text.replace(" ", "")

        pairs = []
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 < len(text):
                b = text[i+1]

                if a == b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1

        return pairs


    def find_letter_coords(self, matrix, letter):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c


    def playfair_encrypt(self, plain_text, matrix):

        pairs = self.prepare_text(plain_text)
        encrypted = ""

        for pair in pairs:
            a, b = pair[0], pair[1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                encrypted += matrix[r1][(c1 + 1) % 5]
                encrypted += matrix[r2][(c2 + 1) % 5]

            elif c1 == c2:
                encrypted += matrix[(r1 + 1) % 5][c1]
                encrypted += matrix[(r2 + 1) % 5][c2]

            else:
                encrypted += matrix[r1][c2]
                encrypted += matrix[r2][c1]

        return encrypted


    def playfair_decrypt(self, cipher_text, matrix):

        cipher_text = cipher_text.upper()
        decrypted = ""

        for i in range(0, len(cipher_text), 2):

            a = cipher_text[i]
            b = cipher_text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                decrypted += matrix[r1][(c1 - 1) % 5]
                decrypted += matrix[r2][(c2 - 1) % 5]

            elif c1 == c2:
                decrypted += matrix[(r1 - 1) % 5][c1]
                decrypted += matrix[(r2 - 1) % 5][c2]

            else:
                decrypted += matrix[r1][c2]
                decrypted += matrix[r2][c1]

        return decrypted