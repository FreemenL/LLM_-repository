from modelscope.models.nlp.bert.configuration import BertConfig
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


# ModelScope's BERT config used by this model does not define these fields
# under newer transformers/PyTorch combinations, but the BERT backbone reads them.
_original_bert_config_init = BertConfig.__init__


def _patched_bert_config_init(self, *args, **kwargs):
    _original_bert_config_init(self, *args, **kwargs)
    self.is_decoder = getattr(self, "is_decoder", False)
    self.add_cross_attention = getattr(self, "add_cross_attention", False)


BertConfig.__init__ = _patched_bert_config_init

embeddings_path = "/Users/xiajiang/Desktop/huggingface/nlp_corom_sentence-embedding_chinese-base"

embedder = pipeline(
    Tasks.sentence_embedding,
    model=embeddings_path,
    model_revision="master",
    pipeline_name="sentence-embedding",
)

texts = [
    "你好，中国",
    "中国是个伟大的国家",
]

result = embedder(input={"source_sentence": texts})
vectors = result["text_embedding"].tolist()

for i, vector in enumerate(vectors):
    print(i, len(vector), vector)
