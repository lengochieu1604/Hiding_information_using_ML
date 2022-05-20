from Crypto.Hash import SHA384
 
text = 'Hello'
hashObject = SHA384.new()
hashObject.update(text.encode('utf-8'))
digest = hashObject.hexdigest()
 
print(digest)