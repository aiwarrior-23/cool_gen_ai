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

## Importing Libraries

The code starts by importing necessary libraries:

```python
import chromadb
from typing_extensions import Annotated

import autogen
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent