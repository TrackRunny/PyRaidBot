<!-- MAIN TITLE -->
# • PyRaidBot

<!-- BADGES -->
![Discord.py Version](https://img.shields.io/badge/discord.py-1.3.1-blue?style=flat-square)
![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue?style=flat-square)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square)

<!-- KEY INFORMATION HEADER -->
## → Bot Information / features

* Raid bot for discord servers.
* Removes all channels, roles + creates new roles and new text channels + spams.
* Customize how many channels / roles you want to create.
* Every guild that has the bot will be raided.

<!-- MODULES HEADER -->
## → Modules

* Raiding (Includes Spamming, Role Deletion, Channel Deletion, Mass Creating Channels, Mass Creating Roles)

<!-- INSTALLATION HEADER -->
## → Installation

**NOTE: RAID BOTS ARE AGAINST THE [DISCORD TOS](https://discordapp.com/terms). USING THIS ON SERVERS THAT ARE NOT YOURS WILL GET YOUR ACCOUNT BANNED! YOU CAN EVEN GET BANNED FOR USING THIS BOT ON YOUR OWN DISCORD SERVER. I AM NOT RESPONSIBLE FOR ANYTHING YOU DO WITH THE SOURCE CODE.**

**I ORIGINALLY MADE THIS BOT FOR TESTING ANTI-SPAM BOTS AS WELL AS BOTS THAT BACKUP YOUR SERVER DATA (Channels, roles, messages, ect)**

---

<!-- Installation Instructions -->
* First, clone this github repo and change directories inside of it.

```markdown
git clone https://github.com/TrackRunny/PyRaidBot.git
<!-- Cloning the github repo -->

cd PyRaidBot
<!-- Changing directories into the repository -->
```

* Next, please install the [**discord.py**](https://github.com/Rapptz/discord.py) module.

```markdown
pip install discord.py
<!-- Remember: Only use this if you only have python 3 installed. -->

or

pip3 install discord.py
<!-- Remember: Use this if you have two versions of python and / or you have python 2 and python 3. -->

```

* Lastly, provide a bot token **and** a Discord account owner ID. You should use your account ID as the bot commands will only run from the correct owner ID.

```python
# - File: PyRaidBot.py | Line 10

# - PUT YOUR DISCORD ACCOUNT ID HERE, DO NOT PUT YOUR ACCOUNT ID IN QUOTES!
# - EXAMPLE: account_id = 546812331213062144
account_id = "PUT YOUR DISCORD ACCOUNT ID HERE"

# - File: PyRaidBot.py | Line 18
bot_token = "BOT TOKEN HERE"
```

## → Finishing Installation

Everything should be ready to go!

To start the bot do, `python PyRaidBot.py` **or** `python3 PyRaidBot.py`.

<!-- LICENSE INFO -->
## → License

This project is licensed under the GPLv3.

<!-- END OF README -->
## → Questions / Contact me

* Discord Account: `TrackRunny#0001`
