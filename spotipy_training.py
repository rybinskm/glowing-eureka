import os
import spotipy
import spotipy.util as util
'''
set SPOTIPY_CLIENT_ID = 'f338035f69974e14a61b0273c905c7f4'
set SPOTIPY_CLIENT_SECRET = 'd6e2aedf82624f99942d38ad6167d327t'
set SPOTIPY_REDIRECT_URI = 'www.google.pl'
'''
# client ID f338035f69974e14a61b0273c905c7f4

# client secret d6e2aedf82624f99942d38ad6167d327

# user ID: rybstonponte

os.environ['SPOTIPY_CLIENT_ID'] = 'f338035f69974e14a61b0273c905c7f4'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'd6e2aedf82624f99942d38ad6167d327t'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'

#username = input("Login:")
username = "rybstonponte"

token = util.prompt_for_user_token(username=username)

spotifyObject = spotipy.Spotify(auth=token)