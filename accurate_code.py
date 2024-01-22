"""
This code sample shows Prebuilt Document operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://learn.microsoft.com/azure/applied-ai-services/form-recognizer/quickstarts/get-started-v3-sdk-rest-api?view=doc-intel-3.1.0&pivots=programming-language-python
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://chandru.cognitiveservices.azure.com/"
key = "3911240f36ba4665ac314260daf3fcb0"

# sample document
formUrl = "https://github.com/Chandrashekhar-ahana/Ingram/blob/main/IM20-08428-11-30ID23A0569446.pdf?raw=true"

document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", formUrl)
result = poller.result()

print("----Key-value pairs found in document----")

for kv_pair in result.key_value_pairs:
    
    if kv_pair.key.content=="INVOICE NUMBER" or kv_pair.key.content=="INVOICE DATE/TIME":
        print("Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
    
    else:
        print("Key '{}': Value:".format(kv_pair.key.content))
        
for pa in result.paragraphs:
    print(pa.content)

print("----------------------------------------")
