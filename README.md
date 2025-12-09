# Discord Bot 

---

## 📌 What This Project Is

This is a custom Discord bot built using Python and the `discord.py` library. It includes:

* Traditional message-based responses
* Modern slash commands
* Guild‑specific command syncing
* Automatic events like member join detection
* A full embed‑sending command

The goal of this project is to learn and implement real Discord bot features while keeping the structure clean and understandable.

---

## ✨ Explanation

1. **The bot connects to Discord using a token.**
2. **It listens for certain events** (messages, user joins, ready state).
3. **It reacts** either by sending text replies, executing slash commands, or sending embed messages.
4. **Slash commands are registered (synced)** to a specific server so they appear instantly.

If you know the basics of Python functions, classes, and async programming, everything in this bot will make sense.

---

## 🏗️ How the Code Is Structured

### 1. The Bot Class

```python
class client(commands.Bot):
```

Instead of using the old `discord.Client`, the project uses `commands.Bot`, which provides:

* Easy slash command support
* Better command handling
* Automatic integration with `app_commands`

This bot overrides important event functions to define its behavior.

### 2. `on_ready` — Bot Startup Logic

This event runs when the bot successfully logs into Discord.
It also includes **guild-specific slash command syncing**, ensuring the new commands appear instantly in your server.

### 3. `on_message` — Detecting Text Commands

This section checks user messages and replies to:

* `hello`
* `how are you`

This is the traditional way Discord bots worked before slash commands existed.

### 4. `on_member_join` — Welcoming New Members

Triggered when someone joins the server.
The bot looks for a channel named `general` and sends a welcome message.

### 5. Slash Commands

These are created with:

```python
@client.tree.command(...)
```

Slash commands in this project:

* `/hello` → Greets the user
* `/printer` → Prints whatever the user types
* `/coffebreak` → Sends a styled embed message

Slash commands are more modern, easier for users, and do not rely on prefix-based messages.

### 6. Embed Command

The `/coffebreak` command demonstrates:

* Titles
* URLs
* Descriptions
* Thumbnails
* Fields
* Authors
* Footers

This is important because embeds are used in most modern Discord bot features.

---

## 🔄 How the Bot Processes a User Action

1. **User does something** (sends a message or uses a slash command)
2. **Discord sends that event to the bot**
3. The bot checks:

   * Which event happened?
   * What command was used?
4. It executes the matching function (message response, slash command, or embed).

This is the essence of event‑driven programming.

---

## 📥 Why the Bot Syncs Commands

New slash commands don't appear instantly unless they are synced.
By restricting syncing to a single guild, updates are:

* Instant
* Safer
* Easier to test

This avoids waiting up to an hour for global commands to update.

---
