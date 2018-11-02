from cryptography.fernet import Fernet

key = 'hBU9lesroX_veFoHz-xUcaz4_ymH-D8p28IP_4rtjq0='

f = Fernet(key)

token = 'gAAAAABaDDCRPXCPdGDcBKFqEFz9zvnaiLUbWHqxXqScTTYWfZJcz-WhH7rf_fYHo67zGzJAdkrwATuMptY-nJmU-eYG3HKLO9WDLmO27sex1-R85CZEFCU='

print(f.decrypt(token))