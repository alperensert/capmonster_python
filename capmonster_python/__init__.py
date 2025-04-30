from .client import CapmonsterClient
from .tasks.basilisk import BasiliskTask
from .tasks.binance import BinanceTask
from .tasks.complex_image_recaptcha import ComplexImageRecaptchaTask, ComplexImageRecaptchaMetadata
from .tasks.complex_image_recognition import ComplexImageRecognitionTask
from .tasks.datadome import DataDomeTask, DataDomeMetadata
from .tasks.geetest import GeeTestV4Task, GeeTestV3Task
from .tasks.image_to_text import ImageToTextTask
from .tasks.imperva import ImpervaTask, ImpervaTaskMetadata
from .tasks.prosopo import ProsopoTask
from .tasks.recaptcha_v2 import RecaptchaV2Task
from .tasks.recaptcha_v2_enterprise import RecaptchaV2EnterpriseTask
from .tasks.recaptcha_v3 import RecaptchaV3Task
from .tasks.temu import TemuTask
from .tasks.tendi import TenDITask
from .tasks.turnstile import TurnstileTask, TurnstileCloudFlareTask
