import os
from transform import process_json

from extract import SpotifyExtractor
from dotenv import load_dotenv


load_dotenv()

def main():

    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']
    playlist_id = os.environ['PLAYLIST_ID']

    extractor = SpotifyExtractor(client_id, client_secret, playlist_id)
    extractor.run()

    output_dir = '../output_files'
    json_file = os.path.join(output_dir, 'json_extract.json')

    bucket_name = os.environ['BUCKET_NAME']
    s3_key = os.environ['S3_KEY']

    process_json(json_file, output_dir, bucket_name, s3_key)


if __name__ == '__main__':
    main()