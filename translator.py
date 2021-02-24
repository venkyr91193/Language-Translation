import logging

from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

from .settings import language_code_dict


class Translator:
    __slots__ = ["model", "tokenizer"]

    def __init__(self):
        try:
            # using the latest model from facebook for many to many language translations
            model_name = "facebook/mbart-large-50-many-to-many-mmt"
            self.model = MBartForConditionalGeneration.from_pretrained(model_name)
            self.tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
        except Exception as e:
            logging.error(f"Error initializing model. {e}")

    def translate(
        self, sentence: str, source_language: str, dest_language: str
    ):
        try:
            self.tokenizer.src_lang = language_code_dict[source_language.lower().capitalize()]
            encoded_input = self.tokenizer(sentence, return_tensors="pt")
            generated_tokens = self.model.generate(
                **encoded_input,
                forced_bos_token_id=self.tokenizer.lang_code_to_id[
                    language_code_dict[dest_language.lower().capitalize()]
                ]
            )
            return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        except Exception as e:
            logging.error(f"Error translating. {e}")
