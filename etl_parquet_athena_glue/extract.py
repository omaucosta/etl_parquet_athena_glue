from dotenv import load_dotenv
from requests import post, get
import os
import base64
import json

load_dotenv()

class SpotifyExtractor:
    def __init__(self, client_id, client_secret, playlist_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.playlist_id = playlist_id
        self.token = None


    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

        url = 'https://accounts.spotify.com/api/token'
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}

        try:
            result = post(url, headers=headers, data=data)
            result.raise_for_status()
            json_result = result.json()
            self.token = json_result['access_token']
            return self.token
        except Exception as err:
            print(f"Error occurred: {err}")
        return None


    def get_auth_header(self):
        return {"Authorization": "Bearer " + self.token}


    def search_for_artist(self):
        if not self.token:
            print("Token not available. Call get_token() first.")
            return None

        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}"
        headers = self.get_auth_header()

        try:
            result = get(url, headers=headers)
            result.raise_for_status()
            json_result = result.json()
            print("Extracted JSON:", json_result)
            return json_result
        except Exception as e:
            print(f"Error fetching playlist: {e}")
            return None


    def save_json(self, json_extract):
        if not json_extract:
            print("No JSON data to save.")
            return

        data_folder = os.path.join(os.getcwd(), '../output_files')
        print(f"Saving to folder: {data_folder}")

        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, 'json_extract.json')

        try:
            with open(file_path, 'w') as f:
                json.dump(json_extract, f, indent=4)
            print(f'Saving file: {file_path}')

        except Exception as e:
            print(f"Error saving file: {e}")


    def run(self):
        self.get_token()
        if self.token:
            json_extract = self.search_for_artist()
            self.save_json(json_extract)
        else:
            print("Failed to retrieve token.")


if __name__ == '__main__':
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    playlist_id = os.environ['PLAYLIST_ID']

    extractor = SpotifyExtractor(client_id, client_secret, playlist_id)
    extractor.run()
