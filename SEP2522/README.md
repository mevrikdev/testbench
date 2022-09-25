# write a celery task to process log files from pre-defined dir

we will write a celery task to process log files and store the object into mongoDB 

## requirements 
- given you have list of text file paths
- read all files by line
- extract files by config format (json, delimited)
-- json format means each line will be json object 
-- delimited means each line will have fields separated by special character, such as "-" or ","
- parse each line into event object 
- store event object to mongodb collection 

## specifications 
- celery must process log files incrementally 
- use config arg to pass log file list and parsing format 


## resources
- create mongodb atlas account to storethe event object 
- attached json log file `access.log.zip`


## delivery
- provide detials to run the task 
- access to mongoDB collections 

