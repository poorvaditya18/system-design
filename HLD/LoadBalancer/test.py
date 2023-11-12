import requests


if __name__ == '__main__':

    heartbeat_url = 'http://localhost:3000/heartbeat'
    heartbeat_payload = {}
    heartbeat_payload["server_address"] = "127.0.0.1:3000"
    heartbeat_payload["request_type"] = "heartbeat"
    heartbeat_payload["data"] = {}
    response = requests.post(heartbeat_url,data=heartbeat_payload)
    print(response)