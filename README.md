# AggriBuddy — AI Agent for Smart Farming Advice

<div align="center">

> *Bridging the digital gap for small and marginal farmers through AI-powered, multilingual agricultural guidance*

[![IBM Watsonx](https://img.shields.io/badge/IBM-Watsonx.ai-054ADA?logo=ibm&logoColor=white)](https://www.ibm.com/products/watsonx-ai)
[![IBM Granite](https://img.shields.io/badge/IBM-Granite%20LLM-1F70C1?logo=ibm&logoColor=white)](https://www.ibm.com/granite)
[![RAG](https://img.shields.io/badge/RAG-LangChain-3B7EDE?logoColor=white)](https://www.langchain.com/)
[![NLP](https://img.shields.io/badge/NLP-Multilingual-4CAF50?logoColor=white)](https://www.ibm.com/products/watsonx-ai)
[![IBM Cloud](https://img.shields.io/badge/IBM-Cloud-054ADA?logo=ibm&logoColor=white)](https://cloud.ibm.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Internship](https://img.shields.io/badge/IBM%20SkillsBuild-Internship%202025-orange)](https://skillsbuild.org)

**[View Notebook](AggriBuddy_Standard_Notebook.ipynb)** &nbsp;|&nbsp; **[IBM Watsonx.ai](https://www.ibm.com/products/watsonx-ai)** &nbsp;|&nbsp; **[IBM SkillsBuild](https://skillsbuild.org)**

</div>

---

![AggriBuddy Banner](farmai.png)

---

## Overview

An AI-powered farming assistant designed to empower small and marginal farmers with real-time, localized, and personalized agricultural advice. Built using IBM Watsonx and Retrieval-Augmented Generation (RAG), this agent bridges the digital gap for farmers by offering support in regional languages for crop guidance, mandi prices, pest alerts, and more.

---

## Problem Statement

Many small-scale farmers struggle due to the lack of timely, accessible, and localized agricultural information. Challenges like unpredictable weather, limited pest knowledge, and poor market access are common. Language and literacy barriers further prevent informed decisions.

---

## Proposed Solution

AggriBuddy is an AI agent trained using IBM Watsonx.ai that delivers real-time, grounded agricultural advice. It supports queries in local languages and uses trusted sources to provide region-specific responses on crops, weather, mandi rates, soil, and pest control.

**Example:** A farmer asks *"Which crop is best in August in Kolhapur?"* — AggriBuddy fetches region-specific seasonal data from the Vector Index, processes it through IBM Granite, and responds in simple, clear language.

---

## System Architecture

```
Farmer Query (local language)
        │
        ▼
┌──────────────────────────────┐
│     IBM Watsonx.ai Studio    │
│                              │
│  ┌────────────────────────┐  │
│  │    IBM Granite LLM     │  │
│  │   (NLP Processing)     │  │
│  └───────────┬────────────┘  │
│              │               │
│  ┌───────────▼────────────┐  │
│  │  Watsonx Vector Index  │  │
│  │       (RAG)            │  │
│  │  ┌──────────────────┐  │  │
│  │  │  Agri PDFs       │  │  │
│  │  │  Mandi Data      │  │  │
│  │  │  Pest Docs       │  │  │
│  │  └──────────────────┘  │  │
│  └───────────┬────────────┘  │
└──────────────┼───────────────┘
               │
               ▼
   Grounded Response (local language)
               │
               ▼
           Farmer
```

---

## Technologies Used

| Category | Technology |
|---|---|
| **AI Platform** | IBM Watsonx.ai Studio |
| **Foundation Model** | IBM Granite LLM |
| **RAG Framework** | Retrieval-Augmented Generation + LangChain |
| **Vector Store** | Watsonx Vector Index |
| **NLP** | Natural Language Processing — multilingual |
| **Storage** | IBM Cloud Object Storage |
| **Knowledge Base** | Agricultural PDFs, mandi price datasets |
| **Notebook** | Jupyter Notebook |
| **Deployment** | Watsonx Web UI + REST API |

---

## IBM Cloud Services Used

- Watsonx.ai Studio
- IBM Granite LLM
- IBM Cloud Lite Account
- Watsonx Vector Index
- IBM Cloud IAM
- IBM Cloud Object Storage

---

## Key Features

| Feature | Description |
|---|---|
| Multilingual support | Handles queries in local Indian languages |
| Crop recommendations | Season and region-specific advice |
| Pest & disease alerts | Grounded in trusted agricultural datasets |
| Mandi price updates | Daily market rates from official sources |
| RAG-powered answers | Document-grounded — no hallucination |
| Off-topic redirection | Keeps the agent focused on agriculture |
| API deployment | REST API available post-deployment |

---

## WOW Factors

- Multilingual support for local farmer queries
- Personalized crop recommendations by season and region
- Pest and disease alerts from trusted datasets
- Daily mandi prices from official sources
- Real-time soil, weather, and crop updates
- Grounded answers via RAG-powered Vector Index — no hallucination

---

## How It Works

1. Farmer asks a query (e.g., *"Which crop is best in August in Kolhapur?"*)
2. IBM Granite model processes the natural language query
3. Watsonx Vector Index fetches grounded info from uploaded agricultural documents
4. Agent responds in simple language, optionally in local dialect

---

## Screenshots

### Setting Up the Agent
![Setting Up the Agent](msetting%20up.png)

### Agent Instructions
![Agent Instructions](agent_instruction.png)

### Tools Used & Testing
![Tools used & Testing](otool_testing.png)

### Deployment & Preview
![Deployment & Preview](Deployment_preview.png)

### API References after Deployment
![API References after Deployment](API.png)

### Resources List
![Resources List](resource_list.png)

---

## How to Run / Deploy

### Prerequisites
- IBM Cloud account (Lite tier works)
- Access to IBM Watsonx.ai Studio
- Agricultural PDF documents for the knowledge base

### Deployment Steps

```
1. Log in to IBM Cloud → https://cloud.ibm.com
2. Launch Watsonx.ai Studio
3. Create a new AI Agent project
4. Upload agricultural PDFs to IBM Cloud Object Storage
5. Create a Watsonx Vector Index and connect the PDFs
6. Configure IBM Granite as the foundation model
7. Set agent instructions and multilingual prompts
8. Add intent redirection for off-topic queries
9. Test in the Watsonx preview panel
10. Deploy via Web UI, Streamlit, or embed code
```

### API Usage (after deployment)

```python
import requests

url = "YOUR_WATSONX_AGENT_API_ENDPOINT"
headers = {
    "Authorization": "Bearer YOUR_IBM_CLOUD_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "input": "Which crop should I grow in August in Kolhapur?",
    "parameters": {"max_new_tokens": 300}
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

---

## End Users

- Small and marginal farmers across India
- Agricultural cooperatives and Farmer Producer Organizations (FPOs)
- Government Krishi Kendras and extension workers
- Rural Extension Officers
- NGOs and AgriTech startups

---

## Results

| Metric | Result |
|---|---|
| Answer grounding | RAG-based — sourced from uploaded documents |
| Languages supported | English + regional Indian languages |
| Off-topic redirection | Configured — agent stays agriculture-focused |
| Deployment mode | Web UI + REST API |
| Knowledge base | Agricultural PDFs + mandi price datasets |
| Foundation model | IBM Granite (IBM Watsonx.ai) |

---

## Certifications & IBM Badges

Built during the IBM SkillsBuild Academic Internship 2025. The following IBM-verified certifications were completed in support of this project:

| Certificate | Issued By | Date | Verify |
|---|---|---|---|
| Code Generation and Optimization Using IBM Granite | IBM SkillsBuild | Jul 21, 2025 | [Credly](https://www.credly.com/badges/7b822ea0-6920-497a-a05c-a18388a7776d) |
| Getting Started with Artificial Intelligence | IBM SkillsBuild | Jul 15, 2025 | [Credly](https://www.credly.com/badges/2a461ee3-0a93-4a93-a39d-dc80f91ebd4e) |
| Journey to Cloud: Envisioning Your Solution | IBM SkillsBuild | Jul 18, 2025 | [Credly](https://www.credly.com/badges/23bb5565-78d0-4eb8-95fc-a9bb8a384686) |
| Lab: Retrieval Augmented Generation with LangChain | IBM SkillsBuild | Jul 16, 2025 | Completion Verified |
| Large Language Model Basics | IBM SkillsBuild | Jul 15, 2025 | Completion Verified |
| Mastering the Art of Prompting | IBM SkillsBuild | Jul 15, 2025 | Completion Verified |
| Introduction to Artificial Intelligence | IBM SkillsBuild | Jul 15, 2025 | Completion Verified |

---

## Future Scope

- Crop disease detection with image processing and computer vision
- Livestock health advisory system
- Offline access for remote areas with poor connectivity
- Voice assistant in local dialects (Hindi, Marathi, Kannada)
- Financial and crop insurance advisory integration
- IoT farm sensor data integration for real-time soil and climate monitoring

---

## Useful Links

- [IBM Cloud Lite](https://cloud.ibm.com)
- [IBM Watsonx.ai](https://www.ibm.com/products/watsonx)
- [IBM Granite Models](https://www.ibm.com/granite)
- [IBM SkillsBuild](https://skillsbuild.org)
- [LangChain RAG Docs](https://python.langchain.com/docs/use_cases/question_answering/)

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Created By

**Shubham Dattatray Potdar**
B.Tech — Computer Science & Engineering
D. Y. Patil College of Engineering and Technology, Kolhapur

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shubham%20Potdar-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shubhampotdar07x)
[![GitHub](https://img.shields.io/badge/GitHub-Shubh07x-181717?logo=github&logoColor=white)](https://github.com/Shubh07x)
[![Email](https://img.shields.io/badge/Email-shubhampotdar8878%40gmail.com-EA4335?logo=gmail&logoColor=white)](mailto:shubhampotdar8878@gmail.com)

---

<div align="center">

*Created with during the IBM SkillsBuild Academic Internship 2025*

**If this project helped you, please consider giving it a ⭐ on GitHub.**

</div>
