
def convert(s):
    if not isinstance(s, bytes): return 0

    ret = ''
    for ch in s:
        if ord('a') <= ch <= ord('z'):
            ret += chr(219-ch)

        else: ret += chr(ch)

    return ret

print(convert(b'aBcD'))
