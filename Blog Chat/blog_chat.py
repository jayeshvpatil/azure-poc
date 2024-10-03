import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "https://ai-furtherai327136331691.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://uh-ai-poc.search.windows.net/")
search_key = os.getenv("SEARCH_KEY", "put your Azure AI Search admin key here")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint = endpoint,
    api_key = subscription_key,
    api_version = "2024-05-01-preview",
)

completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find helpful information from university hospitals blog. Keep your answers short and concise. Cite all the references. If you don't know the answer, politely reply to the user that you don't have the answer."
    },
    {
        "role": "user",
        "content": "Are intrusive thoughts harmful?"
    },
    {
        "role": "assistant",
        "content": "No, intrusive thoughts are not inherently harmful. According to Dr. Robert Chester, a clinical psychologist, although these thoughts can be unsettling, they do not necessarily indicate a mental illness or a hidden desire to act on them [doc1]. Multiple studies have shown that individuals who experience intrusive thoughts are not more likely to act on them [doc1]."
    },
    {
        "role": "user",
        "content": "Is virtual care covered by insurance?"
    },
    {
        "role": "assistant",
        "content": "Yes, many commercial insurance plans cover virtual urgent care visits or allow for submissions to a Health Savings Account (HSA) [doc4]. Initially, prior to the pandemic, insurance coverage for virtual care was limited, primarily to Medicare for rural patients under strict criteria [doc2]. However, the shift during the pandemic led to a broader acceptance and reimbursement for virtual visits, making it a permanent part of healthcare models now [doc2]. When scheduling a virtual visit, a bill will typically be submitted to your insurance company, and you may be responsible for a portion of the cost depending on your insurance plan [doc5]."
    },
    {
        "role": "user",
        "content": "Do I have covid or flu? How do I know?"
    },
    {
        "role": "assistant",
        "content": "To determine whether you have COVID-19 or the flu, consider the following:\n\n1. **Symptoms Overlap**: Both illnesses share symptoms like fever, cough, and fatigue, making it challenging to distinguish between them [doc2][doc3]. \n\n2. **Distinct Symptoms**: \n   - **Flu**: Often presents with more pronounced symptoms such as chills, headache, and body aches [doc2].\n   - **COVID-19**: May include symptoms like loss of taste or smell, though recent variants often cause milder, cold-like symptoms [doc2].\n\n3. **Testing**: An at-home rapid test for COVID-19 can help clarify your situation. If symptoms persist or worsen, consult a doctor for further testing, such as a PCR test, which is more reliable [doc2].\n\n4. **Risk Factors**: If you are at higher risk for complications (e.g., older adults or those with chronic conditions), knowing if you have COVID-19 is crucial due to potential antiviral treatments [doc2].\n\nIf you're uncertain, isolating yourself while symptomatic is advisable to prevent spreading any potential illness."
    }
],
    past_messages=10,
    max_tokens=16384,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "filter": None,
            "endpoint": f"{search_endpoint}",
            "index_name": "dynamic-iron-spgxjkjtz3",
            "semantic_configuration": "azureml-default",
            "authentication": {
              "type": "api_key",
              "key": f"{search_key}"
            },
            "embedding_dependency": {
              "type": "endpoint",
              "endpoint": "https://ai-furtherai327136331691.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-07-01-preview",
              "authentication": {
                "type": "api_key",
                "key": "95b0f27b1419415ca80d6caf87bee30b"
              }
            },
            "query_type": "vector_simple_hybrid",
            "in_scope": True,
            "role_information": "You are an AI assistant that helps people find helpful information from university hospitals blog. Keep your answers short and concise. Cite all the references. If you don't know the answer, politely reply to the user that you don't have the answer.",
            "strictness": 3,
            "top_n_documents": 5
          }
        }]
    })

print(completion.to_json())