import asyncio
from time import sleep
from typing import Optional

from httpx import Response, AsyncClient, Client

from .exceptions import CapmonsterAPIException, CapmonsterException
from .methods import GetBalancePayload, GetTaskResultPayload, CreateTaskPayload
from .tasks.task import TaskPayload


class CapmonsterClient:
    __BASE_URL = "https://api.capmonster.cloud"
    __BALANCE_URL = "/getBalance"
    __TASK_RESULT_URL = "/getTaskResult"
    __CREATE_TASK_URL = "/createTask"
    __MAX_RETRY = 120
    __PER_RETRY_DELAY = 1

    def __init__(self, api_key: str, timeout: Optional[float] = 30.0) -> None:
        self.api_key = api_key
        self.__async_client = AsyncClient(timeout=timeout, base_url=self.__BASE_URL)
        self.__sync_client = Client(timeout=timeout, base_url=self.__BASE_URL)

    def get_balance(self) -> float:
        """
        Fetches the current balance using the provided API key.

        Raises:
            This method may raise exceptions if the HTTP request fails or the JSON response
            format is unexpected. These exceptions are not handled within the method.

        Returns:
            float: The balance fetched from the external service. Defaults to 0.0 if the balance
            key is not found in the response.
        """
        payload = GetBalancePayload(clientKey=self.api_key).model_dump()
        response = self.__make_sync_request(self.__BALANCE_URL, payload).json()
        return response.get("balance", 0.0)

    async def get_balance_async(self) -> float:
        """
        Asynchronously fetches the current balance using the provided API key.

        Raises:
            This method may raise exceptions if the HTTP request fails or the JSON response
            format is unexpected. These exceptions are not handled within the method.

        Returns:
            float: The balance fetched from the external service. Defaults to 0.0 if the balance
            key is not found in the response.
        """
        payload = GetBalancePayload(clientKey=self.api_key).model_dump()
        response = await self.__make_async_request(self.__BALANCE_URL, payload)
        return response.json().get("balance", 0.0)

    def create_task(self, task: TaskPayload, callback_url: Optional[str] = None) -> int:
        """
        Creates a task based on the provided payload and returns the task ID.

        This method is responsible for initiating a task by preparing the request with the
        provided task details and optional callback URL, sending a synchronous request to the
        task creation endpoint, and parsing the response to retrieve the task ID.

        Args:
            task: The task configuration payload that defines the specifics of the task to be
                created.
            callback_url: An optional URL to be called back upon task completion or update.

        Returns:
            The unique identifier of the created task.

        Raises:
            CapmonsterException: If the task creation request fails or the response is not contains valid task id.
        """
        payload = CreateTaskPayload(clientKey=self.api_key, task=task, callbackUrl=callback_url).model_dump(
            exclude_none=True)
        payload["softId"] = 30
        response = self.__make_sync_request(self.__CREATE_TASK_URL, payload).json()
        return response.get("taskId", 0)

    async def create_task_async(self, task: TaskPayload, callback_url: Optional[str] = None) -> int:
        """
        Asynchronously creates a task based on the provided payload and returns the task ID.

        This method is responsible for initiating a task by preparing the request with the
        provided task details and optional callback URL, sending a synchronous request to the
        task creation endpoint, and parsing the response to retrieve the task ID.

        Args:
            task: The task configuration payload that defines the specifics of the task to be
                created.
            callback_url: An optional URL to be called back upon task completion or update.

        Returns:
            The unique identifier of the created task.

        Raises:
            CapmonsterException: If the task creation request fails or the response is not contains valid task id.
        """
        payload = CreateTaskPayload(clientKey=self.api_key, task=task, callbackUrl=callback_url).model_dump(
            exclude_none=True)
        payload["softId"] = 30
        request = await self.__make_async_request(self.__CREATE_TASK_URL, payload)
        response = request.json()
        return response.get("taskId", 0)

    def get_task_result(self, task_id: int) -> dict:
        """
        Fetches the result of a specific task by its identifier.

        This function interacts with API to retrieve the results of a
        previously submitted task. The function uses the provided task ID and
        sends a request to the API endpoint to get the result. It returns the
        solution data extracted from the API response or an empty dictionary if
        no solution data is found.

        Args:
            task_id (int): An integer representing the unique identifier of the task.

        Returns:
            dict: A dictionary containing the solution data retrieved from the task
            result API endpoint. If the solution is not found in the response, an empty
            dictionary is returned.
        """
        payload = GetTaskResultPayload(clientKey=self.api_key, taskId=task_id).model_dump()
        response = self.__make_sync_request(self.__TASK_RESULT_URL, payload).json()
        return response.get("solution", {})

    async def get_task_result_async(self, task_id: int) -> dict:
        """
        Asynchronously fetches the result of a specific task by its identifier.

        This function interacts with API to retrieve the results of a
        previously submitted task. The function uses the provided task ID and
        sends a request to the API endpoint to get the result. It returns the
        solution data extracted from the API response or an empty dictionary if
        no solution data is found.

        Args:
            task_id (int): An integer representing the unique identifier of the task.

        Returns:
            dict: A dictionary containing the solution data retrieved from the task
            result API endpoint. If the solution is not found in the response, an empty
            dictionary is returned.
        """
        payload = GetTaskResultPayload(clientKey=self.api_key, taskId=task_id).model_dump()
        request = await self.__make_async_request(self.__TASK_RESULT_URL, payload)
        response = request.json()
        return response.get("solution", {})

    def join_task_result(self, task_id: int) -> dict:
        """
        Joins and retrieves the result of a task given its ID, retrying a specified number
        of times if the result is not immediately available.

        Args:
            task_id: The identifier of the task for which the result needs to be retrieved.

        Returns:
            dict:
                The result of the task if successfully retrieved within the maximum retries.

        Raises:
            CapmonsterException:
                If the maximum retry limit is exceeded without obtaining the task result.
        """
        for _ in range(0, self.__MAX_RETRY + 1):
            result = self.get_task_result(task_id)
            if result:
                return result
            elif not result:
                sleep(self.__PER_RETRY_DELAY)
        raise CapmonsterAPIException(
            61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    async def join_task_result_async(self, task_id: int):
        """
        Asynchronously joins and retrieves the result of a task given its ID, retrying a specified number
        of times if the result is not immediately available.

        Args:
            task_id:  The identifier of the task for which the result needs to be retrieved.

        Returns:
            dict:
                The result of the task if successfully retrieved within the maximum retries.

        Raises:
            CapmonsterException:
                If the maximum retry limit is exceeded without obtaining the task result.
        """
        for _ in range(0, self.__MAX_RETRY + 1):
            result = await self.get_task_result_async(task_id)
            if result:
                return result
            elif not result:
                await asyncio.sleep(self.__PER_RETRY_DELAY)
        raise CapmonsterAPIException(
            61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    def __make_sync_request(self, url: str, payload: dict) -> Response:
        try:
            response = self.__sync_client.post(url, json=payload)
            return self.__check_response(response)
        except Exception as e:
            raise CapmonsterException(-1, type(e).__name__, str(e))

    async def __make_async_request(self, url: str, payload: dict) -> Response:
        try:
            post = await self.__async_client.post(url, json=payload)
            return self.__check_response(post)
        except Exception as e:
            raise CapmonsterException(-1, type(e).__name__, str(e))

    @staticmethod
    def __is_ready(response: dict):
        status = response.get("status")
        if status == "processing":
            return False
        elif status == "ready":
            return True
        else:
            raise CapmonsterAPIException(error_id=-1,
                                         error_code="CAPMONSTER_API_ERROR",
                                         error_description="Sometimes can be happen if Capmonster "
                                                           "servers there is too much intensity")

    @staticmethod
    def __check_response(data: Response) -> Response:
        response = data.json()
        if type(response) is dict:
            if response.get("errorId", 0) != 0:
                raise CapmonsterAPIException(
                    response.get("errorId"),
                    response.get("errorCode", response.get("errorCode", "UNKNOWN_ERROR")),
                    response.get("errorDescription", response.get("errorDescription", "Unknown error"))
                )
            return data
        else:
            raise CapmonsterAPIException(error_id=-1,
                                         error_code="CAPMONSTER_API_ERROR",
                                         error_description="Sometimes can be happen if Capmonster "
                                                           "servers there is too much intensity")
