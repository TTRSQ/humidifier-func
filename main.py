import functions_framework
import src.usecase as api
import os

plug_id = os.getenv("DEVICE_ID_PLUG")
meter_id = os.getenv("DEVICE_ID_METER")
humidifier_remote_id = os.getenv("REMOTE_ID_HUMIDIFIER")


@functions_framework.http
def hello_http(request):
    plug_status = api.get_plug_status(plug_id)
    if not plug_status["on"]:
        return "ok"

    is_humidifier_on = plug_status["weight"] > 10

    meter_status = api.get_meter_status(meter_id)

    if meter_status["humidity"] < 40 and not is_humidifier_on:
        api.send_remote_command(humidifier_remote_id, "電源")

    if meter_status["humidity"] >= 60 and is_humidifier_on:
        api.send_remote_command(humidifier_remote_id, "電源")

    return "ok"
