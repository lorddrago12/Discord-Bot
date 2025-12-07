# Discord Bot

An updated Discord bot built using Python, `discord.py`, and `discord.ext.commands`. This version introduces slash commands, improved structure, and guild-specific command syncing.

---

## 📌 What's New

* Switched from `discord.Client` to `commands.Bot` for more functionality
* Added slash commands using `app_commands`
* Synced commands to a specific guild for faster updates
* Added a `/hello` command
* Added a `/printer` command that echoes user input
* Improved bot structure and event handling

---

## 📂 How It Works

### Event Improvements

* **on_ready** now syncs slash commands to your server
* **on_message** still listens for normal text commands like `hello` and `how are you`
* **on_member_join** attempts to welcome new users in the `#general` channel

### Slash Commands

* `/hello` — Replies with a personal greeting
* `/printer` — Sends back whatever the user types
* `/coffebreak` — Sends an embed with a title, thumbnail, field, author, and footer
