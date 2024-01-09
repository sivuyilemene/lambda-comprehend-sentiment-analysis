import json
import boto3

def lambda_handler(event, context):
    # initiating comprehend client
    comprehend = boto3.client(service_name='comprehend',region_name='us-east-1')
    
    text = """
    'This is a dangerous weather condition and its not over', New York City Mayor Eric Adams
    said on Friday morning, as New Yorkers struggle to commute amid roads and subway closures'
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