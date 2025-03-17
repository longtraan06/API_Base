from fastapi import FastAPI, UploadFile, File
import json
import aiofiles
from fastapi.responses import JSONResponse


app = FastAPI()

# Endpoint nhận file JSONL, xử lý và trả về JSONL
@app.post("/process-json/")
async def process_json(file: UploadFile = File(...)):
    # Đọc file JSON
    async with aiofiles.open(file.filename, "r", encoding="utf-8") as f:
        content = await f.read()
    
    data_dict = json.loads(content) # convert file json sang dict

    #####################

    # trong đây là nơi đặt model sử lý data list
    # model này sẽ trả về một dict
    processed_data = [{"processed": True, **data_dict}] # ví dụ đây là file list dict kết qủa sau khi sử lý

    #####################
    
    
    # Chuyển kết quả thành JSONL để trả về
    return JSONResponse(content=processed_data, media_type="application/json") # thay processed_data = data từ model
