import os
import openai
import gradio as gr

# openai.api_key = os.getenv("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")
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Construi mi propio Chat-GPT con juegos de azar y mujerzuelas, pregunta prro ..."

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", "AI:"]
    )

    return response.choices[0].text


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Mi Chat-GPT</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("Enviar")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)