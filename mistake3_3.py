from typing import Callable

TextProcessor = Callable[[str], str]

def strip_processor(text: str) -> str:
    return text.strip()
def uppercase_processor(text: str) -> str:
    return text.upper()
def add_watermark_processor(text: str) -> str:
    t = text + " [Bản quyền: Uyên]"
    return t

class ArticleProcessor:
    def __init__(self, processors: list[TextProcessor] = None):
        self.processors = processors or []
    def processor(self, base_text: str) -> str:
        final_text = base_text
        #Pipeline
        for step in self.processors:
            final_text = step(final_text)
        return final_text

if __name__ == "__main__":
    article = ArticleProcessor(processors=[uppercase_processor, add_watermark_processor])
    print(article.processor("ấn phẩm Chuyến tàu đến Paris"))