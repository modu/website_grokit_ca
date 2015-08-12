
# HTTPS And Certificates Tools

This is not really an article but a dump of different tools and commands that are useful when dealing with HTTPS and certificates.

# OpenSSL Commands

## Dump Private Key + Public Certificate from Password Protected .pfx File

openssl pkcs12 -in certificate.pfx -nodes
(You will be prompted for password.)

## Dump Private Key Only to File from Password Protected .pfx File

openssl pkcs12 -in certificate.pfx -nocerts -out privateKey.pem -nodes

## Dump Certificate and Public Key from Password Protected .pfx File

openssl pkcs12 -in yourP12File.pfx -clcerts -nokeys -out publicCert.pem
openssl x509 -pubkey -noout -in publicCert.pem

## Generate Cert (another way)

openssl genrsa 2048 > private.pem
openssl req -x509 -new -key private.pem -out public.pem
openssl pkcs12 -export -in public.pem -inkey private.pem -out mycert.pfx

Note: .pem files are same as .cer files.

# Check Certificate Served by HTTPS Server

## Simple CURL Command

		curl https://www.yahoo.com -v -k --trace-ascii https_trace.txt

Amongst other things, you get certificate info:

		== Info: SSLv3, TLS handshake, Finished (20):
		<= Recv SSL data, 16 bytes (0x10)
		0000: .........i..UC$.
		== Info: SSL connection using ECDHE-RSA-AES128-GCM-SHA256
		== Info: Server certificate:
		== Info:		 subject: C=US; ST=California; L=Sunnyvale; O=Yahoo Inc.; OU=Information Technology; CN=www.yahoo.com
		== Info:		 start date: 2015-06-26 00:00:00 GMT
		== Info:		 expire date: 2015-12-30 23:59:59 GMT
		== Info:		 issuer: C=US; O=VeriSign, Inc.; OU=VeriSign Trust Network; OU=Terms of use at https://www.verisign.com/rpa (c)10; CN=VeriSign Class 3 Secure Server CA - G3
		== Info:		 SSL certificate verify ok.

## C# Code That Juices HTTPS Server Certificate Info

		private static bool ValidateServerCertficate(
						object sender,
						X509Certificate cert,
						X509Chain chain,
						SslPolicyErrors sslPolicyErrors)
		{
			System.Console.WriteLine(cert.GetCertHashString());
			return true;
		}

		static void Main(string[] args)
		{
			HttpClient httpClient = new HttpClient();
			ServicePointManager.ServerCertificateValidationCallback = ValidateServerCertficate;
			HttpRequestMessage http = new HttpRequestMessage(HttpMethod.Get, "https://www.yahoo.com");
			httpClient.SendAsync(http).Wait();
		}
