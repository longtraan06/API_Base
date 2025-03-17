from fastapi import UploadFile
import json
import aiofiles

async def convert_json_to_dict(file: UploadFile):

    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    async with aiofiles.open(file.filename, 'r', encoding='utf-8') as f:
        data = dict(f)
    
    return data