import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import json

from dotenv import load_dotenv

load_dotenv()

def process_json(
        json_file: str, 
        output_dir: str,
        bucket_name: str,
        s3_key: str) -> None:
    
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(json_file):
        raise FileNotFoundError(f"File not found: {json_file}")


    with open(json_file, 'r') as f:
        data = json.load(f)
    df = pd.json_normalize(data['tracks']['items'])


    parquet_file = os.path.join(output_dir, "spotfy_playlist.parquet")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file)


    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name=os.environ['AWS_REGION']
    )
    
    s3.upload_file(parquet_file, bucket_name, s3_key)
