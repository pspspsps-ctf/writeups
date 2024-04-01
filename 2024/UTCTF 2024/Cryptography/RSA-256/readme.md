# RSA-256

> Based on the military-grade encryption offered by AES-256, RSA-256 will usher in a new era of cutting-edge security... or at least, better security than RSA-128.
> 
> By Jeriah (@jyu on discord)

Solution:

We are given with a text file: `vals.txt`

```
N = 77483692467084448965814418730866278616923517800664484047176015901835675610073
e = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321
```

Since we have `N`, let's use http://factordb.com/ to get its prime factors

```
p = 1025252665848145091840062845209085931
q = 75575216771551332467177108987001026743883
```

Great! Now to decrpypt the ciphertext `c`, we need to compute `φ(N)` first.

In RSA, `N` is the product of two prime numbers, `p` and `q`. The function `φ(N)`, known as Euler's totient function, is defined as the number of positive integers less than `N` that are relatively prime to `N`. For a prime number `p`, `φ(p)` is simply `p - 1`, because all numbers less than a prime are relatively prime to it.

When `N` is the product of two distinct prime numbers `p` and `q`, the value of `φ(N)` is given by:

```
φ(N) = φ(p) * φ(q) = (p - 1) * (q - 1)
```

This formula is used because the numbers that are not relatively prime to `N` are exactly those that are multiples of `p` or `q`, and there are `(p - 1)` multiples of `q` and `(q - 1)` multiples of `p` that are less than `N`.

With that said, we will be using:

```
phi = (p - 1) * (q - 1)
```

Next, we need to compue the private exponent `d`. 

The public exponent `e` and the private exponent `d` are multiplicative inverses modulo `φ(N)`. This means that their product, when divided by `φ(N)`, leaves a remainder of 1:

```
(e * d) % φ(N) = 1
```

The value of `d` can be found using the Extended Euclidean Algorithm, which is a way to find the modular multiplicative inverse of `e` modulo `φ(N)`. In practical terms, `d` is the decryption key that allows the holder to decrypt messages that were encrypted with the public key `(N, e)`.

Using Python, we can do:

```python
from Crypto.Util.number import inverse

d = inverse(e, phi)
```

Lastly, we decrypt the ciphertext `c`. 

Since we have the private exponent `d`, we can decrypt the ciphertext `c` by raising it to the power of `d` modulo `N`:

```
m = c^d mod N
```

This operation reverses the encryption process, which involved raising the plaintext message `m` to the power of e modulo `N`. The reason this works is due to the properties of modular arithmetic and the way `e` and `d` are chosen. The result `m` is the original plaintext message that was encrypted.

The full Python script is:

```python
from Crypto.Util.number import inverse

# Given values
N = 77483692467084448965814418730866278616923517800664484047176015901835675610073
e = 65537
c = 43711206624343807006656378470987868686365943634542525258065694164173101323321

# Prime factors of N
# http://factordb.com/index.php?query=77483692467084448965814418730866278616923517800664484047176015901835675610073
p = 1025252665848145091840062845209085931
q = 75575216771551332467177108987001026743883

# Compute φ(N)
phi = (p - 1) * (q - 1)

# Compute the private exponent d
d = inverse(e, phi)

# Decrypt the ciphertext c
m = pow(c, d, N)

# Convert the plaintext message m to bytes
messageBytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')

# Decode the bytes to a string (assuming UTF-8 encoding)
message = messageBytes.decode('utf-8')

print("Decrypted message:", message)
```

Flag: `utflag{just_send_plaintext}`