import src.switchbot as bot

devices = bot.request_bot_api("/v1.1/devices", bot.Method.GET)["body"]["deviceList"]
print(devices)
