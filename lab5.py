import requests

url = "https://aes.cryptohack.org/flipping_cookie/"

r = requests.get(f"{url}get_cookie/")
cookie = r.json()["cookie"]

print(cookie)
iv = cookie[0:32]
print(iv)
iv = bytes.fromhex(iv)

o = b"admin=False;"
w = b"admin=True;;"
t = bytes(iv[i] ^ o[i] for i in range(len(o)))
niv = bytes(t[i] ^ w[i] for i in range(len(t)))
niv += iv[len(t):]
ncookie = cookie[32:]
r = requests.get(f"{url}check_admin/{ncookie}/{niv.hex()}")
print(r.text)