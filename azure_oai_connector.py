import os

from promptflow.core import Prompty, AzureOpenAIModelConfiguration

AZURE_OPENAI_ENDPOINT="https://AOAI-ETL.openai.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT="Trial4o"
AZURE_OPENAI_API_KEY="c81b1674d1f84cccbbd858fa136f6405"
AZURE_OPENAI_API_VERSION="2024-02-15-preview"

model_config = AzureOpenAIModelConfiguration(
    azure_deployment=AZURE_OPENAI_CHAT_DEPLOYMENT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

prompty = Prompty.load("chat.prompty", model={'configuration': model_config})

# in_file_object  = open("m_Sample_Hackathon.xml", "r+")
# input_xml = in_file_object.read()

#print(result)

# oai_connector.py
def process_xml_data(xml_data):
    print("In aoi connector")
    # response = prompty(
    # # chat_history=[
    # #     {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
    # #     {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."}
    # # ],
    #     chat_input=xml_data)

    # Code to send XML data to Azure OpenAI and return the response
    ...
    response = {'message': 'response from Azure OAI json response'}
    return response
