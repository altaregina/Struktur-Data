def merge_files(input_prefix, output_file):
    data = bytearray()

    i = 1
    while True:
        input_file = f"{input_prefix}_part_{i}.bin"
        try:
            with open(input_file, 'rb') as file:
                chunk_data = file.read()
                if not chunk_data:
                    break
                data.extend(chunk_data)
        except FileNotFoundError:
            break
        i += 1

    with open(output_file, 'wb') as output:
        output.write(data)

if __name__ == "__main__":
    input_prefix = input("Masukkan awalan nama file yang ingin digabungkan: ")
    output_file = input("Masukkan nama file keluaran setelah penggabungan: ")

    merge_files(input_prefix, output_file)
    print("Penggabungan file selesai.")
