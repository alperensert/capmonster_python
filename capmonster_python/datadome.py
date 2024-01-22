from .capmonster import UserAgent


class DataDomeTask(UserAgent):
    def __init__(self, client_key):
        super(DataDomeTask, self).__init__(client_key)

    def create_task(self, website_url: str, metadata: object):
        data = {
            "client_key": self._client_key,
            "task": {
                "type": "CustomTask",
                "class": "DataDome",
                "websiteURL": website_url,
                "metadata": metadata,
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        return self._make_request("createTask", data=data).get("taskId")
