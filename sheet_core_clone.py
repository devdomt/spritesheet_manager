
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('SpritePy-7989e7a6e86d.json', scope)

gc = gspread.authorize(credentials)

new_spritesheet = gc.create("nowy")
new_spritesheet.share('devdomtest@gmail.com', perm_type = 'user', role = 'writer')
