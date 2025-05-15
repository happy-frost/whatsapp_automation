# WhatsApp Web Automation (Learning Project)

This is a **learning-focused Python project** that uses Selenium to automate simple tasks on [WhatsApp Web](https://web.whatsapp.com/), such as logging in and sending messages to contacts. Insipiration was the missing feature in automating sending messages to groups on whatsapp official api, so this library mainly focuses on sending messages to groups.

> ⚠️ **Disclaimer**: This project is for **educational purposes only**.  
It is **not affiliated with WhatsApp or Meta**.
Use at your own risk and ensure compliance with WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/terms-of-service). 
Use responsibly and at your own risk.   
---

## 📚 Features

- Automates WhatsApp Web login (via manual QR code scan)
- Send messages to groups using Selenium
- Send documents to groups using selenium
- Modular codebase for experimentation and learning
- Easily extendable
---

## 🛠️ Setup

### Requirements
- Python 3.7+
- Google Chrome + ChromeDriver
- Selenium

### Install dependencies

```bash
pip install selenium
```

### Using Google Chrome Profile
If you would like to use a google chrome profile for your chrome browser, simply add the user-data-dir as the first argument to the initilization function and profile-directory as the second argument (optional value defualts to "Default")

```
whatsapp = Whatsapp(user_data_dir,profile_dir)
```
You can try using the profile directory at the default location. However, if that does not work, fully close all chrome profile and launch it with a clean user data directory:
Commands for windows
1. Close all chrome process
```
taskkill /f /im chrome.exe
```
2. Launch Chrome with Clean User Data Directory
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\ChromeProfiles\MyChromeProfile"
```
3. Configure the profile

Do any configuration as you may require

4. Add the path to your profile to the arguments when instatiating the Whatsapp class
```
whatsapp = Whatsapp(user_data_dir,profile_dir)
```

### Testing Locally
To test copy the sample.env to a .env file in the root directory, then run: 
```
pytest
``` 