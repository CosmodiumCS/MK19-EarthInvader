![Alt text](assets/title.png)

Discord bot using the cryptography toolkit of [SkeletonKey](https://github.com/CosmodiumCS/SkeletonKey) with the Nextcord API wrapper.

[Offical invite link](https://discord.com/api/oauth2/authorize?client_id=993324580125032538&permissions=8&scope=applications.commands+bot)

## Usage
Usage continues the trend of the SkeletonKey suite often. See the help menu by simply using `/help`.

## Setting up yourself
Should you want to use the code yourself, you can either use the Docker container or replace the Discord token in `main.py`. You will then have to generate an invite link of your own. The docker container is recommended, as it is easier to daemonize.

### Using With Docker
You can pull the latest image from dockerhub and run it with:
```
docker pull soulsender/earth-invader:latest
docker run -e TOKEN=yourtoken earth-invader WEBHOOK_URL=url
```
or alternatively with the docker-compose file.

You can get your `TOKEN` from the [discord developer portal](https://discord.com/developers/docs/intro).
> WARNING: This token controls your entire bot. **It is very important you keep it hidden.**

You can get your logging `WEBHOOK_URL` by going to a channel in a server, going to settings, and webhooks.

#### Using With Python
You will need to add your own token in `src/main.py` under `client.run()`. It's recommended you store the token and webhook in an environment (`.env`) file for better security. Rename `.env_example` in the root directory and add your own credentials.

#### Invite Link
You will need to make an invite link in your Discord developer portal.

## Credits
 - [misarb](https://github.com/Soulsender/Earth-Invader/pull/6) - md5 and morse code.
 - Based on the original [Cryptex Project](https://github.com/SSGorg/Cryptex)
 - Icon by [Adioma](https://adioma.com).