1. Run rasa server locally : rasa run --enable-api -m models/20230427-234323-spatial-food.tar.gz

2. 
- Open the Discord developer portal and log into your account.
- Click on the New Application button to create a new app.
- Select Bot tab and then click on the Add Bot button to create a new bot.
- Change value of "BOT_TOKEN" in discord_dialog_connector.py to the value of newly generated token.

3. Run discord server with invited bot

4. Run discord_dialog_connector.py (Bot should come online at this point)

5. Talk with him ;)