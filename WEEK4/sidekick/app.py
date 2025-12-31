import gradio as gr
from sidekick import Sidekick

async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick