# Ireland Helper Telegram Bot

## Overview
A Telegram bot that provides information about Ireland, specifically Dublin, and moderates selling posts in group chats.

## Bot Token
- Uses `BOT_TOKEN` environment variable

## Features

### 1. /start Command
- Sends welcome message: "Привет! Я твой помощник по Ирландии. Ты можешь спросить меня о Дублине или использовать команды."

### 2. Selling Post Moderation
- Keywords detected: `продам`, `продается`, `продається`, `продаются`
- Action: Deletes the message and sends a warning with links to appropriate channels:
  - [Барахолка Ирландии](https://t.me/buy_sell_ireland)
  - [Объявления Одесса-Ирландия](https://t.me/Odessa_IE/3806)
- Requires admin rights to delete messages

### 3. Citywest Handler
- Keywords: `citywest`, `ситивест`, `ситиуест`, `свтівест`
- Provides info about Citywest Convention Centre refugee reception center:
  - Address: Garters Lane, Saggart, Co Dublin, D24 A38Y
  - Schedule for temporary protection applications, housing inquiries, fingerprinting

### 4. Guinness Handler
- Keyword: `гиннесс`
- Provides info about Guinness stout and St. James's Gate brewery

### 5. Dublin Handler
- Keyword: `дублин`
- Provides info about Dublin - capital city, population ~1.2 million

## Technical Details
- Uses `pyTelegramBotAPI` library
- Runs with `bot.polling()` for continuous operation
- Markdown parse mode used for formatted messages with links
