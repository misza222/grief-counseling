from jinja2 import Environment, FileSystemLoader

from grief_counseling.config import Config


class Prompter:
    def __init__(self):
        self.template_env = Environment(
            loader=FileSystemLoader(
                [
                    Config.TEMPLATES_DIR,
                ]
            )
        )

    def build_system_prompt(self, core, template_filename="main.j2"):
        template = self.template_env.get_template(template_filename)
        prompt = template.render(core=core)

        return prompt
