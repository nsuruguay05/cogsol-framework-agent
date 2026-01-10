from cogsol.content import BaseRetrieval
from data.CogsolFrameworkDocs import CogsolFrameworkDocsTopic
from data.CogsolAPIsDocs import CogsolAPIsDocsTopic

class CogsolFrameworkDocsRetrieval(BaseRetrieval):
    """Sample retrieval configuration."""

    name = "cogsol_framework_docs_search"
    topic = CogsolFrameworkDocsTopic
    num_refs = 5
    formatters = []

class CogsolAPIsDocsRetrieval(BaseRetrieval):
    """Sample retrieval configuration."""

    name = "cogsol_apis_docs_search"
    topic = CogsolAPIsDocsTopic
    num_refs = 5
    formatters = []
