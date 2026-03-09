# Project Description
This project designs a distributed batch-processing system for large-scale chess game analytics. 
It consolidates and normalizes chess game archives from multiple sources, including online play 
(Lichess PGN archives) and historical professional databases, in order to consolidate key information such as opening
frequencies correlation to skill rating.

## Setup:
To test the output of the repository, the pgn parsing package must be installed and a local sqlite database instance must be created.
To install the chess dependency, install the requirements using "pip install -r requirements.txt".
To create the local sqlite database, run "create_table.py".

## Environment Setup:
The data that will be aggregated comes from downloadable files, so there are no particular environment variables to consider other than storage. 
The lichess data can be downloaded from https://database.lichess.org/#standard_games; files can be up to 250GB when unzipped, so ample disk space must be available. 
A truncated version of the raw data is stored in the repository for example purposes.

## How To Run:
 To store the file data into the database, run "db_connect.py". The database will be stored under the **src/storage** folder, as chess_data.db. To test that the data has been stored, run "query_testing.py" and view the console output.

## Project Status:
Currently, the file acquisition, file parsing tools, and storage system are all functional. The schema of data storage is roughly defined, but will likely be adjusted before the final version. Likewise, the data acquisition works as of now, but will likely be optimized in the future.
Other functionality that must also be done: the ingested data must still be normalized and cleaned.