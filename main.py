from happytransformer import HappyTextToText, TTSettings
import gradio as gr

happy_tt = HappyTextToText("T5", "t5-small")

translation_settings = TTSettings(do_sample=False, max_length=100)

def translate_english_to_french(text):
    """
    Translate text from English to French using the HappyTextToText model.
    """
    input_text = f"translate English to French: {text}"
    result = happy_tt.generate_text(input_text, args=translation_settings)
    return result.text


def gradio_ui():
    """
    Create a Gradio interface for English to French translation.
    """
    interface = gr.Interface(
        fn=translate_english_to_french,
        inputs="text",
        outputs="text",
        title="English to French Translator",
        description="Enter an English sentence, and it will be translated to French."
    )
    return interface

if __name__ == "__main__":
    app = gradio_ui()
    app.launch(share=True)
