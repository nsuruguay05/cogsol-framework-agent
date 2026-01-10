from cogsol.tools import BaseRetrievalTool
from data.retrievals import CogsolAPIsDocsRetrieval, CogsolFrameworkDocsRetrieval

class CogsolFrameworkDocsSearch(BaseRetrievalTool):
    """Retrieval tool that queries a Content API retrieval."""

    name = "cogsol_framework_docs_search"
    description = "Search over all Cogsol Framework documentation."
    retrieval = CogsolFrameworkDocsRetrieval()

class CogsolAPIsDocsSearch(BaseRetrievalTool):
    """Retrieval tool that queries a Content API retrieval."""

    name = "cogsol_apis_docs_search"
    description = "Search over all Cogsol APIs documentation."
    retrieval = CogsolAPIsDocsRetrieval()