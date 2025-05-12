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

### Testing Locally
To test copy the sample.env to a .env file in the root directory, then run: 
```
pytest
``` 