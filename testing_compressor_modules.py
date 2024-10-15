import time
import lzma
import gzip
import bz2


def time_taking_to_compress(compressing, data):
    start = time.time()
    length_of_data, name_of_module = compressing(data)
    print(f"Compressed {len(data)} bytes into {len(length_of_data)} by {name_of_module} module.")
    end = time.time()

    return end-start

def compress_data_by_lzma(data):
    compress_data = lzma.compress(data)
    return compress_data, "lzma"

def compress_data_by_gzip(data):
    # compress_data = gzip.compress(data)
    compress_data = gzip.compress(data, compresslevel=9) # compresslevel=(1-9)
    return compress_data, "gzip"

def compress_data_by_bz2(data):
    # compress_data = bz2.compress(data)
    compress_data = bz2.compress(data, compresslevel=9) # compresslevel=(1-9)
    return compress_data, "bz2"


data = b'This testing data' * 99999999

print("Original data size: ", len(data))


print(f"Time of taking by lzma module to compress data of {len(data)} bytes: {time_taking_to_compress(compress_data_by_lzma, data)}")
print(f"Time of taking by gzip module to compress data of {len(data)} bytes: {time_taking_to_compress(compress_data_by_gzip, data)}")
print(f"Time of taking by bz2 module to compress data of {len(data)} bytes: {time_taking_to_compress(compress_data_by_bz2, data)}")