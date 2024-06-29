[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13142467)
# Discord Bot Project

In this project, you will build your own bot to interact with Discord servers
using the Discord API. You will use the [discord.py](https://discordpy.readthedocs.io/en/latest/)
library to interact with the Discord API. Your devcontainer is already set up with the necessary
libraries. Additionally, you have been provided with a minimal bot that you can use as a starting
point for your project.

## Getting Started

1. Log into Discord and create a new server (name it whatever you want).
2. Follow the directions [here](https://discordpy.readthedocs.io/en/latest/discord.html) to create
   a bot user and add it to your server. Be sure that the bot has the permissions to read and send messages.
3. Copy the bot token and paste it into the `DISCORD_TOKEN` environment variable in the `.env` file.
4. Generate the url to add your bot to your server by following the directions [here](https://discordpy.readthedocs.io/en/latest/discord.html#inviting-your-bot).
5. Run main.py. You should see the message "Logged in as <your bot name>" in the terminal.
6. Test your bot by using the command `$hello` in your server. Your bot should respond with "Hello!".

## Project Requirements

The purpose of this project is to expand the functionality of the bot provided to you. The exact type of bot you create is up to you. However, your bot must meet the following requirements:

1. Your bot must respond to at least 3 different commands or events. These commands can be anything you want, but they must be different from the `$hello` command already provided. For example, you could create a command that responds with a random number, or a command that responds with a random meme. For a explanation of the discord API, see [the discord docs](https://discordpy.readthedocs.io/en/latest/api.html).
2. Your bot must use at least 1 external API. For example, you could use the [Random Dog API](https://random.dog/woof.json) to get a random dog image, or the [Random Cat API](https://aws.random.cat/meow) to get a random cat image. Or something else; truth be told Copilot came up with those two and they're a little weird. Here's another one: suppose you have a study group chat and you are all stuck on a question. You could link this project with the last one and get the bot to send your teacher and email containing content from the last 10 messages (or whatever). If you are strapped for ideas, consider asking Copilot or ChatGPT for some suggestions.
3. Your code should be tidy and well-documented. This means good naming and formatting conventions, as well as comments and docstrings where appropriate. You should also include a README.md (you can rename this one and created your own README.md) that explains how to use your bot. This should include a list of commands and what they do, as well as any other information that you think is relevant.

### Helper Code

In addition to a basic bot, you have also been provided with a small amount of helper code. The first is the .env file. As noted above, you will paste your bot token in here. This is your bots unique password:_Do not paste the bot token into the code or add it to your repository in any way_. You will also need to keep the `load_dotenv()` line in your code. This line loads the environment variables from the 
.env file into your program. You will also need to keep the `os.getenv('DISCORD_TOKEN')` line in your code. This line gets the value of the `DISCORD_TOKEN` environment variable.

Also provided is a really lousy database module. This is located in db.py and contains exactly two functions:

1. `put(key, value)` - stores a value in the database with the given key
2. `get(key)` - retrieves the value stored in the database with the given key

This is basically the same as using `someDictionary[key] = value` except that the data will be stored in a file and persist between runs of the program. You may or may not find this useful.

## Submission

This project will be conducted through GitHub classroom using codespaces. You *must* still commit and push your code to GitHub; however, you can and should use the built-in git functionality. Please remember to commit frequently and use good, informative commit messages.

### AI Policy

You will notice that Copilot Chat has been added to your codespace. I am expecting that you will use it as a research tool (alongside the usual Googling and following the provided links). You _may_ use it to generate and explain code as you please. _However_, you must be able to explain the code that you use. If you cannot explain the code, you should not use it. Or better yet, you could ask Copilot to explain it until you have a comprehensive understanding.

Please take this seriously: learning to ue the AI well is as important as learning about APIs and OAuth. Piling up a bunch of code that you don't understand will defeat both purposes of this assignment. If you have any questions, please ask.

Finally, since you have access to AI, I will be expecting your code to be especially tidy and well-tested. It should be relatively hard for me to break your code, and fair warning, I'm pretty good at it. 

And now for some unhinged nonsense from Copilot as a reminder of the limitations of the AI and the importance of reading and understanding the code you use:

If I can break your code, I will. If I can't, I will ask you to break it for me. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me. If you can't, I will ask you to fix it. If you can't, I will ask you to explain it to me.