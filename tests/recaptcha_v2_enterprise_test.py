import pytest
from pydantic import ValidationError

from capmonster_python import RecaptchaV2EnterpriseTask


def test_min_score():
    task = RecaptchaV2EnterpriseTask(websiteURL="https://example.com", websiteKey="key", minScore=0.7)
    assert task.to_request()["minScore"] == 0.7


def test_min_score_omitted_by_default():
    task = RecaptchaV2EnterpriseTask(websiteURL="https://example.com", websiteKey="key")
    assert "minScore" not in task.to_request()


def test_min_score_range():
    with pytest.raises(ValidationError):
        RecaptchaV2EnterpriseTask(websiteURL="https://example.com", websiteKey="key", minScore=1.5)
