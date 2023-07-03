import sys
from Crypto.Util import number

def decrypt_data(encoded_data, d, n):
    decrypted_data = []

    for chunk in encoded_data:
        decrypted_chunk = pow(chunk, d, n)  # Calculate the decrypted chunk
        chunk_bytes = decrypted_chunk.to_bytes((decrypted_chunk.bit_length() + 7) // 8, 'big')
        chunk_str = chunk_bytes.decode()
        decrypted_data.append(chunk_str)

    return decrypted_data

def main():
    if len(sys.argv) != 4:
        print("Usage: python decripta.py <private_key_file> <input_file> <output_file>")
        return

    private_key_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(private_key_file, 'r') as file:
        d, n = map(int, file.read().strip().split('\n'))

    with open(input_file, 'r') as file:
        encoded_data = [int(line.strip()) for line in file]

    decrypted_data = decrypt_data(encoded_data, d, n)

    with open(output_file, 'w') as file:
        file.write(''.join(decrypted_data))

    print("Data decrypted successfully!")

if __name__ == '__main__':
    main()