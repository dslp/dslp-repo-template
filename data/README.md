# Data Directories

The data directory is so that all project contributors maintain the same relative file paths for use of datasets in their development environments. 

**YOU SHOULD NOT COMMIT YOUR DATA TO THE REPO!**

You may optionally wish to commit small sample data files for quick debugging, but in general it's better to create scripts that generate or pull sample data into the development environment.

The folders are as follows.

## raw  

The original datasets pulled from a source system.

## interim  

Datasets created during the interim steps of a data pipeline. This folder is mostly for creating copies of interim datasets for debugging purposes.

## processed  

The output datasets from data pipelines. Generally used as the input to modeling.
