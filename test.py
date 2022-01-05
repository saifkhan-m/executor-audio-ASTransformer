import os

from executor import ASTransformer_encoder
from jina import Document, DocumentArray

conf = ASTransformer_encoder(527,100)
#test_input = torch.rand([10, 100, 128])
#test_output = conf.model(test_input)
# output should be in shape [10, 527], i.e., 10 samples, each with prediction of 527 classes.
#print(test_output.shape)
dir = os.getcwd()
filename= os.path.join(dir,'data/sample.wav')
sound= Document()
sound.filename= 'filename'
doc = DocumentArray([Document(text=filename)])
doc = DocumentArray([Document(tags={'filename':filename} )])


conf.encode(doc)
for d in doc:
    print(d.embedding)