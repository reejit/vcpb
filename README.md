# Pyrogram bot to automate streaming music in voice chats

## Help
If you face an error, want to discuss this project or get support for it, join [it's group](https://t.me/VoiceChatPyroBot) on Telegram.

## Requirements
* A computer (a Debian-based Linux recommmended).
* An alt Telegram account.
* Bot token from [@BotFather](https://t.me/BotFather).
* API ID & hash from [my.telegram.org](https://my.telegram.org).
* Python 3.6 or newer & latest version of pip.
* MPV (and libmpv).
* A software to forward audio to tdesktop (Linux: pulseaudio, Windows: voicemeeter).

## Deploying

### The code

#### Cloning
```
    git clone https://github.com/rojserbest/vcpb.git vcpb && cd vcpb
```

#### Configuring

##### CLI args (when running bot.py)
Example:
```
python3 bot.py \
--api-id 1 \
--api-hash abcdef1234 \
--token 1234567890:ABCDEF \
--sudo-users 111111 22222 33333 \
--mongo-db-uri mongodb+srv://user:pass@subdomain.domain.extention/vcpb \
--group -1001876543112 \
--dur-limit 10 \
--lang en
```

##### Config file
Copy `config/sample_config.py` to `config/config.py` and make it use your credentials (you can also give those as an arg when running bot.py):
`API_ID` int: your api id from [my.telegram.org](https://my.telegram.org)
`API_HASH` str: your api hash from [my.telegram.org](https://my.telegram.org)
`TOKEN` str: your bot token from [@BotFather](https://t.me/BotFather)
`SUDO_USERS` list(int): a list of user ids which can pause, skip and change volume
`MONGO_DB_URI` str: your MongoDB URI (you can get one for free in their [official website](https://mongodb.com/), sign up, create a cluster and a database named "vcpb")
`GROUP` int: the id of the group where your bot plays (not required if both `USERS_MUST_JOIN` and `LOG` are false)
`USERS_MUST_JOIN` bool: if true, only users which are in the group can use the bot
`LOG` bool: if true, now playing messages will be sent to the group
`LANG` str: your bot language, choose an available language code in [strings/](https://github.com/rojserbest/VoiceChatPyroBot/tree/main/strings)
`DUR_LIMIT` int: max video duration in minutes for downloads

#### PIP requirements

`pip(3) install -U -r requirements.txt`

### Running

⚠️ Warning for Linux users: don't run any command as root (except those which require it), else you might face bulky problems. You can create a user with `adduser music` and add it to sudoers using `sudo usermod -aG sudo music`.

ℹ️ The volume command isn't working on Windows.

#### On Linux VPS

These are apt package manager instructions but you can install the required packages with other package managers too.

1. Update and upgrade apt:
`sudo apt update && sudo apt upgrade -y`

2. Install requirements:
`sudo apt install python3-pip xrdp pulseaudio mpv libmpv-dev screen -y`

3. Download tdesktop:
`cd ~ && wget https://telegram.org/dl/desktop/linux -O tdesktop.tar.xz && tar -xf tdesktop.tar.xz && rm tdesktop.tar.xz`

4. Configure XRDP session to only start Telegram:
`echo "~/Telegram/Telegram" >~/.xsession`

5. Enable pulseaudio service (you can skip this step if you don't have systemctl):
`systemctl --user enable pulseaudio`

6. Restart the machine:
`sudo reboot`

7. Start pulseaudio (you can skip this step if you did step 5):
`pulseaudio --start`

8. Go back to directory of the clone and load a pulseaudio null sink, by running:
`bash pa.sh`

9. Make a screen for the bot and attach to it:
`screen -S vcbot`

10. Run the bot:
`python(3) bot.py`

11. Detattach from the screen by pressing CTRL+A then CTRL+D.

12. Open a remote desktop client and login to your user.

13. You should see the Telegram GUI, just login, join a voice chat and set `VoiceChatPyroBot` as your microphone.

14. Done, you can now start sending commands to your bot and it'll stream in the voice chat.

#### On Linux desktop

These are apt package manager instructions but you can install the required packages with other package managers too.

1. Update and upgrade apt:
`sudo apt update && sudo apt upgrade -y`

2. Install requirements:
`sudo apt install pulseaudio mpv libmpv-dev pavucontrol screen -y`

3. If you have Telegram skip this step, otherwise download it [here](https://desktop.telegram.org).

4. Go to directory of the clone and load a pulseaudio null sink, by running:
`bash pa.sh`

5. Make a screen for the bot and attach to it:
`screen -S vcbot`

6. Run the bot:
`python(3) bot.py`

7. Detattach from the screen by pressing CTRL+A then CTRL+D.

8. Open Telegram, join a voice chat and set `VoiceChatPyroBot` as your microphone.

9. Done, you can now start sending commands to your bot and it'll stream in the voice chat.

#### On Windows 10 PC

1. Download Voicemeeter [here](https://vb-audio.com/Voicemeeter/index.htm) and install it.

2. Download virtual audio cable [here](https://vb-audio.com/Cable/index.htm) and install it.

3. Reboot.

4. Right click the speaker account in your taskbar, then click playback.

5. Set Voicemeeter input and Voicemeeter output as default and click OK.

6. Download MPV.

7. Start Voicemeeter engine.

8. Run the bot:
`python bot.py`

9. Open Telegram, join a voice chat and set `Voicemeeter input` as your microphone.

10. Done, you can now start sending commands to your bot and it'll stream in the voice chat.

## Usage

#### Streaming YouTube videos

1. Open [YouTube](https://youtube.com) in your browser, and search for a song.
2. Copy the complete video URL to clipboard and send it to your bot in private.

#### Method 2

1. Enable inline for you bot in  [@BotFather](https://t.me/BotFather).
2. In your bot's private, type @usernameOfYourBot followed by your YouTube search query, and click a result.

## Authors & Acknowledgment

### Inspiration
* [@AndrewLaneX](https://github.com/AndrewLaneX) ([Telegram](https://t.me/TwitFace))

### Development & contribution
* [@rojserbest](https://github.com/rojserbest) ([Telegram](https://t.me/su_Theta))
* [@iiiiii1wepfj](https://github.com/iiiiii1wepfj) ([Telegram](https://t.me/itayki))
* [@ByteOPCode](https://github.com/ByteOPCode) ([Telegram](https://t.me/BAZINGA))
* [@pokurt](https://github.com/pokurt) ([Telegram](https://t.me/DeprecatedUser))
* [@Quiec](https://github.com/Quiec) ([Telegram](https://t.me/fusuf))
* [@SpEcHiDe](https://github.com/SpEcHiDe) ([Telegram](https://t.me/SpEcHIDe))
* [@sudoAlphaX](https://github.com/sudoAlphaX) ([Telegram](https://t.me/su_Alpha))
* [@zomenaro](https://github.com/zomenaro)
* [@subinps](https://github.com/subinps)
* [@NicolaSmaniotto](https://github.com/NicolaSmaniotto)
* [@SelaxG](https://github.com/SelaxG)
* [@sppidy](https://github.com/sppidy)
