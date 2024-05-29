import autogen
from config import LLM_CONFIG

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

examples_adder = autogen.AssistantAgent(
    name="ExamplesAdder",
    is_termination_msg=termination_msg,
    system_message="You read the json having an article written. Your job is to add more examples in that json. Add a new key Examples and then add atleast 4 examples to it. No escape sequences in the final json to be used. ",
    llm_config=LLM_CONFIG,
    description="Adding more examples",
)