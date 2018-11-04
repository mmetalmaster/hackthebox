# Stego Challenge: Senseless Behaviour (50 Points)

**John is practicing his steganography skills but don't let the space kittens affect what you see... There is more than one way to uncover hidden secrets.**

The author gave as a wav file.

```
$ file meow.wav 
meow.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz
```

Let's check the file using binwalk and strings.

```
$ binwalk meow.wav 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
12897995      0xC4CECB        MySQL MISAM compressed data file Version 3
20226912      0x134A360       MySQL MISAM index file Version 3
26753717      0x1983AB5       MySQL MISAM compressed data file Version 2
36745260      0x230B02C       MySQL MISAM compressed data file Version 11
```

```
$ strings meow.wav | awk 'length($0) > 20'
35/*o7Q5p:p7=<,2]<5(d:]
(A$"2P'M<P._@t0Q@B/=A
#"A=)J>O+J6~)o-'$O'L!h!
d+) e-z"(/&$R1V&'4u'k6
'*( :h:66\1T4,&cC9*~?
1*3S7u4(9B5#8x4A3@1H(
.8#K/&#l0}(B4?,&4
                 '-,~#9&
>s8aBB9wDf8gC>42@o28;
AP:cBG2I:[:]=[;"<%Aq9$I
#o;;%W@a"YAb V?G"B=R#
1|-.32/752/:60+{4^'p3
4l"[8Q$%:X&39>')4M%2.4#
P^V_L~S29rD`AyR1?JM40D?
0pCD/YCS,8Bi)\BJ'qCF&
C~'C?4&_CN*?ET)oCx"7J
6k5w6y8I3]:70S9X..7g.
```

We got nothing.

Let's fire up Audacity and check if there's any hint.

<img src="audacity.png">

Same thing, nothing. :/

I searched for steg tool for wav and found this `WavSteg.py` tool from [ragibson's Steganography repo](https://github.com/ragibson/Steganography) and tried using it.

```
$ python3 WavSteg.py -r -s meow.wav -o output.txt -n 2 -b 1000000
Reading files...                   Done in 0.06 s
Recovering 1000000 bytes...        Done in 0.28 s
Writing to output file...          Done in 0.01 s
```

Opening the output.txt file will greet us with bunch of useless data.

<img src="wavsteg-output.png">

I just tried that tool to check if we could get something with 1 million bytes of data to recover from the wav file. Apparently, this requires the size in bytes of the hidden data to be accurate or the result may be too short or contain extraneous data.

Then I searched and tried any tools that could help me discover anything relevant for this challenge but end up nothing until I found this tool called [steg_brute](https://github.com/Va5c0/Steghide-Brute-Force-Tool). This tool executes a brute force attack with Steghide.

```
$ python steg_brute.py -b -d rockyou.txt -f meow.wav 

 [i] Searching...
  0%|                |
  
 [+] Information obtained with password: skittles
 
 wrote extracted data to "meow_flag.txt".
 ```

The `meow_flag.txt` file contains a long BASE64 ciphertext and decoding it will return a long hexadecimal string. After that decoding process, we got an unreadable data but I suddenly noticed this familiar strings:

```
$ cat meow_flag.txt | base64 --decode | xxd -r -p | head -3
?PNG

IHDR?!ؑ? IDATx????S?w????]??:gww:??$v<0???A????,?B
                                                 B?c?Af2?1&Ll?9???Cϻ????֭??????H??t??>??????KK??Zo]XZe??U?
                                                                                                         ?O?0???ة?Ď????$??Q|?|?BGG??"~r???9?Ϭ0?p???UfgWHL_e2q???E&??????K??_dl?2cSK??^&qf??K7YY??OX??	˟|???#V??r?I??)+7????e??a??o??|?{???w???+????g߱??-?}????????????p???s?????m??A???淙u?n}??ͯ_?>?J???/???S???O??????7?????o????????Y??UF-??U?<}N=?j?
                                                                                     ??>y?Q?ۭV??????v?)?~????q???ظ?+7?t?A?zO2j???,?}???,]?U????Z???ŵ? ??=????o?J}???.?}!???ɟu??i??7??ō?;??O?x?!
                                                            ?n1??	?3kL/|"??u??|"????k,??`zf?ٹ5f??azf?????.??3?h??????3????-01????eƧ?2?Xf???LN?01????u&?W?J,˟Ϩ???n;9sM???:?3?H?]????̵??O?<?v|?7\?'?ߔ?7o?ضJ???񩫌O.16??ة+;??v?תɥW????v???????'???????E3ˌ??%:????CC????.D[AlG?w`2x1?[14?0??]?ؽ=8}a?m}xR????"?3J(<F?so[
                                                  _`?`?q????w???)z?&	GG??
                                                                            N?e`d^??9???9F?
                                                                                           ???>???Btu"?:1?~
                                                                                                           ?̎6
                                                                                                             ?[*k
                                                                                                                 f?????????????ҋ??At??l?????????!%?5F??I??t?N?I?N??Mx Axp?Hl???
                                             ??,ѡ9?26K82E0twK?މ ??B+f????dn???C?qzz?Fp?Dp??"???=ܾ??޶|???w'?u?@h?@?(??t?OJ?]???i"?鉜????????D?????????>H?oh??MMy-y??)???HU?>??Q??oT?????_K???ߦ??m?"K?????5???b?b??;v~[?}n
```

So I converted it to PNG.

```
$ cat meow_flag.txt | base64 --decode | xxd -r -p > meow.png
```

<img src="meow.png">

Let's check the image using binwalk and strings.

```
$ binwalk meow.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 702 x 395, 8-bit/color RGBA, non-interlaced
```

```
$ strings meow.png | awk 'length($0) > 10'
JZ`14Ct8syEth
X.199Ab4Fd0
Mx*N4>Kb>C:
!eY%aZ!eY#nR
EEM+rM5rM5RM-
w7W9J'8HF9H
MN|TNlDFdXA
$GW'EW/GW'C[#A]QF
Nl%Cb-Cj-Cli
OjRCjRCrBM|
#4ROP_K@WKP
x7{KfNnLr|}
n1b[6a3/b_1|
0IS?qc/IS?i
aB)e\%eT)cD.
ga#`a3la;fa#
e+id'cb7kfo
@-3Om>Mu.E5
I2<C2<M24I*b&
0lf!bb!lf>hd.P<
2lf%bd%bdyh
1na=nd-f`9,1
R)2I/RI/2i?
Ln5Ln5L~-B>
'l:6&FHLhHXTl
h$ai"nm%fi&bl$8\
fO*:G>6O.6Gn
3Dh8L$<A42Il<Nt,Nd4F2
bl4J84N42I$<
64H42J82Ahh
chhB^#E^#EV)A\,B\"BZ
O8:L$6Ixd6SG3K 4G8
FS+AU+AS+A#
~G|7K|7K:qL>w
Rl9!l9!2=ed
F+iZ#)j=)j=i
3EIU?Je>JAA
i(Qc/Va/VQ_
}%:y1:Y99J#
\`D]nGYlAYlA[jAU
dE:2U&*M.2E6
2u*rU*ju&zm
?8F 4.(8F04N$:)@px
[_JB]BD^B@Z
,bwu#U8Qi=Tnm
;8C"=F49L49B8>D 
IG/i[7YW/)k
OJ?DR?BR?FR7N
H[U$Lr265Sn
'<J$8L">E*9
```

Nothing interesting, so let's use Stegsolve and check differentt planes.

Then I found something with Red Plane - a Braille.

<img src="red-plane.png">

Converting this braille to text using this website https://www.dcode.fr/braille-alphabet, will give us `BLINDASABAT` as the result.
