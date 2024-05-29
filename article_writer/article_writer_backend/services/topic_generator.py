import autogen
from config import LLM_CONFIG

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

topics_generator = autogen.UserProxyAgent(
    name="TopicsGenerator",
    human_input_mode="NEVER",
    code_execution_config=False,
    description="An Agent which generates topics for the article that it is asked to write",
)
