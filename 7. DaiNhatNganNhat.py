
def tu_dai_nhat(s):
    ds = s.split()
    dai_nhat = ds[0]
    for tu in ds:
        if len(tu) > len(dai_nhat):
            dai_nhat = tu
    return dai_nhat

def tu_ngan_nhat(s):
    ds = s.split()
    ngan_nhat = ds[0]
    for tu in ds:
        if len(tu) < len(ngan_nhat):
            ngan_nhat = tu
    return ngan_nhat
if __name__ == "__main__":
    print(tu_dai_nhat("short long longest"))   # longest
    print(tu_ngan_nhat("short long longest"))  # short

