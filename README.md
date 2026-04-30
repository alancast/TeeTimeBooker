# 🏌️ Tee Time Booker

**This repo will be retired because I built [this one](https://github.com/wardcrazy01894/TeeTimeBooker) leveraging Claude.
It's much better. I could have done it here but it would ruin my commit history for my chart spelling.**

An automated Python bot that books tee times. For now starting with **Mangrove Bay Golf Club** (St. Petersburg, FL). Planning to be built with Playwright for reliable browser automation and AI agents for smart decision-making.

## Mangrove Bay

**Bookings open 7 days in advance at 6:00 AM** — this bot wakes up early, checks availability, and books my preferred slots. Mangrove Bay uses ForeUp for it's reservation system

---

## ✨ Features

For now these are planned features, nothing is set up yet.

- **Automatic booking** — Logs in, searches available tee times, and completes reservations.
- **Smart scheduling** — Runs daily around 5:55 AM with retries and backoff.
- **Dry-run mode** — Test safely without actually booking.
- **Robust error handling** — Screenshots, traces, and logs on failure.
- **Configurable preferences** — Players, time windows, walking/cart, course (Mangrove Bay main or Cypress Links).
- **Notifications** — Email, Discord, Telegram, or SMS when a tee time is booked (or on failure).
- **Headless & stealth** — Runs reliably without detection issues.
- **AI-powered intelligence** — Uses LLMs to evaluate and select the best available times based on your preferences (e.g., "closest to 8:30 AM for 4 players, prefer walking").

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Playwright** — Modern browser automation (more reliable than Selenium)
- **LangChain / CrewAI** (optional) — AI decision layer
- **APScheduler** or cron — Scheduling
- **Docker** (recommended for deployment)

---

## 📁 Project Structure

```bash
tee-time-booker/
├── src/
│   ├── __init__.py
│   ├── booking.py          # Core Playwright automation
│   ├── ai_agent.py         # LLM-powered tee time selection
│   ├── scheduler.py        # Daily job logic
│   ├── notifications.py    # Email/Discord/etc.
│   └── utils.py            # Helpers, logging, config
├── config/
│   └── settings.yaml       # Preferences (time windows, players, etc.)
├── .env.example            # Copy to .env
├── Dockerfile
├── requirements.txt
├── main.py                 # Entry point
├── README.md
└── .github/workflows/      # GitHub Actions (optional)
```
