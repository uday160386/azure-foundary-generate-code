import os
from openai import AzureOpenAI
from dotenv import load_dotenv


def main(): 
        
    try: 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_modelname = os.getenv("AZURE_MODEL_NAME")
        
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        endpoint = azure_oai_endpoint
        model_name = azure_oai_modelname
        deployment = azure_oai_deployment

        subscription_key = azure_oai_key
        api_version = "2024-12-01-preview"

        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=subscription_key,
        )

       # Get the prompt
        text = input('\nEnter a question:\n')

        response = client.chat.completions.create(
            stream=True,
            messages=[
                {
                    "role": "system",
                    "content": "I'm a helpful assistant to generate Java code.",
                },
                {
                    "role": "user",
                    "content": text,
                }
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model=deployment,
        )

        for update in response:
            if update.choices:
                print(update.choices[0].delta.content or "", end="")

        client.close()
    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()