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
        "content": "You are an SQL expert tasked with writing queries to retrieve data from the Epic EHR database. This tables contains details about patient visits, including appointment details, diagnoses, costs, and provider information.\n\nThe table schema is in attached markdown files -\nDateDim.md\nDepartmentDim.md\nPatientDim.md\nProviderDim.md\nTimeOfDayDim.md\nVisitFact.md\n\nEach column represents a specific attribute of the visit, such as the visit date, provider, diagnoses, or costs. Make sure all important joins are added in your query.\nYou can perform operations like selecting specific columns, applying filters, joining other tables (such as PatientDim, TimeOfDayDim, ProviderDim), and grouping or sorting the results. \nExample Natural Language Requests:\n\n\"Find all visits where the appointment was scheduled as a same-day appointment.\"\n\"Retrieve the visit key, appointment date, and provider details for visits that involved a face-to-face encounter.\"\n\"Get the total cost of visits for each department.\"\nTake a step-by-step approach in your response, cite sources and give reasoning before sharing final answer in t-sql format. for the following request:"
    },
    {
        "role": "user",
        "content": "Find all visits where the appointment was scheduled as a same-day appointment."
    },
    {
        "role": "assistant",
        "content": "To retrieve all visits where the appointment was scheduled as a same-day appointment, we will query the `VisitFact` table. The relevant column for identifying same-day appointments is `IsSameDayAppointment`, which returns 1 if the appointment was a same-day appointment.\n\n### Steps to Construct the Query:\n1. **Select Relevant Columns**: We will select the columns that provide useful information about the visits, such as `VisitKey`, `AppointmentDateKey`, and `PrimaryVisitProviderKey`.\n2. **Filter for Same-Day Appointments**: We will apply a filter to only include records where `IsSameDayAppointment` equals 1.\n3. **Join with Other Tables**: If needed, we can join with the `ProviderDim` table to get provider details, but for this query, we will focus on the `VisitFact` table.\n\n### SQL Query:\nHere’s the SQL query to achieve this:\n\n```sql\nSELECT \n    v.VisitKey,\n    v.AppointmentDateKey,\n    v.PrimaryVisitProviderKey\nFROM \n    VisitFact v\nWHERE \n    v.IsSameDayAppointment = 1;\n```\n\n### Explanation:\n- **SELECT**: We are selecting the `VisitKey`, `AppointmentDateKey`, and `PrimaryVisitProviderKey` from the `VisitFact` table.\n- **FROM**: We are querying the `VisitFact` table, aliased as `v`.\n- **WHERE**: We filter the results to include only those visits where `IsSameDayAppointment` is equal to 1, indicating that the appointment was scheduled as a same-day appointment.\n\nThis query will return all visits that were scheduled on the same day, providing a clear view of such appointments."
    },
    {
        "role": "user",
        "content": "Get the total cost of visits for each department"
    },
    {
        "role": "assistant",
        "content": "To retrieve the total cost of visits for each department, we will need to join the `VisitFact` table with the `DepartmentDim` table. The `VisitFact` table contains the cost information, while the `DepartmentDim` table provides the department details.\n\n### Steps to Construct the Query:\n1. **Select Relevant Columns**: We will select the department name and the total cost of visits.\n2. **Join Tables**: We will join the `VisitFact` table with the `DepartmentDim` table using the `DepartmentKey`.\n3. **Aggregate Costs**: We will use the `SUM` function to calculate the total cost for each department.\n4. **Group Results**: We will group the results by department to get the total cost per department.\n\n### SQL Query:\nHere’s the SQL query to achieve this:\n\n```sql\nSELECT \n    d.DepartmentName,\n    SUM(v.TotalCost) AS TotalVisitCost\nFROM \n    VisitFact v\nJOIN \n    DepartmentDim d ON v.DepartmentKey = d.DepartmentKey\nGROUP BY \n    d.DepartmentName;\n```\n\n### Explanation:\n- **SELECT**: We are selecting the `DepartmentName` from the `DepartmentDim` table and the total cost of visits calculated using `SUM(v.TotalCost)`.\n- **FROM**: We are querying the `VisitFact` table, aliased as `v`.\n- **JOIN**: We join the `DepartmentDim` table, aliased as `d`, on the `DepartmentKey` to link visits to their respective departments.\n- **GROUP BY**: We group the results by `DepartmentName` to aggregate the total costs for each department.\n\nThis query will return the total cost of visits for each department, providing a clear overview of the financials associated with each department's visits."
    },
    {
        "role": "user",
        "content": "Retrieve the visit key, appointment date, and provider details for visits that involved a face-to-face encounter."
    },
    {
        "role": "assistant",
        "content": "To retrieve the visit key, appointment date, and provider details for visits that involved a face-to-face encounter, we will query the `VisitFact` table and join it with the `ProviderDim` table to get the provider details. The relevant column in the `VisitFact` table to identify face-to-face encounters is `IsFaceToFace`, which returns 1 for such encounters.\n\n### Steps to Construct the Query:\n1. **Select Relevant Columns**: We will select the `VisitKey`, `AppointmentDateKey`, and provider details such as `PrimaryVisitProviderKey` and `ProviderName`.\n2. **Join Tables**: We will join the `VisitFact` table with the `ProviderDim` table using the `PrimaryVisitProviderKey`.\n3. **Filter for Face-to-Face Encounters**: We will apply a filter to include only records where `IsFaceToFace` equals 1.\n\n### SQL Query:\nHere’s the SQL query to achieve this:\n\n```sql\nSELECT \n    v.VisitKey,\n    v.AppointmentDateKey,\n    p.ProviderName\nFROM \n    VisitFact v\nJOIN \n    ProviderDim p ON v.PrimaryVisitProviderKey = p.ProviderKey\nWHERE \n    v.IsFaceToFace = 1;\n```\n\n### Explanation:\n- **SELECT**: We are selecting the `VisitKey`, `AppointmentDateKey`, and `ProviderName` from the respective tables.\n- **FROM**: We are querying the `VisitFact` table, aliased as `v`.\n- **JOIN**: We join the `ProviderDim` table, aliased as `p`, on the `PrimaryVisitProviderKey` to link visits to their respective providers.\n- **WHERE**: We filter the results to include only those visits where `IsFaceToFace` is equal to 1, indicating that the encounter was a face-to-face visit.\n\nThis query will return the visit key, appointment date, and provider details for all visits that involved a face-to-face encounter."
    }
],
    past_messages=10,
    max_tokens=800,
    temperature=0.15,
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
            "index_name": "uh-epic-data-dictionary",
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
            "role_information": "You are an SQL expert tasked with writing queries to retrieve data from the Epic EHR database. This tables contains details about patient visits, including appointment details, diagnoses, costs, and provider information.\n\nThe table schema is in attached markdown files -\nDateDim.md\nDepartmentDim.md\nPatientDim.md\nProviderDim.md\nTimeOfDayDim.md\nVisitFact.md\n\nEach column represents a specific attribute of the visit, such as the visit date, provider, diagnoses, or costs. Make sure all important joins are added in your query.\nYou can perform operations like selecting specific columns, applying filters, joining other tables (such as PatientDim, TimeOfDayDim, ProviderDim), and grouping or sorting the results. \nExample Natural Language Requests:\n\n\"Find all visits where the appointment was scheduled as a same-day appointment.\"\n\"Retrieve the visit key, appointment date, and provider details for visits that involved a face-to-face encounter.\"\n\"Get the total cost of visits for each department.\"\nTake a step-by-step approach in your response, cite sources and give reasoning before sharing final answer in t-sql format. for the following request:",
            "strictness": 3,
            "top_n_documents": 5
          }
        }]
    })

print(completion.to_json())