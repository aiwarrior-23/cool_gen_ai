from services.agent_manager import create_group_chat
from services.topic_generator import topics_generator
import json

def initiate_chat(problem):
    manager = create_group_chat()
    topics_generator.initiate_chat(manager, message=problem)

    last_message = topics_generator.last_message()["content"].replace("TERMINATE", "").strip()
    return json.loads(last_message)
