def split_file(input_file, chunk_size, output_prefix):
    with open(input_file, 'rb') as file:
        data = file.read()
        total_chunks = (len(data) + chunk_size - 1) // chunk_size

        for i in range(total_chunks):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            chunk_data = data[start:end]

            output_file = f"{output_prefix}_part_{i + 1}.bin"
            with open(output_file, 'wb') as output:
                output.write(chunk_data)

if __name__ == "__main__":
    input_file = input("Masukkan nama file yang ingin dipisahkan: ")
    chunk_size = int(input("Masukkan ukuran setiap bagian (dalam byte): "))
    output_prefix = input("Masukkan awalan nama file keluaran: ")

    split_file(input_file, chunk_size, output_prefix)
    print("Pemisahan file selesai.")
