
# HTTPSCryptographyAndCertificates

# How Public Private Key Cryptography and Certificates are Used to Communicate Securely Through HTTPS

sj2: Communicating Securely on the Web Using Certificates (HTTPS, TLS, SSL, …)

When you securely visit a website using HTTPS how does your browser know that https://bank.com is really bank.com? After all, a person having access to a router between the two computers could pretend to be bank.com, send you a credible-looking login window and steal your password.

The answer is a combination of public / private key cryptography (PPC) and certificates with a chain of trust.

This article first, gives a brief introduction to PPC and certificates. Then, we show how they are used in conjunction in order to secure the web.

## Public / Private Key Cryptography

~RSA

m’ = encrypt(privateKey, m)
m = decrypt(publicKey, m’)

→ If I have someone’s publicKey, I can verify that an encrypted message comes from that person. It is _impossible_ to generate m’ without knowing publicKey.

AND / OR?

m’’ = encrypt(publicKey, m)
m = decrypt(privateKey, m’’)

→ If I have someone’s publicKey, I can securely send message to that person since once encrypted, the message is only decipherable by someone that has the _associated_ privateKey.

Where generating m’ from m without knowing privateKey is ‘almost-impossibly-hard’.

Utility: people can verify that the author of the message is the owner of the key.

-- difference with symmetric encryption.

https://en.wikipedia.org/wiki/Length_extension_attack
^^ can’t just naively use a hash function.

## Certificates

Let’s define a certificate as a document that contains:

- Name
- Expiry date
- publicKey
- metadata: thumbprint

where: 
thumbprint = encrypt(privateKey, cryptoHash(certificate))

Note that the hashing is not necessary. It is just used so that the thumbprint is much smaller than the certificate. But if you just replace cryptoHash(x) by the identity function (f(x) = x), everything would still work.

? what if someone steals a certificate ?
→ OK since the privateKey never leaks.

**Verifying that a certificate is valid.**

=> comes from the owner of the cert => owner of the publicKey

cryptoHash(certificate) = decrypt(publicKey, thumbprint)

# How Used on the Web

GET https://www.bank.com

me                                                  bank.com
----------[TLS handshake] ----------->
←-------[ certificate ]------------------

Let’s assume a simpler case than internet, then we will show how internet use a derivation of that scheme that is most useful.

Assume that beforehand I met with all the websites in the world, and I have one public key per website. Then I have somewhere: 

archive.org public key = hhsjxx0g203zhldu
bank.com’s public key = lg9nlb2gpsymbtn3
[... a billion lines later …]
zzzzzulu.com’s public key = w17hddda3z27cyuo

## A Much More Elegant Solution (How It Actually Works)

Sequence of trust.


# Open Questions

When get a new certificate, the private key does not change.

Terminology?: salt, key, initialization vector

# See Also

[RSA_Paper]: http://people.csail.mit.edu/rivest/Rsapaper.pdf

https://en.wikipedia.org/wiki/Public_key_certificate

[not read] http://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art012

http://crypto.stackexchange.com/questions/21102/what-is-the-ssl-private-key-file-format/21104#21104

http://crypto.stackexchange.com/questions/2893/how-do-digital-certificates-work-and-why-is-it-not-possible-to-reverse-engineer


# References

[...]

# Appendix
## [move appendix] What Are Hash Functions and What is A Cryptographic Hash Function?

Map a large set to a smaller set.

sha256
md5 is not cool anymore.

Properties of cryptographic hash:

given: m* = hash(m), ‘almost-impossibly-hard’ to generate: m^ such that m* = hash(m^).

This would mean that having the hash does not prove I have m.

Use: 
- reduce size of proofs.
- bittorrent: trust files hosted on untrusted websites: if hash matches what is on the author’s website, it proves that

# [weak] What Does ‘Almost-Impossibly-Hard’ Mean?

Not impossible, since you could just try all m’ in existence with:

m = decrypt(publicKey, m’)

Here is a simple algorithm that can hack:

	try randomly until matches


# Mathematics-Like: Can I Trust That Person?

[in mathematical term, proof that I can trust that person]

~~~~~
