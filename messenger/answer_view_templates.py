import json

def quick_reply(client_id,text, buttons):
    data = json.dumps({
        "recipient": {
            "id": client_id
        },
        "message": {
            "text": text,
            "quick_replies": __formatQuickReplies(buttons)
        }
    })

    return data

def __formatQuickReplies(buttons): #[(title1, image_url1), ..., title11]
    qr = []
    for b in buttons:
        if type(b) is tuple:
            title, image_url = b
            qr += [{"content_type":"text","title":title,"payload":title,"image_url":image_url}]
        else:
            qr += [{"content_type": "text", "title": b, "payload": b}]
    return qr


def text(client_id, text):
	return json.dumps({
        "recipient": {
            "id": client_id
        },
        "message": {
            "text": text
        }
    })

def textPublish(client_id, text):
	return json.dumps({
        "recipient": {
            "id": client_id
        },
        "message": {
            "text": text
        },
        "tag": "NON_PROMOTIONAL_SUBSCRIPTION"
    })


def typing_on(client_id):
    return json.dumps({
        "recipient": {
            "id": client_id
        },
        "sender_action": "typing_on"
    })

def mark_seen(client_id):
    return json.dumps({
        "recipient": {
            "id": client_id
        },
        "sender_action": "mark_seen"
    })