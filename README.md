# Telegram bot calculator and Wikipedia

## Functions
- Math calculations
- Search information on Wikipedia

## Requirements
- Python 3.8+
- Telegram account
- Bot token from [@BotFather](https://t.me/BotFather)

## Install and start

1. **Clone the repository**
```bash
git clone https://github.com/Just-codde/uni-telegram-bot.git
cd uni-telegram-bot

2. **Create a virtual environment**
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

3. **Install requirements**
pip install -r requirements.txt

4. **Set up the configuration**
cp .env.example .env
# Edit .env file and add your token:
# BOT_TOKEN=your_actual_token_here

5. **Start bot**
python calculator-bot.py

## Usage
Available commands:

    /start - Start working with the bot

    /help - Commands list and usage

    /calculate - Start calculation mode

    /wiki <request> - Search on Wikipedia


Example using /calculator:

Your message:
/calculate

Bot's message:
Wtite your math expression

Your message:
2+2*2

Bot's message:
Answer: 6

/calculate


Example using /wiki:

Your message:
/wiki Linux

Bot's message:
Linux

Linux is a family of open-source Unix-like operating systems...

https://en.wikipedia.org/wiki/Linux


Technical details

    Python 3.8+ - Programming language

    python-telegram-bot - Telegram API integration

    wikipedia - Wikipedia content access

    numexpr - Safe mathematical expressions evaluation

    python-dotenv - Environment configuration management


## Architecture

Main Application Structure

ApplicationBuilder()
├── Command Handlers
│   ├── /start → start() - Welcome message
│   ├── /help → help() - Command list
│   ├── /calculate → calculate() - Activate calculator mode
│   └── /wiki → wiki() - Wikipedia search
│
├── Message Handler → message_hand()
│   └── Processes user input in calculator mode
│
└── Core Functions
    ├── wiki_get() - Wikipedia API wrapper
    └── numexpr.evaluate() - Safe math evaluation


Data Flow:

1. User sends command → Telegram servers

2. Bot receives update → Appropriate handler

3. Calculator mode:
    User activates with /calculate

    Bot sets user state: user[user_id] = True

    Next message processed as math expression

    numexpr.evaluate() safely computes result

    State reset: user[user_id] = False

4. Wikipedia search:
    wikipedia.summary() gets article preview

    Error handling for disambiguation/page errors

    Returns formatted response with title, summary, and URL


Security Features:

    numexpr instead of eval() - prevents code injection

    User state management - isolates calculator sessions

    Exception handling - graceful error recovery


File Structure

telegram-bot/
├── calculator-bot.py      # Main bot application
├── requirements.txt       # Python dependencies
├── .env.example          # Configuration template
├── .env                  # Your credentials (NOT in git)
├── .gitignore           # Git ignore rules
└── README.md            # This file


## Error Handling

The bot includes comprehensive error handling for:

    Invalid mathematical expressions

    Wikipedia API failures

    Network connectivity issues

    User input validation


## Dependencies

See requirements.txt for complete list:

    python-telegram-bot - Modern Telegram Bot API

    wikipedia - Wikipedia content access

    numexpr - Fast and safe numerical evaluation

    python-dotenv - Environment variable management


## Contributing

1. Fork the repository

2. Create a feature branch

3. Make your changes

4. Test thoroughly

5. Submit a pull request