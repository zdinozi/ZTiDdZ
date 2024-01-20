import base64
def encodeBase64(String):
    string_bytes = String.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')
    return base64_string
string = input()
print(encodeBase64(string))