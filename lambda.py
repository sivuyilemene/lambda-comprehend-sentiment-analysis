import json
import boto3

def lambda_handler(event, context):
    # initiating comprehend client
    comprehend = boto3.client(service_name='comprehend',region_name='us-east-1')
    
    text = """
    'FEEL GOOD | Cape Town officers lauded for helping deliver a 'beautiful, bouncing baby boy' on gravel road'
    """
    #calling sentiment method a parsing through the text
    comprehend_json_obj = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    
    # converting json comprehend object into a json string
    json_text = json.dumps(comprehend_json_obj, indent=4)
    # printing out the respone of the comprehend
    print("json_text:", json_text)
    
    #extracting the dominant sentiment
    sentiment = comprehend_json_obj['Sentiment']
    
    return f"sentiment: {sentiment}"