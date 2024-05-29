import autogen
from config import LLM_CONFIG

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

advanced_topic = autogen.AssistantAgent(
    name="AdvancedTopic",
    is_termination_msg=termination_msg,
    system_message="You read the json having an article written. Your job is to add a new key which talks about advanced topics related to the article. Give final response in the same JSON format and then reply with TERMINATE.  No escape sequences in the final json to be used.",
    llm_config=LLM_CONFIG,
    description="Adding a section on Advanced Topics",
)