import gradio as gr
from transformers import pipeline
from bear_core import bear_reply

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    max_new_tokens=120,
    temperature=0.7,
    top_p=0.9
)

def chat_fn(message, history):
    history = history or []

    # Build B.E.A.R.'s personality prompt
    prompt = bear_reply(message)

    # Generate model output
    output = generator(prompt)[0]["generated_text"]

    # Extract only the model's reply after "B.E.A.R.:"
    if "B.E.A.R.:" in output:
        reply = output.split("B.E.A.R.:")[-1].strip()
    else:
        reply = output.strip()

    history.append((message, reply))
    return history, history

with gr.Blocks(title="B.E.A.R. - Adaptive AI") as demo:
    gr.Markdown("# B.E.A.R.")
    gr.Markdown("Your adaptive AI companion.")

    chatbox = gr.Chatbot(label="Chat with B.E.A.R.")
    msg = gr.Textbox(label="Say something")

    msg.submit(chat_fn, [msg, chatbox], [chatbox, chatbox])

demo.launch()
