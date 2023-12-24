![Alt text](title.png)

Discord bot using the cryptography toolkit of [SkeletonKey](https://github.com/CosmodiumCS/SkeletonKey) with the Nextcord API wrapper.

[Offical invite link](https://discord.com/oauth2/authorize?client_id=993324580125032538&permissions=139586947136&scope=bot%20applications.commands)

## Usage
Usage continues the trend of the SkeletonKey suite often. See the help menu by simply using `/help`.

## Setting up yourself
Should you want to use the code yourself, you can either use the Docker container or replace the Discord token in `main.py`. You will then have to generate an invite link of your own.

#### Discord Developer 
You will also need to make your own [discord developer](https://discord.com/developers/docs/intro) account to acquire said token.

#### Using With Docker
You can pull the latest image from dockerhub and run it with:
```
docker pull soulsender/earth-invader
docker run -e TOKEN=yourtoken earth-invader
```
or alternatively with the docker-compose file.

#### Using With Python
You will need to add your own token in `main.py` under `client.run()`. It's recommended you store the token in an environment (`.env`) file for better security. Rename `.env_example` in the root directory and add your own credentials as follows:

```
TOKEN=your token here
```

> WARNING: This token controls your entire bot. **It is very important you keep it hidden.**

#### Invite Link
You will need to make an invite link in your Discord developer portal.

## Credits
 - [misarb](https://github.com/Soulsender/Earth-Invader/pull/6) - md5 and morse code.
 - Based on the original [Cryptex Project](https://github.com/SSGorg/Cryptex)
 - Icon by [Adioma](https://adioma.com).
