
from jina import Document, DocumentArray
import os
from jina import Flow
params={'total_labels': 50,
      'input_target_dim': 512,
      'dataset_mean_std': [-6.6268077, 5.358466],
      'model_path': '/home/dato6579/jobs/ast_exec/executor-audio-ASTransformer/pretrained_models/ast_esc50_best_model.pth'}
f = Flow().add(uses='jinahub://ASTransformer_encoder',uses_with=params, install_requirements=True, force=True)


filename = os.path.join(os.getcwd(), 'data/1-4211-A-12.wav')
doc = DocumentArray([Document(tags={'filename': filename})])

with f:
    responses = f.post(on='index', inputs=doc, return_results=True)
    print(responses[0].docs[0].embedding)