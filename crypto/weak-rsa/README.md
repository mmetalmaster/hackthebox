# Crypto Challenge: Weak RSA (20 Points)

**Can you decrypt the message and get the flag?**

The challenge gave us two files, `key.pub` and `flag.enc`.

Let's check the content of each file.

```
$ cat key.pub
-----BEGIN PUBLIC KEY-----
MIIBHzANBgkqhkiG9w0BAQEFAAOCAQwAMIIBBwKBgQMwO3kPsUnaNAbUlaubn7ip
4pNEXjvUOxjvLwUhtybr6Ng4undLtSQPCPf7ygoUKh1KYeqXMpTmhKjRos3xioTy
23CZuOl3WIsLiRKSVYyqBc9d8rxjNMXuUIOiNO38ealcR4p44zfHI66INPuKmTG3
RQP/6p5hv1PYcWmErEeDewKBgGEXxgRIsTlFGrW2C2JXoSvakMCWD60eAH0W2PpD
qlqqOFD8JA5UFK0roQkOjhLWSVu8c6DLpWJQQlXHPqP702qIg/gx2o0bm4EzrCEJ
4gYo6Ax+U7q6TOWhQpiBHnC0ojE8kUoqMhfALpUaruTJ6zmj8IA1e1M6bMqVF8sr
lb/N
-----END PUBLIC KEY-----
```

```
$ cat flag.enc
?_?vc[??~?kZ?1?Ĩ?4?I?9V?ֿ?^G???(?+3Lu"?T$???F0?VP?־j@?????|j?????{¾?,?????YE?????Xx??,??c?N&Hl2?Ӎ??[o??
```

We have the public key and the encrypted text but we need to know the private key for us to decrypt the ciphertext. So I searched on GitHub for a tool that could possible decrypt this RSA challenge and I found this repository:
https://github.com/Ganapati/RsaCtfTool

RsaCtfTool is a tool that uncipher data from weak public key and try to recover private key Automatic selection of best attack for the given public key.

Now to decrypt the the ciphertext, I executed the command below and finally got the flag.

```
$ python RsaCtfTool.py --publickey key.pub --uncipherfile  flag.enc
[+] Clear text : HTB{s1mpl3_Wi3n3rs_4tt4ck}
```
