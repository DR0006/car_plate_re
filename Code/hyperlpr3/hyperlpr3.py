# �����Ҫ��ģ���������
from .config.settings import onnx_runtime_config as ort_cfg  # ���� ONNX ģ������
from .inference.pipeline import LPRMultiTaskPipeline  # ���복��ʶ��Ķ�����ܵ�
from .common.typedef import *  # ���볣�õ����Ͷ���
from os.path import join  # ��������ƴ���ļ�·���ĺ���
from .config.settings import _DEFAULT_FOLDER_  # ����Ĭ��ģ�������ļ���·��
from .config.configuration import initialization  # �����ʼ������

# ��ʼ�� HyperLPR3 ģ������
initialization()


# ���� LicensePlateCatcher �࣬���ڳ���ʶ��
class LicensePlateCatcher(object):

    # ���캯�������ڳ�ʼ������ʶ����
    def __init__(self,
                 inference: int = INFER_ONNX_RUNTIME,  # �ƶ�ģʽ��Ĭ��ʹ�� ONNX ����ʱ
                 folder: str = _DEFAULT_FOLDER_,  # ģ�ʹ洢�ļ���·����Ĭ��ΪĬ���ļ���
                 detect_level: int = DETECT_LEVEL_LOW,  # ���Ƽ�⼶��Ĭ��Ϊ�ͼ�
                 logger_level: int = 3,  # ��־��¼����Ĭ��Ϊ 3
                 full_result: bool = False):  # �Ƿ��ȡ������ʶ������Ĭ��Ϊ False

        # ����Ƿ�ѡ���� ONNX ����ʱ
        if inference == INFER_ONNX_RUNTIME:
            from hyperlpr3.inference.multitask_detect import MultiTaskDetectorORT  # ���복�Ƽ������
            from hyperlpr3.inference.recognition import PPRCNNRecognitionORT  # ���복��ʶ������
            from hyperlpr3.inference.classification import ClassificationORT  # ���복�Ʒ�������
            import onnxruntime as ort  # ���� ONNX ����ʱ��
            ort.set_default_logger_severity(logger_level)  # ���� ONNX ����ʱ����־����

            # ����ѡ��ĳ��Ƽ�⼶�𣬳�ʼ����Ӧ�ļ����ģ��
            if detect_level == DETECT_LEVEL_LOW:
                det = MultiTaskDetectorORT(join(folder, ort_cfg['det_model_path_320x']), input_size=(320, 320))
            elif detect_level == DETECT_LEVEL_HIGH:
                det = MultiTaskDetectorORT(join(folder, ort_cfg['det_model_path_640x']), input_size=(640, 640))
            else:
                raise NotImplemented  # �׳�δʵ���쳣

            rec = PPRCNNRecognitionORT(join(folder, ort_cfg['rec_model_path']), input_size=(48, 160))  # ��ʼ��ʶ����ģ��
            cls = ClassificationORT(join(folder, ort_cfg['cls_model_path']), input_size=(96, 96))  # ��ʼ��������ģ��

            # ��������ʶ��Ķ�����ܵ���������⡢ʶ��ͷ���
            self.pipeline = LPRMultiTaskPipeline(detector=det, recognizer=rec, classifier=cls, full_result=full_result)
        else:
            raise NotImplemented  # �׳�δʵ���쳣

    # ���÷��������ڶ�����ͼ����г���ʶ��
    def __call__(self, image: np.ndarray, *args, **kwargs):
        return self.pipeline(image)  # ����ʶ����
