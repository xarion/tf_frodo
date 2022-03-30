## FRODO: Free rejection of Out-of-distribution samples

use FRODO simply by

```
import model
from tf_frodo import FRODO

model_with_frodo = FRODO(model).fit(x_validation) 

results = model_with_frodo.predict(x_test)

assert results["model_outputs"] == model(x_test)
results["FRODO"] # Rejection scores for each sample in x_test
```