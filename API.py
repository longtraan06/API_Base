from fastapi import FastAPI, UploadFile, File
import json
import aiofiles
from fastapi.responses import StreamingResponse
import io
from convert_json_to_list import *


app = FastAPI()

# Endpoint nhận file JSONL, xử lý và trả về JSONL
@app.post("/process-jsonl/")
async def process_jsonl(file: UploadFile = File(...)):
    # Gọi hàm convert to list dict
    data_list = await convert_jsonl_to_dict(file) 

    #####################

    # trong đây là nơi đặt model sử lý data list
    # model này sẽ trả về một list_dict
    #####################
    
    processed_data = [{"processed": True, **record} for record in data_list] # ví dụ đây là file list dict kết qủa sau khi sử lý
    
    # Chuyển kết quả thành JSONL để trả về
    jsonl_content = "\n".join(json.dumps(record, ensure_ascii=False) for record in processed_data) # thay processed_data bằng list_dict kết quả
    return StreamingResponse(io.StringIO(jsonl_content), media_type="application/jsonl", headers={"Content-Disposition": "attachment; filename=output.jsonl"})

