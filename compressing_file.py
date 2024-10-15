# import lzma

## Good at speed and also good at compress it not have internal compresslevel deciding function
# with open("9286297.jpg", "rb") as f_in, lzma.open("9286297c.xz", "wb") as f_out:
#     f_out.write(f_in.read())


# with lzma.open("9286297c.xz", "rb") as f_in, open("9286297cun.jpg", "wb") as f_out:
#     f_out.write(f_in.read())


## Not good at speed but good at compresslevel as i set commpresslevel(1-9) high(9) and it perform as expected
# import bz2

# with open("9286297.jpg", "rb") as f_in, bz2.open("9286297c.xz", "wb", compresslevel=9) as f_out:
#     f_out.write(f_in.read())


# with bz2.open("9286297c.xz", "rb") as f_in, open("9286297cun.jpg", "wb") as f_out:
#     f_out.write(f_in.read())


# Best at speed but not good at compresslevel because i set commpresslevel(1-9) high(9) but it perform as expected
import gzip

with open("9286297.jpg", "rb") as f_in, gzip.open("9286297c.xz", "wb", compresslevel=9) as f_out:
    f_out.write(f_in.read())


with gzip.open("9286297c.xz", "rb") as f_in, open("9286297cun.jpg", "wb") as f_out:
    f_out.write(f_in.read())