# Using AWS Lambda and Amazon Comprehend for Sentiment Analysis

## Overview
This guide offers detailed steps to create and deploy an AWS Lambda function utilizing Amazon Comprehend for sentiment analysis. Learn how to set up AWS Lambda, configure permissions, and leverage Amazon Comprehend for sentiment analysis tasks.


![Drag Racing](/lambda-comprehend.png)


### AWS Services Overview
- **AWS Lambda:** A serverless compute service that allows running code without provisioning or managing servers.
- **Amazon Comprehend:** A natural language processing (NLP) service that uses machine learning to analyze text for insights such as sentiment analysis, language detection, and keyphrase extraction.





### 1. Create a Lambda Function

1. **Access Lambda Console:**
   - Log in to your AWS Management Console and navigate to the Lambda service.
   - Click on the "Create function" button.

2. **Choose Authoring Option:**
   - Select "Author from scratch" to create your Lambda function from the console.
   
3. **Configure Function:**
   - Enter a descriptive function name.
   - Choose the Python runtime for this Lambda function.
   - Optionally, set the execution role for the function.

4. **Code Writing/Upload:**
   - Write or upload your Python Lambda function code using the provided code editor.
   - Define the handler function, which AWS Lambda will invoke.

### 2. Add Permissions to Lambda Function

1. **Access Lambda Configuration:**
   - Navigate to the Lambda function page.
   - Go to the "Configuration" tab.

2. **Modify Permissions:**
   - Click on the "Permissions" tab within the Configuration section.
   - Locate and click on the execution role name. This action redirects you to the IAM Role associated with the Lambda function.

3. **Attach Policies:**
   - In the IAM Role permissions tab, click on the "Add permissions" dropdown.
   - Choose "Attach policies."
   - Use the search bar to find 'comprehend'.
   - Select the 'ComprehendReadOnly' policy.
   - Click the "Add permissions" button to attach the policy to the Lambda function's role.

### 3. Deploy and Run Code

1. **Finalize Deployment:**
   - Return to the Lambda function created earlier in the console.

2. **Deploy the Function:**
   - Click on the "Deploy" button to ensure the latest changes are saved and ready for execution.
