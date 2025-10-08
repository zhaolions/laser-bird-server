"""
系统控制器 - 处理系统相关的 API 端点
"""

from datetime import datetime, timezone

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/v1/sys",
    tags=["System"],
)


class WelcomeReponse(BaseModel):
    """环境信息响应模型"""

    satus: str
    message: str
    timestamp: datetime
    version: str


@router.api_route("/", methods=["GET", "POST"], response_model=WelcomeReponse)
async def index():
    """index"""
    return WelcomeReponse(
        satus="success",
        message="Welcome to Laser Bird Server API!",
        timestamp=datetime.now(timezone.utc),
        version="0.1.0",
    )


