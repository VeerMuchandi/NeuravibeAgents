# Phone Plan Shopper A2A tester

## Review the code

See how the RemoteA2AAgent is defined in `agent.py` and how the agent_card is dynamically accessed from the running agent. 
`AGENT_CARD_WELL_KNOWN_PATH` is currently `.well-known/agent-card` and use it the way it is set.

```
phone_plan_shopper_agent = RemoteA2aAgent(
    name="phone_plan_shopper_agent",
    description="Agent that helps shop for EPP discounted phone plans an devices.",
    agent_card=(
        f"http://localhost:8001/a2a/phoneplan_shopper{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)
```

## Steps to test

1. Set up your python virtual environment

2. Install google-adk 
```
pip install google-adk
```
3. Go one directory level above to ensure that you are in the folder where both phoneplan_a2a_tester and phoneplan_shopper are there
```
cd ..
```

4. **Running A2A Agent:** 
From terminal run
```
adk api_server --a2a --port 8001 .
```
This will find the a2a agents in the structure and start them locally i.e., it will discover phoneplan_shopper
**Note**: You should be in the parent folder to run this command and not give the folder name for `phoneplan_shopper`.

**Note** Look at the agent card or `agent.json` file in the phoneplan_shopper folder. The URL is set to 

```
"url": "http://localhost:8001/a2a/phoneplan_shopper",
```
The part after a2a should match the name of the folder which may not match with the agent_name!

If the A2A agent is successfully discovered and is running you will see messages like these. If you don't see Agent Executor messages, something went wrong!
```
025-09-26 17:39:34,561 - INFO - fast_api.py:358 - Setting up A2A agent: phoneplan_shopper
/usr/local/google/home/veermuchandi/code/agents/NeuravibeAgents/phone_venv/lib/python3.11/site-packages/google/adk/cli/fast_api.py:361: UserWarning: [EXPERIMENTAL] A2aAgentExecutor: ADK Implementation for A2A support (A2aAgentExecutor, RemoteA2aAgent and corresponding supporting components etc.) is in experimental mode and is subjected to breaking changes. A2A protocol and SDK arethemselves not experimental. Once it's stable enough the experimental mode will be removed. Your feedback is welcome.
  agent_executor = A2aAgentExecutor(
/usr/local/google/home/veermuchandi/code/agents/NeuravibeAgents/phone_venv/lib/python3.11/site-packages/google/adk/a2a/executor/a2a_agent_executor.py:95: UserWarning: [EXPERIMENTAL] A2aAgentExecutorConfig: ADK Implementation for A2A support (A2aAgentExecutor, RemoteA2aAgent and corresponding supporting components etc.) is in experimental mode and is subjected to breaking changes. A2A protocol and SDK arethemselves not experimental. Once it's stable enough the experimental mode will be removed. Your feedback is welcome.
  self._config = config or A2aAgentExecutorConfig()
2025-09-26 17:39:34,562 - INFO - fast_api.py:386 - Successfully configured A2A agent: phoneplan_shopper
```

6. Open another terminal and run
```
adk web
```

7. Select `phoneplan_a2a_tester` from the adk web user interface and test.





