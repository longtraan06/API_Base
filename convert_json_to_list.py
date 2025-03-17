from fastapi import UploadFile
import json
import aiofiles

async def convert_jsonl_to_dict(file: UploadFile):
    data_list = []
    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    async with aiofiles.open(file.filename, 'r', encoding='utf-8') as f:
        async for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            data_list.append(record)
    
    return data_list