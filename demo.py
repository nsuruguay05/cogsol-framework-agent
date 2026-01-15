from agents.cogsolframeworkagent import CogsolFrameworkAgent
from data.retrievals import CogsolFrameworkDocsRetrieval

# Trying out the CogsolFrameworkAgent
agent = CogsolFrameworkAgent()
response = agent.run("How can I integrate Cogsol Framework into my application? Use a short line to answer in a funny way.")
print("First message response:")
print(response["messages"][-1]["content"])

print("\nNumber of messages in the conversation after second message:")
response = agent.run("Ha, funny :) -- Any fun ideas to use Cogsol Framework? Use a short line to answer in a funny way.")
print(len(response["messages"]))

print("\nNumber of messages in the conversation after reset:")
response = agent.run("Hi, have we talked before?", reset=True)
print(len(response["messages"]))
print("\nFirst message after reset:")
print(response["messages"][-1]["content"])

# Trying out the CogsolFrameworkDocsRetrieval
print("\nRetrieval results for 'How do I create a new topic?':\n")
retrieval = CogsolFrameworkDocsRetrieval()
results = retrieval.run("How do I create a new topic?")
for block in results["similar_blocks"]:
    print(f"- {block['source']}:\n\"{block['text'][:100].strip()}...\"\n")