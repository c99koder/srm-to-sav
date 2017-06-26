# srm-to-sav
Convert RetroArch SRM files to raw GBA SAV files and vice versa

# Usage

```
sav-to-srm.py -i <input.sav> -o <output.srm> [--byteswap]
```

# Byte Swapping

Some games, such as The Legend of Zelda - The Minish Cap write their save data backwards in RetroArch.  Use the `--byteswap` argument to write the data in the correct order.