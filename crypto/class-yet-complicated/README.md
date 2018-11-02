# Crypto Challenge: Classic, yet complicated! (10 Points)

**Find the plaintext, the key is your flag! <br>
Flag format : HTB{key in lowercase}**

This challenge gave us a file named ciphertext.txt.

```
$ cat ciphertext.txt 
alp gwcsepul gtavaf, nlv prgpbpsu mb h jcpbyvdlq, ipltga rv glniypfa we ekl 16xs nsjhlcb. px td o lccjdstslpahzn fptspf xstlxzi te iosj ezv sc xcns ttsoic lzlvrmhaw ez sjqijsa xsp rwhr. tq vxspf sciov, alp wsphvcv pr ess rwxpqlvp nwlvvc dyi dswbhvo ef htqtafvyw hqzfbpg, ezutewwm zcep xzmyr o scio ry tscoos rd woi pyqnmgelvr vpm . qbctnl xsp akbflowllmspwt nlwlpcg, lccjdstslpahzn fptspfo oip qvx dfgysgelipp ec bfvbxlrnj ojocjvpw, ld akfv ekhr zys hskehy my eva dclluxpih yoe mh yiacsoseehk fj l gebxwh sieesn we ekl iynfudktru. xsp yam zd woi qwoc.
```

Based on my observation, there are similar words/letters in the ciphertext such as `alp` and `ekl`. So this is definitely a Vigenère Cipher. So to decode this ciphertext, we must know the `key` used to encode the ciphertext.
Luckily this website https://www.dcode.fr/vigenere-cipher can help us decode the ciphertext by knowing a plaintext word used in the ciphertext.

So going back to the repeating words/letters.. I'm highly confident that `alp` is equivalent to the word `the`. And I finally decoded the ciphertext.

Decoded ciphertext:
```
the vigenere cipher, was invented by a frenchman, blaise de vigenere in the 16th century. it is a polyalphabetic cipher because it uses two or more cipher alphabets to encrypt the data. in other words, the letters in the vigenere cipher are shifted by different amounts, normally done using a word or phrase as the encryption key . unlike the monoalphabetic ciphers, polyalphabetic ciphers are not susceptible to frequency analysis, as more than one letter in the plaintext can be represented by a single letter in the encryption. the key is the flag.
```

Aside from getting the decoded ciphertext, I also got the key which is `helloworld`.
