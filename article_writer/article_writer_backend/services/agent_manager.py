import autogen
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from services.topic_generator import topics_generator
from services.article_writer import article_writer
from services.proof_reader import proof_reader
from services.examples_adder import examples_adder
from services.advanced_topic import advanced_topic
from config import LLM_CONFIG

def _reset_agents():
    topics_generator.reset()
    article_writer.reset()
    examples_adder.reset()
    advanced_topic.reset()
    topics_generator.clear_history()
    article_writer.clear_history()
    examples_adder.clear_history()
    advanced_topic.clear_history()

def create_group_chat():
    _reset_agents()
    groupchat = autogen.GroupChat(
        agents=[topics_generator, article_writer, examples_adder, advanced_topic],
        messages=[],
        max_round=4,
        speaker_selection_method="round_robin",
        allow_repeat_speaker=False,
        enable_clear_history=True
    )
    return autogen.GroupChatManager(groupchat=groupchat, llm_config=LLM_CONFIG, max_consecutive_auto_reply=1)
