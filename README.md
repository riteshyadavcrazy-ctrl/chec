---
title: Save Restricted Content Bot V3
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
license: agpl-3.0
---

# Save Restricted Content Bot v3

Telegram bot for saving Telegram post content and downloading media from supported links.

## Deploy on Hugging Face Spaces

1. Create a new Hugging Face Space.
2. Select **Docker** as the SDK.
3. Upload/push this project to the Space root.
4. Add the required secrets in **Settings → Variables and secrets**.

## Required environment variables

- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `MONGO_DB`
- `OWNER_ID`
- `LOG_GROUP`

## Optional environment variables

- `DB_NAME`
- `STRING`
- `MASTER_KEY`
- `IV_KEY`
- `YT_COOKIES`
- `INSTA_COOKIES`
- `FREEMIUM_LIMIT`
- `PREMIUM_LIMIT`

## Local run

```bash
pip install -r requirements.txt
python3 main.py
```

## Notes

For private Telegram channels or groups, the logged-in user session must already be a member of the chat. Use `/login` before fetching private content.
