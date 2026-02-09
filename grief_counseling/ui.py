"""Gradio UI for grief_counseling."""

import gradio as gr
from loguru import logger

from grief_counseling.core import Config, process_config


def create_app() -> gr.Blocks:
    """Create and configure Gradio app."""
    app = gr.Blocks(title="My App")
    with app:
        gr.Markdown("# My App")
        gr.Markdown("A modern Python application with Gradio UI")

        with gr.Row():
            app_name = gr.Textbox(
                label="App Name",
                placeholder="Enter app name",
                value="my-awesome-app",
            )
            debug_mode = gr.Checkbox(label="Debug Mode", value=False)

        submit_btn = gr.Button("Process", variant="primary")
        output = gr.Textbox(label="Result", interactive=False)

        def process(name: str, debug: bool) -> str:
            """Process the config."""
            logger.info(f"Processing: {name}, debug={debug}")
            config = Config(name=name, debug=debug)
            result = process_config(config)
            return result

        submit_btn.click(
            fn=process,
            inputs=[app_name, debug_mode],
            outputs=output,
        )

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
