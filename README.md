# Data Engineering Project - Spotify API Pipeline to AWS S3, Athena and Glue

## Overview
This project is a data pipeline that extracts information from the Spotify API, transforms the data from JSON to Parquet format, stores it in Amazon S3, and runs queries using Amazon Athena. The pipeline is designed to be scalable and efficient, utilizing an AWS Glue crawler to catalog the data automatically.

## Project Objectives
- Data Extraction: Fetch data from the Spotify API, including playlists, tracks, artists, and albums.
  
- Data Transformation: Convert the data from JSON to Parquet format for optimized queries and storage.
  
- Storage in S3: Store the transformed data in Amazon S3 in a well-organized structure.

- Athena Queries: Perform efficient queries using Amazon Athena after the data is cataloged by AWS Glue.

## Pipeline Structure

1. #### Data Extraction

   - The Spotify API is used to gather data such as playlists, artist information, albums, and songs.

   - The data is returned in JSON format and processed in batches.
  
2. #### Data Transformation

   - The JSON data is converted to Parquet format using libraries like pyarrow.
 
   - Parquet is preferred for its efficiency in storage and query optimization for large datasets.

3. #### Storage in S3

   - After transformation, the Parquet files are uploaded to an Amazon S3 bucket, organized by date and data type.

   - The folder structure follows a partition format for easier querying: s3://<bucket-name>/spotify_data/{data_type}/{year}/{month}/{day}/.

4. #### Cataloging with AWS Glue

   - An AWS Glue Crawler is configured to automatically detect and catalog the data in S3, creating tables in the Data Catalog to facilitate querying in Athena.

5. #### Athena Queries

   - Using Amazon Athena, the data stored in S3 is queried directly. With the Glue catalog, SQL queries can be run to perform analysis and reporting.

## Technologies Used
- Spotify API;
- Python;
- AWS S3;
- AWS Glue;
- Amazon Athena;
- Parquet;

## Prerequisites
Before running the project, make sure you have the following dependencies:

- Python 3.8+
- Spotify API Key: You will need this to authenticate requests to the Spotify API.
- AWS Account with permissions to use S3, Glue, and Athena.
- Poetry: Install Poetry for dependency management.

## Installing Poetry
You can install Poetry using the following command:

    curl -sSL https://install.python-poetry.org | python3

    git clone https://github.com/your-username/spotify-etl-project.git

For more details, see the official Poetry documentation.

## Installation
1. Clone the project repository:

        git clone https://github.com/your-username/spotify-etl-project.git

        cd spotify-etl-project

2. Install the dependencies using Poetry:

        poetry install

3. Activate the virtual environment created by Poetry:

        poetry run python scr.py

4. Configure your AWS credentials:


        AWS_ACCESS_KEY_ID=<your-access-key>
    
        AWS_SECRET_ACCESS_KEY=<your-secret-key>

        CLIENT_ID=<your-client-id>

        CLIENT_SECRET=<your-clientt-secret>

## Running the Pipeline
    poetry run python scr.py

## Project Structure
```
├── etl_parquet_athena_glue/
│   ├── __pycache__
│   ├── __init__.py
│   ├── extract.py
│   ├── src.py
│   ├── transform.py
├── output_files/
├── tests/
│   ├── __init__.py
├── .env
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
