import socket
import json
from logic import validate_probabilities, roll_dice

s = socket.socket()
s.bind(("localhost", 8080))
s.listen(1)

print("start server...")

while True:
    c, addr = s.accept()
    req = c.recv(4096).decode()

    if "GET /roll_dice" in req:
        try:
            body = req.split("\r\n\r\n")[1]
            data = json.loads(body)

            p = data["probabilities"]
            n = data["number_of_random"]

            validate_probabilities(p)
            dices = roll_dice(p, n)

            res_data = {
                "status": "success",
                "dices": dices
            }

            res_json = json.dumps(res_data)

            res = "HTTP/1.1 200 OK\r\n"
            res += "Content-Type: application/json\r\n\r\n"
            res += res_json

        except Exception as e:
            res = "HTTP/1.1 400 Bad Request\r\n\r\n"
            res += str(e)
    else:
        res = "HTTP/1.1 404 Not Found\r\n\r\n"

    c.send(res.encode())
    c.close()