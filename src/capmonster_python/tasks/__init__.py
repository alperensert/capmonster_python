from .altcha import AltchaTask, AltchaMetadata
from .amazon import AmazonTask
from .basilisk import BasiliskTask
from .binance import BinanceTask
from .castle import CastleTask, CastleMetadata
from .complex_image_recaptcha import ComplexImageRecaptchaTask, ComplexImageRecaptchaMetadata
from .complex_image_recognition import ComplexImageRecognitionTask
from .datadome import DataDomeTask, DataDomeMetadata
from .funcaptcha import FunCaptchaTask
from .geetest import GeeTestV4Task, GeeTestV3Task
from .image_to_text import ImageToTextTask
from .imperva import ImpervaTask, ImpervaTaskMetadata
from .mtcaptcha import MTCaptchaTask
from .prosopo import ProsopoTask
from .recaptcha_v2 import RecaptchaV2Task
from .recaptcha_v2_enterprise import RecaptchaV2EnterpriseTask
from .recaptcha_v3 import RecaptchaV3Task
from .recaptcha_v3_enterprise import RecaptchaV3EnterpriseTask
from .task import VanillaTaskPayload, ProxyPayload, UserAgentPayload
from .temu import TemuTask
from .tendi import TenDITask
from .tspd import TSPDTask, TSPDMetadata
from .turnstile import TurnstileTask, TurnstileCloudFlareTask, TurnstileWaitingRoomTask
from .yidun import YidunTask

__all__ = [
    "VanillaTaskPayload",
    "ProxyPayload",
    "UserAgentPayload",
    "AltchaTask",
    "AltchaMetadata",
    "AmazonTask",
    "BasiliskTask",
    "BinanceTask",
    "CastleTask",
    "CastleMetadata",
    "ComplexImageRecaptchaTask",
    "ComplexImageRecaptchaMetadata",
    "ComplexImageRecognitionTask",
    "DataDomeTask",
    "DataDomeMetadata",
    "FunCaptchaTask",
    "GeeTestV3Task",
    "GeeTestV4Task",
    "ImageToTextTask",
    "ImpervaTask",
    "ImpervaTaskMetadata",
    "MTCaptchaTask",
    "ProsopoTask",
    "RecaptchaV2Task",
    "RecaptchaV2EnterpriseTask",
    "RecaptchaV3Task",
    "RecaptchaV3EnterpriseTask",
    "TemuTask",
    "TenDITask",
    "TSPDTask",
    "TSPDMetadata",
    "TurnstileTask",
    "TurnstileCloudFlareTask",
    "TurnstileWaitingRoomTask",
    "YidunTask"
]
