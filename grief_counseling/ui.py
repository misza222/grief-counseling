"""Gradio UI for grief_counseling."""

import gradio as gr

from grief_counseling.utils.client import call_llm


def interact(message: str, history: list):
    """
    Main function - sends message to LLM without any system prompt.
    """
    if not message or not message.strip():
        return history, {"status": "No message"}, ""

    # Build messages from history (no system prompt!)
    messages = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    messages.append({"role": "user", "content": message})

    # Call LLM directly
    try:
        response_text = call_llm(messages)
    except Exception as e:
        error_msg = f"Error generating response: {str(e)}"
        print(f"ERROR: {error_msg}")
        return history, {"error": error_msg}, ""

    # Update history
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response_text})

    return history


def reset_conversation():
    """Resets conversation."""
    return []


def create_app() -> gr.Blocks:
    """Create and configure Gradio app."""
    app = gr.Blocks(title="Grief Counseling App")
    with app:
        gr.Markdown("# Grief Counseling App")
        gr.Markdown("Developer UI for testing core functionality and LLM integration.")

        with gr.Row(), gr.Column(scale=7):
            chatbot = gr.Chatbot(height=600, show_label=False)

            msg = gr.Textbox(placeholder="Message...", lines=2, show_label=False)

            with gr.Row():
                send_btn = gr.Button("Send", variant="primary", scale=3)
                clear_btn = gr.Button("Clear", variant="secondary", scale=1)

        # Event handlers
        send_btn.click(fn=interact, inputs=[msg, chatbot], outputs=[chatbot]).then(
            lambda: "", None, msg
        )

        msg.submit(fn=interact, inputs=[msg, chatbot], outputs=[chatbot]).then(
            lambda: "", None, msg
        )

        clear_btn.click(fn=reset_conversation, inputs=[], outputs=[chatbot])

    return app


def launch() -> None:
    """Launch the Gradio app."""
    app = create_app()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )


if __name__ == "__main__":
    launch()
