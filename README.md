![Alt text](title.png)

Discord bot using the cryptography toolkit of [SkeletonKey](https://github.com/CosmodiumCS/SkeletonKey) with the Nextcord API wrapper.

## Usage
Usage continues the trend of the SkeletonKey suite often. See the help menu by simply using `/help`.

## Setting up yourself
Should you want to use the code yourself, you need only replace the Discord token in `main.py`, and generate an invite link of your own.

#### Token & Guild ID
You will need to add your own token and guild id in `main.py` under `client.run()`. It is recommended that it is stored in a `.env` file for better security. Rename `.env_example` in the root directory and add your own credentials as follows:

```
TOKEN=your token here
GUILD_ID=your guild id
```

Your `GUILD_ID` can be found by enabling developer mode in the advanced settings of the discord client, right clicking and selecting copy ID on your server of choice.

> WARNING: This token controls your entire bot. **It is very important you keep it hidden.**

#### Discord Developer 
You will also need to make your own [discord developer](https://discord.com/developers/docs/intro) account to aquire said token.

#### Invite Link
You will need to make an invite link in your discord developer portal.

## Credits
 - [misarb](https://github.com/Soulsender/Earth-Invader/pull/6) - md5 and morse code.
 - Based on the original [Cryptex Project](https://github.com/SSGorg/Cryptex)

