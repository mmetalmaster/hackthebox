# Stego Challenge: Raining Blood (40 Points)

**Can you find the hidden message?**

The author of this challenge gave us an MP3 file.

```
$ file RainingBlood.mp3 
RainingBlood.mp3: Audio file with ID3 version 2.3.0, contains:MPEG ADTS, layer III, v1, 320 kbps, 44.1 kHz, JntStereo
```

Let's check the content of the file using `strings` command and use `awk` command to filter the result.

```
$ strings RainingBlood.mp3 | awk 'length($0) > 20 && length($0) < 80'
!22222222222222222222222222222222222222222222222222
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
!#'),.1368;=@BEGJMORTWY\^acfhknqsvx{}
f<SFRCe2gxZGQxbmdfZDR0NF9iM3R3MzNuX21wM19mcjRtM3NfaXNfbm90X2Z1bm55ISF9Cg==
5LAME3.99.5UUUUUUUUUB
CrULAME3.99.5UUUUUUUUUUUUUUU
LAME3.99.5UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
LAME3.99.5UUUUUUUUUUUUUUUUUUU
```

And we got a BASE64. Let's decode it and get the flag:

```
$ echo "SFRCe2gxZGQxbmdfZDR0NF9iM3R3MzNuX21wM19mcjRtM3NfaXNfbm90X2Z1bm55ISF9Cg==" | base64 --decode
HTB{h1dd1ng_d4t4_b3tw33n_mp3_fr4m3s_is_not_funny!!}
```
