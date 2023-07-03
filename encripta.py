import sys
from Crypto.Util import number

def encrypt_data(data, e, n):
    encoded_data = []
    chunk_size = number.size(n) 

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        chunk_int = int.from_bytes(chunk.encode(), 'big')
        encoded_chunk = pow(chunk_int, e, n)  
        encoded_data.append(encoded_chunk)

    return encoded_data

def main():
    if len(sys.argv) != 4:
        print("Usage: python encripta.py <public_key_file> <input_file> <output_file>")
        return

    public_key_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(public_key_file, 'r') as file:
        e, n = map(int, file.read().strip().split('\n'))

    with open(input_file, 'r') as file:
        data = file.read().strip()
        data_encoded = data.encode().hex()

    encrypted_data = encrypt_data(data_encoded, e, n)

    with open(output_file, 'w') as file:
        file.write('\n'.join(map(str, encrypted_data)))

    print("Data encrypted successfully!")

if __name__ == '__main__':
    main()
