from ..emulator import Discipline
from typing import Any


def get_common(params: dict[str, Any]):
    return {
        key: params.get(key)
        for key in
        Discipline.model_fields.keys() & params.keys()
    }

def check(params: dict[str, Any]):
    if not (params.get("id") or (params.get("code") and params.get("specialty"))):
        raise ValueError("provide 'id' or ('code' and 'specialty') to update")
