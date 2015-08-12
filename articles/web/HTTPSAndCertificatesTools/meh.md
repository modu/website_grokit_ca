
## [Save This as Last Resort, More Complicated. Does not Generate Public Key Either] Generate Certificate in .CRT and .PFX Form

(Adapted from http://stackoverflow.com/questions/20445365/create-pkcs12-file-with-self-signed-certificate-via-openssl-in-windows-for-my-a)

.pfx is for windows and is password protected.

openssl genrsa -out private_key.key 2048
openssl req -new -key private_key.key -out cert_sign_request.csr -config openssl.cnf
openssl x509 -req -days 3650 -in cert_sign_request.csr -signkey private_key.key -out certificate.crt
openssl pkcs12 -keypbe PBE-SHA1-3DES -certpbe PBE-SHA1-3DES -export -in certificate.crt -inkey private_key.key -out certificate.pfx -name "certName"

Note: openssl.cnf will be somewhere in your SSH distribution.

