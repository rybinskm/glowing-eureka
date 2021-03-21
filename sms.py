from textmagic.rest import TextmagicRestClient

username = 'Rybston'
token = 'abcd1234'
client = TextmagicRestClient(username, token)

message = client.messages.create(phones='+48536548830', text='Hello :)')
