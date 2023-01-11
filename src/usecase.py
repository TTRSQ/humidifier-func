import src.adapter.switchbot as bot


def set_plug_power(plug_id: str, on: bool):
    res = bot.request_bot_api(
        f"/v1.1/devices/{plug_id}/commands",
        bot.Method.POST,
        {
            "commandType": "command",
            "command": "turnOn" if on else "turnOff",
            "parameter": "default",
        },
    )
    return {
        "success": res["statusCode"] == 100,
        "message": res["message"],
    }


def get_plug_status(plug_id: str):
    res = bot.request_bot_api(
        f"/v1.1/devices/{plug_id}/status",
        bot.Method.GET,
    )
    return {
        "success": res["statusCode"] == 100,
        "message": res["message"],
        "on": res["body"]["power"] == "on",
        "voltage": res["body"]["voltage"],
        "weight": res["body"]["weight"],
    }


def send_remote_command(remote_id: str, btn_name: str):
    res = bot.request_bot_api(
        f"/v1.1/devices/{remote_id}/commands",
        bot.Method.POST,
        {
            "commandType": "customize",
            "command": btn_name,
            "parameter": "default",
        },
    )
    return {
        "success": res["statusCode"] == 100,
        "message": res["message"],
    }


def get_meter_status(meter_id: str):
    res = bot.request_bot_api(
        f"/v1.1/devices/{meter_id}/status",
        bot.Method.GET,
    )
    return {
        "success": res["statusCode"] == 100,
        "message": res["message"],
        "humidity": res["body"]["humidity"],
        "temperature": res["body"]["temperature"],
    }
