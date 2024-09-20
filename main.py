import gradio as gr

def count_letters(text: str) -> int:
    """Counts the number of letters in a given name."""
    return len(text)

interface = gr.Interface(
    fn=count_letters,
    inputs=gr.Textbox(label="Text"),
    outputs=gr.Textbox(label="Total Charsacters"),
)

if __name__ == "__main__":
    interface.launch()    
    
    