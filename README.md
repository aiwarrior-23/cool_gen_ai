# Automated Technical Blog Article Generation Using Multiple Agents

This repository demonstrates how to use multiple agents to automate the creation of technical blog articles. The code utilizes several tools and techniques, including Autogen and Azure OpenAI services, to generate topics, write articles, and add examples and advanced topics. The process is managed by a `GroupChatManager`, which coordinates the interactions between different agents.

## Table of Contents
- [Importing Libraries](#importing-libraries)
- [API Configuration](#api-configuration)
- [Termination Message Function](#termination-message-function)
- [Defining Agents](#defining-agents)
- [Resetting Agents](#resetting-agents)
- [create_article Function](#create_article-function)
- [Generating Articles](#generating-articles)
- [Combining JSON Outputs](#combining-json-outputs)
- [Conclusion](#conclusion)
- [Complete Article](#complete-article)

## Importing Libraries

The code starts by importing necessary libraries.

## API Configuration

API keys and endpoints are specified for connecting to Azure OpenAI services. This configuration is necessary for the agents to communicate with the language models hosted on Azure.

## Termination Message Function

A helper function `termination_msg` is defined to determine if a message indicates the end of the process. This function checks if the message contains the keyword `TERMINATE`.

## Defining Agents

Four agents are defined using autogen’s `UserProxyAgent` and `AssistantAgent` classes. These are the agents that will coordinate with each other to give the final article.

- **topics_generator**: Generates topics for the articles. It coordinates with other agents to get the final article. The first agent that it submits the article to is the `article_writer`.
- **examples_adder**: Adds examples to the generated article. This receives the article in JSON format from `article_writer` agent and then adds more examples to it. Finally, it sends it to the `advanced_topic` agent.
- **advanced_topic**: Adds a section on advanced topics related to the article provided by `examples_adder` agent.
- **article_writer**: Writes the article based on the topics provided by the agent `topics_generator`. It writes the article and then converts it into a JSON format so that it can be rendered in the UI. Then the `examples_adder` agent is called.

## Resetting Agents

The `_reset_agents` function resets the state of all agents, clearing their history to ensure they start fresh for each new task.

## create_article Function

The `create_article` function initializes a group chat with the defined agents and manages the conversation flow to produce the desired article. It allows each agent to contribute to the article in a round-robin fashion.

The flow of agent is decided here. Also, it is ensured that the loop runs only 4 times so that the agents don’t start talking to each other indefinitely. Also, `max_auto_reply` is set to 1 so that each agent responds only once. We can tweak these for our respective problem statements.

## Generating Articles

A list of topics is defined, and for each topic, the `create_article` function is called to generate an article. The final JSON output for each topic is cleaned and appended to the `final_json` list.

## Combining JSON Outputs

The individual JSON outputs from all topics are combined into a single dictionary, which represents the final set of articles.

## Conclusion

This code provides a robust framework for automating the creation of technical blog articles using multiple agents. By leveraging the power of Azure OpenAI services and the autogen library, it demonstrates a scalable approach to content generation that can be customized and extended for various applications.

## Complete Article

You can read the complete article explaining the code at the link below:
- [Automating Article Writing with Multiple Agents](https://medium.com/@himanshuit3036/automating-article-writing-with-multiple-agents-78ea50e3cd47)
