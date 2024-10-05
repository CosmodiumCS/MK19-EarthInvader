![title](assets/title.png)
# Earth-Invader

A powerful Discord bot that utilizes the [SkeletonKey](https://github.com/CosmodiumCS/SkeletonKey) cryptography toolkit, built with the Nextcord API wrapper.

[Invite Earth-Invader](https://discord.com/api/oauth2/authorize?client_id=993324580125032538&permissions=8&scope=applications.commands+bot)

## Features
Earth-Invader integrates various cryptographic functions from the SkeletonKey suite. You can easily explore the features by using the `/help` command within Discord to access the help menu.

## Getting Started

### Running the Bot
You can run Earth-Invader in two primary ways: using Docker for a more seamless setup, or directly in Python by modifying the source code.

#### Option 1: Docker (Recommended)
Using Docker simplifies deployment and daemonization. You can pull the latest image and run it by executing the following:

```bash
docker pull soulsender/earth-invader:latest
docker run -e TOKEN=your_discord_token -e WEBHOOK_URL=your_webhook_url earth-invader
```

Alternatively, you can set up the bot with a `docker-compose` file. 

- **TOKEN**: Retrieve your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/docs/intro). This token grants full control over your bot, so ensure it's kept secure.
- **WEBHOOK_URL**: This is optional but recommended for logging. You can create a webhook URL in Discord by going to a channel's settings and selecting **Webhooks**.

#### Option 2: Python Setup with Poetry
To run Earth-Invader with Python using Poetry:

1. Clone the repository.
2. Install Poetry if you haven't already using [these](https://python-poetry.org/docs/#installing-with-pipx) instructions.
3. Navigate to the project directory and install the required dependencies using Poetry:
    ```sh
    poetry install
    ```
4. Replace the placeholder token in `src/main.py` under `client.run()` with your own Discord bot token.
5. Optionally, store your token and webhook URL in an environment file (`.env`) for added security. You can rename the `.env.example` file located in the root directory and add your credentials there.
6. Run the project using Poetry:
    ```sh
    poetry run python src/main.py
    ```

#### Generating an Invite Link
Once your bot is set up, generate an invite link through the Discord Developer Portal to invite it to your server. Ensure the necessary permissions are selected.

## Usage
The bot follows the pattern of other SkeletonKey suite tools. To get started with Earth-Invader's capabilities, simply type `/help` within your Discord server.

## Security Warning
**Important**: The bot's token controls its entire functionality. Keep it hidden and never expose it in public repositories or logs.

## Credits
- [0xSolanaceae](https://github.com/0xSolanaceae) - Codebase contributions and general improvements.
- [misarb](https://github.com/Soulsender/Earth-Invader/pull/6) - Contributions to MD5 and Morse code functionality.
- Built upon the original [Cryptex Project](https://github.com/SSGorg/Cryptex)
- Icon designed by [Adioma](https://adioma.com)