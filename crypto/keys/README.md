# Crypto Challenge: Keys (40 Points)

**Can you decrypt the message?**

Let's check the given file:

```
$ cat keys.txt 
hBU9lesroX_veFoHz-xUcaz4_ymH-D8p28IP_4rtjq0=
gAAAAABaDDCRPXCPdGDcBKFqEFz9zvnaiLUbWHqxXqScTTYWfZJcz-WhH7rf_fYHo67zGzJAdkrwATuMptY-nJmU-eYG3HKLO9WDLmO27sex1-R85CZEFCU=
```

Hmm.. I'm pretty sure that's not a Base64.. To be honest, this is where I got stuck and ask to some friends online for a hint.

They gave me a hint: `symmetric encryption cryptography`

So I searched on Google for `symmetric encryption cryptography` and I found this documentation: https://cryptography.io/en/latest/fernet/

Ohh, Fernet.. Okay..

Solution:
```
from cryptography.fernet import Fernet

key = 'hBU9lesroX_veFoHz-xUcaz4_ymH-D8p28IP_4rtjq0='

f = Fernet(key)

token = 'gAAAAABaDDCRPXCPdGDcBKFqEFz9zvnaiLUbWHqxXqScTTYWfZJcz-WhH7rf_fYHo67zGzJAdkrwATuMptY-nJmU-eYG3HKLO9WDLmO27sex1-R85CZEFCU='

print(f.decrypt(token))
```

Running that python scripts gives us the flag:

```
$ python fernet-solver.py 
Flag : HTB{N0t_A_Fl1g!}
```
