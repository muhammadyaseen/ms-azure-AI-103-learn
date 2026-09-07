###
# Worflows are retiring on 01.12.2026
# Migration to Azure Agent SDK and code based workflows:
# https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow#migration-guide
# > Foundry is moving workflow authoring to a code-first model.

# Option 1: Microsoft Agent Framework
# Use Microsoft Agent Framework for most workflows. The orchestration you build visually 
# maps directly onto Agent Framework, which supports the same patterns through 
# declarative YAML or code-first authoring. In many cases, you can bring your 
# exported workflow YAML into an Agent Framework project and run it with minimal changes.

# Option 2: Azure Logic Apps
# If a visual designer is the main reason you use workflows, Azure Logic Apps gives 
# you a fully featured, low-code canvas for orchestration and can call Foundry agents 
# as steps. Azure Logic Apps lets you combine deterministic steps, including prebuilt 
# built-in actions, APIs, and MCP servers, with the probabilistic reasoning of Foundry 
# agents in the same run.

###

# Develop_Multi-Agent_Solution_with_Ms_Agent_Framework