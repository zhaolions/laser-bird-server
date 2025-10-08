"""
FastAPI 主应用

激光驱鸟器服务端 API
"""

from fastapi import FastAPI

from laser_bird_server.controller import sys_controller

app = FastAPI(
    title="激光驱鸟器API",
    description="激光驱鸟器服务端 API",
    version="0.1.0",
)

app.include_router(sys_controller.router)

if __name__ == "__main__":
    import uvicorn

    # 开发模式运行
    uvicorn.run(
        "laser_bird_server.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
