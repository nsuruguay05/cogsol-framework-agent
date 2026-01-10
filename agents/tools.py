from cogsol.tools import BaseTool, tool_params
#
# class ExampleTool(BaseTool):
#     description = "Demo tool that echoes the provided text."
#
#     @tool_params(
#         text={"description": "Text to echo", "type": "string", "required": True},
#         count={"description": "Times to repeat", "type": "integer", "required": False},
#     )
#     def run(self, chat=None, data=None, secrets=None, log=None, text: str = "", count: int = 1):
#         """
#         text: Text to echo back.
#         count: Times to repeat the text.
#         """
#         message = " ".join([text] * max(1, int(count)))
#         # chat/data/secrets/log are available per platform docs
#         response = message
#         return response
