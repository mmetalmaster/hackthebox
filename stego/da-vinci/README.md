# Stego Challenge: Da Vinci (30 Points)

**Try to find out the secret which is hiding inside of these pictures and learn the truth about Mona Lisa!**

The author gave us three pictures.

**monalisa.jpg**<br>
<img src="monalisa.jpg">

**Plans.jpg**<br>
<img src="Plans.jpg">

**Thepassword_is_the_small_name_of_the_actor_named_Hanks.jpg**<br>
<img src="Thepassword_is_the_small_name_of_the_actor_named_Hanks.jpg">

Let's see if there's something in these images using `strings` command.

```
$ strings monalisa.jpg | awk 'length($0) > 10'
;CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 92
5Optimized by JPEGmini 3.9.20.0L Internal 0x8c97c7da
))))))))))))))))))))))))))))))))))))))))))))))))))
EK:p%q%FvR\e
 d'v[{EmXx1
T\c!`.w0x-B ].
dk*bbJB[>X[e
O:V=v,Tee3n-7Y
EbqL%g>@Dq$
z#iWV(mO)~PL
c<[;pg],s{p
NbfVh1Y~v":>
k^*kTJ$2LT^BC
6Yw6L<7(^]i
T::Ks\"c'e8
famous.zipUT
ia
  \2nA{D9x
FayU)W^[Ja=
famous.zipUT
```

Ohh.. a zip file, will try to use binwalk later to properly check that image.

```
$ strings Thepassword_is_the_small_name_of_the_actor_named_Hanks.jpg | awk 'length($0) > 10'
""""""""""""""""""""""""""""""""""""""""""""""""""
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
```

Okay.. Nothing Interesting here..

```
$ strings Plans.jpg | awk 'length($0) > 10'
//33//@@@@@@@@@@@@@@@
#0+.'''.+550055@@?@@@@@@@@@@@@
?:Vn.$R0!B@X2
rLXn0~uHg*T
zX^(1*cxY3:
RN;m@.
      VebJ
https://www.youtube.com/watch?v=jc1Nfx4c5LQ
```

Wait.. what?! A YouTube Link? 

<img src="youtube.jpg">

Playing the video will prompts us `Picasso's Guernica` and the title of that video is `Guernica 3D`.

Hmmm?? Well, let's leave that for now and move forward with binwalk.

Let's now use binwalk to check if there are any embedded files in these images aside from what we've discovered earlier.

```
$ binwalk monalisa.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
450363        0x6DF3B         Zip archive data, at least v2.0 to extract, uncompressed size: 117958, name: famous.zip
450440        0x6DF88         Zip archive data, encrypted at least v2.0 to extract, compressed size: 117776, uncompressed size: 122869, name: Mona.jpg
568411        0x8AC5B         End of Zip archive
568537        0x8ACD9         End of Zip archive
```

```
$ binwalk Plans.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
```

```
$ binwalk Thepassword_is_the_small_name_of_the_actor_named_Hanks.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
```

So there's only 1 image with an embedded zip file named `famous.zip` and inside of that zip file is an image named `Mona.jpg`. 
Let's try to extract the file using this command: `binwalk -e monalisa.jpg`.

Extracted Files are:
- _monalisa.jpg.extracted/
  - 6DF3B.zip
  - famous.zip

When opening the famous.zip file, it asks us for a password. Going back to the given images above, the third image gave us a hint. So let's try to use `TOM` as password.

```
$ unzip famous.zip 
Archive:  famous.zip
[famous.zip] Mona.jpg password: 
password incorrect--reenter: 
password incorrect--reenter: 
   skipping: Mona.jpg                incorrect password
```

Oh fudge, what to do now.. Well, the next thing I did is to find for a tool that will bruteforce the zip file with a dictionary.

Then I found this -> [fcrackzip](https://github.com/hyc/fcrackzip).
fcrackzip is a braindead program for cracking encrypted ZIP archives.

So Let's try this tool and bruteforce the password of `famous.zip` file.

```
$ fcrackzip -u -D -p rockyou.txt famous.zip 
PASSWORD FOUND!!!!: pw == leonardo
```

Poof, we just got the password!

Let's unzip the `famous.zip` file now.

```
$ unzip famous.zip 
Archive:  famous.zip
[famous.zip] Mona.jpg password: 
  inflating: Mona.jpg
```

Great! We just got this image named `Mona.jpg`.

<img src="Mona.jpg">

Next step is to `binwalk` that image.

```
$ binwalk Mona.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
```

How about `strings`?

```
$ strings Mona.jpg | awk 'length($0) > 10'
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
RIR^M}g.'>_
```

Uhmm.. We haven't used `TOM` yet. Maybe we can use `steghide` and use `TOM` as password to extract hidden files.

```
$ steghide extract -sf Mona.jpg -p TOM
steghide: could not extract any data with that passphrase!
```

Okay.. Let's try this hint: `Thepassword_is_the_small_name_of_the_actor_named_Hanks.jpg`

```
$ steghide extract -sf Mona.jpg -p tom
steghide: could not extract any data with that passphrase!
```

Oh fugde, it's not even working!!

Ohh.. how about `Guernica` from the YouTube video we've discovered in `Plans.jpg`?

```
$ steghide extract -sf Mona.jpg -p Guernica
wrote extracted data to "key".
```

Holy Moly! Guernica is the password!

Let's check the content of that file!

```
$ cat key 
VTBaU1EyVXdNSGRpYTBKbVZFUkdObEZHT0doak1UbEZUVEJDUldaUlBUMD0=
```

Oh, a BASE64 ciphertext.

```
$ echo 'VTBaU1EyVXdNSGRpYTBKbVZFUkdObEZHT0doak1UbEZUVEJDUldaUlBUMD0=' | base64 --decode
U0ZSQ2UwMHdia0JmVERGNlFGOGhjMTlFTTBCRWZRPT0=
```

A BASE64 again? For real?! How many times should I decode that fudge to get the original text?

Oh fudge.. wait.. The title of the video is `Guernica 3D` and we already used `Guernica` as password.. how about `3D`? :)

I guess `3D` means `3 times of Decoding`.

Let's try it!

```
$ cat key | base64 --decode | base64 --decode | base64 --decode
HTB{M0n@_L1z@_!s_D3@D}
```

Booyah! We got the flag!
