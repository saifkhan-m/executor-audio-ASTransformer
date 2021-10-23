# executor-audio-ASTransformer


## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://executor-audio-ASTransformer')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://executor-audio-ASTransformer')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
