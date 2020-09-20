import requests
vblink = input("Write Webhook Url:")
requests.delete(vblink)
print("Webhook Deleted.")
