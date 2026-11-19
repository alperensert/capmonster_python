import warnings


def warn_deprecated(message: str, stacklevel: int = 3) -> None:
    """
    Emits a DeprecationWarning pointing at the caller's code.

    Args:
        message: What is deprecated and what to use instead.
        stacklevel: How many frames up the warning should point to.
    """
    warnings.warn(message, DeprecationWarning, stacklevel=stacklevel)


def warn_proxy_required(task: str, stacklevel: int = 3) -> None:
    """
    Emits a UserWarning when a task that the API documents as proxy-only is created without a proxy.

    Args:
        task: Name of the task class.
        stacklevel: How many frames up the warning should point to.
    """
    warnings.warn(f"{task}: CapMonster Cloud requires your own proxy for this task; "
                  f"the request will likely be rejected without one.", UserWarning, stacklevel=stacklevel)
