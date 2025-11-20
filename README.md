# Explainable AI Toolkit for Scientific Data

This project demonstrates a lightweight framework for:
- Knowledge Graph construction
- Symbolic reasoning
- Causal explanation of events
- Natural language summarization
- A REST API for explainability

It aims to show skills relevant to research internships in AI, 
Explainable AI (XAI), Knowledge Graphs, and symbolic reasoning 
(Inria BOREAL, Coconut, EDF LLM, TALN Antilles...).

---

##  Concepts covered

###  Knowledge Graphs
Graph integration of heterogeneous data (sensors, events, causes).
Using Python + NetworkX.

###  Symbolic AI & Reasoning
Shortest-path explanation of causal chains.
Root cause analysis for scientific events.

###  Natural Language Processing (NLP)
Simple text generation for event summarization.

###  API Development
FastAPI server exposing:
- `/neighbors/{id}`
- `/explain/{event_id}`
- `/summary/{event_id}`

---

##  Project Architecture

explainable-ai-toolkit/
├── data/
├── kg/
├── reasoning/
├── nlp/
└── api/


##  How to run

pip install -r requirements.txt
uvicorn api.api:app --reload

Copier le code
http://localhost:8000/explain/Event2



##  Purpose

This mini-project demonstrates abilities in:

- Data modeling & knowledge representation  
- Reasoning & explainability  
- Python architecture  
- NLP  
- Scientific data processing  
- Research-oriented problem solving  

It fits **100%** the expectations of research teams working on 
Explainable AI, Knowledge Graphs, Reasoning, NLP, or XAI.