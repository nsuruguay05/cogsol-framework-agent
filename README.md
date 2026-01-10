# Cogsol Framework Agent

## Setup
- Install CogSol Framework from: https://github.com/Pyxis-Cognitive-Solutions/cogsol-framework
- Configure environment variables in `.env` (see `.env.example`).
- Migrate data app first: `python manage.py migrate data`.
- Migrate agents app next: `python manage.py migrate`.
- Ingest documents for Cogsol Framework Docs topic:
  
  `python manage.py ingest "Cogsol Framework Docs" ./data/CogsolFrameWorkDocs --pattern "*.txt" --ingestion-config CogsolFrameworkIngestionConfig`

- Ingest documents for Content API Models topic:

  `python manage.py ingest "Cogsol APIs Docs\Cognitive API Models" ./data/CogsolAPIsDocs/CognitiveModels --pattern "*.txt" --chunking "langchain"`
- Ingest documents for Cognitive API Models topic:

  `python manage.py ingest "Cogsol APIs Docs\Content API Models" ./data/CogsolAPIsDocs/ContentModels --pattern "*.txt" --chunking "langchain"`
- Ingest documents for Cogsol APIs Docs topic:

  `python manage.py ingest "Cogsol APIs Docs" ./data/CogsolAPIsDocs/cognitive.txt --chunking "langchain"`

  `python manage.py ingest "Cogsol APIs Docs" ./data/CogsolAPIsDocs/content.txt --chunking "langchain"`

## Running the Agent
- Start chat with the agent: `python manage.py chat --agent CogsolFrameworkAgent`.