import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def extract_from_csv(file_to_process): 
	dataframe = pd.read_csv(file_to_process) 
	return dataframe 

