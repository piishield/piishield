import os
import gradio as gr

from piishield import PIIShield

def redact(audio):
    ps = PIIShield(input=audio)
    output_feature = ps.policies
    if ps.analysis['company_secret'] > 0:
        output_feature = ps.analysis
    return (str(os.path.join(os.path.dirname(__file__), "output/output.mka")), ps.redact_words, output_feature)

demo = gr.Interface(
    fn=redact,
    inputs=gr.Audio(source="microphone", type="filepath"),
    examples=[
        [os.path.join(os.path.dirname(__file__),"examples/Kids.m4a")],
        [os.path.join(os.path.dirname(__file__),"examples/Company.m4a")],
    ],
    outputs=[gr.Audio(), "text", "label"],
    title="PIIShield",
    description="Upload or record data which you wish to redact PII for!",
    allow_flagging="never"
)

demo.launch()

