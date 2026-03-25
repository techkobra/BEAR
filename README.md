🐻 B.E.A.R. — Adaptive Discord AI Companion
B.E.A.R. (Behavior‑Enhanced Adaptive Respondent) is a modular, personality‑driven Discord AI assistant built for natural conversation, voice interaction, and long‑term adaptability. Designed to feel like a smart friend rather than a generic bot, B.E.A.R. blends text, voice, memory, and custom logic into a single evolving companion.

✨ Features
Conversational AI — responds naturally to messages in real time

Voice Support — joins voice channels, listens, and speaks

Modular Architecture — clean separation of bot logic, personality, and utilities

Slash Commands — structured commands for quick actions

Memory‑Ready — designed to integrate long‑term user memory

Custom Personality Engine — adjustable tone, behavior, and style

Secure Token Handling — .env‑based secrets, never committed to GitHub

🧱 Project Structure
Code
BEAR/
│
├── bot.py              # Main Discord bot logic
├── bear_core.py        # Personality, memory, and behavior engine
├── requirements.txt    # Python dependencies
├── .env                # Secrets (not committed)
└── README.md           # This file
🚀 Setup
1. Clone the repository
Code
git clone https://github.com/techkobra/BEAR.git
cd BEAR
2. Install dependencies
Code
pip install -r requirements.txt
3. Create a .env file
Add your Discord bot token:

Code
DISCORD_TOKEN=your_token_here
4. Run B.E.A.R.
Code
python bot.py
🎙️ Voice Support
B.E.A.R. includes optional voice features powered by discord.py and PyNaCl.
This allows the bot to:

Join voice channels

Speak using TTS

Use voice activity mode

Handle audio streams

Voice features can be enabled or disabled depending on your deployment.

🛣️ Roadmap
Memory persistence

Web research tools

Personality presets

Voice conversation mode

Server‑specific configuration

Dashboard UI

🤝 Contributing
Pull requests are welcome.
For major changes, open an issue first to discuss what you’d like to modify.

📄 License
MIT License (optional)
