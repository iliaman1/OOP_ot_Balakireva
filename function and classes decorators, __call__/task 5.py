class RenderList:
    def __init__(self, tag):
        self.tag = tag if tag in ('ul', 'ol') else 'ul'

    def __call__(self, *args, **kwargs):
        return '\n'.join([f'<{self.tag}>', *map(lambda x: f"<li>{x}</li>", args[0]), f'</{self.tag}>'])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)