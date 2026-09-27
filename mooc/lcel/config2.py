import os
from langchain_core.runnables import RunnableLambda
from langchain_core.callbacks import BaseCallbackHandler


class MyCallbackHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized, inputs, **kwargs):
        print("Chain started with run_id:", kwargs.get("run_id"))
        print("Chain started with run_name:", kwargs.get("name"))

    def on_chain_end(self, outputs, **kwargs):
        print("Chain ended with run_id:", kwargs.get("run_id"))


def add_one(x: int, config: dict) -> int:
    print(f"add_one:{config}")

    return x + 1


runnable = RunnableLambda(add_one).with_config(run_name="AddOneRunnable")
callbacks = [MyCallbackHandler()]

print(runnable.invoke(1, config={
    'configurable': {
        'userId': 'id-1212',
        'status': ['up'],
    },
    'tags': ['tag11', 'tag2'],
    'metadata': {'key1': 'value1', 'key2': 'value2'},
    'callbacks': callbacks
}))