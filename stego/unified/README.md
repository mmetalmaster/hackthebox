# Stego Challenge: Unified (20 Points)

**This file seems to contain innocuous information. What is the true message?**

```
$ cat BOD_30079.txt
<<-----UTF-8 MESSAGE BOD_30079 BEGINS---->>

Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems.

The system works in many languages. 该系统以许多语言工作. يعمل النظام في العديد من اللغات. 
󠁈󠁔󠁂󠁻󠁴󠁲󠀱󠁴󠁨󠀳󠁭󠀱󠁵󠀵󠁟󠀱󠀴󠀹󠀹󠁽���� ���� �� �������� ��� ����� � ���� ��� ��
Το σύστημα λειτουργεί σε πολλές γλώσσες.Система работает на многих языках.

Steganography is the practice of concealing messages within other non-secret text or data.
The cover media may appear unremarkable at first glance and will require close investigation.

<<-----UTF-8 MESSAGE BOD_30079 ENDS----->>
```

First thing I did is to search on Google for `Unicode Text Steganography` then I found this link:
https://www.irongeek.com/i.php?page=security/unicode-steganography-homoglyph-encoder

I copied the Unicode in the text file and pasted it to Stegotext field and pressed Decode button to get the flag.

Text to be decoded:
```
该系统以许多语言工作. يعمل النظام في العديد من اللغات. 
󠁈󠁔󠁂󠁻󠁴󠁲󠀱󠁴󠁨󠀳󠁭󠀱󠁵󠀵󠁟󠀱󠀴󠀹󠀹󠁽���� ���� �� �������� ��� ����� � ���� ��� ��
Το σύστημα λειτουργεί σε πολλές γλώσσες.Система работает на многих языках
```

Result:
```
HTB{tr1th3m1u5_1499}
```
