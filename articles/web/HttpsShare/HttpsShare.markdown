
# Https Share

This script allows you to securely share files over HTTPS. (You can get the [full source on GitHub](https://github.com/nothing1212/https_share)).

You simply start the script using the following:

    python3 https_share.py -a magic-access-token_fj9efd3c -p 4443

Now, you need the magic token in order to access the files. If you access the https URL without setting the magic token first, you will get a '401 Unauthorized'.

![HttpsShare](../../static/https_share_sshot_token_input.png)

You can set the token in the UI and click submit, or just send friends a link to the '/set_token/' URL:

    https://ip_of_server:4443/set_token/magic-access-token_fj9efd3c

Obviously replace the magic token by the same one you used when starting the application. This token will be saved as a cookie and now you can now access the files!

The use-case for this script is to share files between computers without risking having someone unauthorized getting access. It uses TLS so all the traffic will be encrypted.

![HttpsShare](../../static/https_share_sshot.png)

There is also support for in-browser upload:

![HttpsShare](../../static/https_share_sshot_upload.png)

## How It Works

The access model is very simple. It simply maps the /set_cookie/.* regex-url to a function which asks the browser to set the cookie to the content of the url.

        if re.search('^/set_cookie/.*', self.path):
            handleSetToken(self)
            return

 The function then set the cookie through the browser:

        def handleSetToken(httpHanlder):

            tokenV = httpHanlder.path.split("/")[-1]

            httpHanlder.send_response(200)
            httpHanlder.send_header('Content-type','text/html')
            httpHanlder.send_header('Set-Cookie', 'accessToken=%s;Path=/; HttpOnly' % tokenV)
            httpHanlder.end_headers()

            httpHanlder.wfile.write(html.encode())

You can now access any resource given that the browser returns the magic cookie:

        def isAuthorized(httpHanlder):
                tokenV = ''
                cookies = httpHanlder.headers.get('Cookie')
                if cookies:
                    tokenV = cookies.split('accessToken=')[1]

                if tokenV == httpHanlder.server.data['access_token']:
                    return True

                return False

Downloading a file through HTTPS is trivial when using the python base class. You first map URLs to functions:

        def functorFromUrl(url):

            hDict = {}
            hDict[r'^/$'] = handleMain
            hDict[r'^/files/.*'] = handleUrlListFiles

            for k, v in hDict.items():
                if re.search(k, url):
                    return v

            return None

... and then in 'handleUrlListFiles' you just read and return the files:

def handleUrlListFiles(httpHanlder):

        [...]

        elif os.path.isfile(queryPath):

            filename = os.path.split(queryPath)[1]

            httpHanlder.send_response(200)
            httpHanlder.send_header('Content-disposition','attachment; filename=%s' % filename)
            httpHanlder.end_headers()

            fh = open(queryPath, 'rb')
            fileBytes = fh.read()
            fh.close()

            httpHanlder.wfile.write(fileBytes)

        else:
            handleNotFound(httpHanlder)

The "httpHanlder.send_header('Content-disposition','attachment; filename=%s' % filename)" line just tells your browser that the resource is a file so that it starts a download dialog.

## Open Issue(s)

- When serving a large file, there is no buffer concept... the file is loaded in memory in its entirety. Obviously, buffering would be better.

- Never checked if checksum matches for large files upload. Would be good to do since chunking logic is non-trivial.
