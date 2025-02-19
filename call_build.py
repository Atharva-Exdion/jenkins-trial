from app.API_SERVER.routers.dev_ops import DevOps  
import asyncio

# Create an instance and run the async method
asyncio.run(DevOps().docker_build_images(True, True, True, True, True))
