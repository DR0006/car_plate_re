# car_plate_re

����ʶ��

**Fxx**

--------------------------------

- opencv-python (>3.3)
- onnxruntime (>1.8.1)
- fastapi (0.92.0)
- uvicorn (0.20.0)
- loguru (0.6.0)
- python-multipart 
- tqdm 
- requests

> ��onnxruntime�汾���µ�ʱ���ҷ������б���,������װ����1.8.1

```bash
raise ValueError(
ValueError: This ORT build has ['AzureExecutionProvider', 'CPUExecutionProvider'] enabled. Since ORT 1.9, you are
required to explicitly set the providers parameter when instantiating InferenceSession. For example,
onnxruntime.InferenceSession(..., providers=['AzureExecutionProvider', 'CPUExecutionProvider'], ...)
```