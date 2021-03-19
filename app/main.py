import uvicorn
from fastapi import FastAPI, Path, Query, HTTPException
from starlette.responses import JSONResponse
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from database.mongodb import MongoDB
from config.development import config
from model.room import createRoomsModel, updateRoomsModel

mongo_config = config["mongo_config"]
mongo_db = MongoDB(
    mongo_config["host"],
    mongo_config["port"],
    mongo_config["user"],
    mongo_config["password"],
    mongo_config["auth_db"],
    mongo_config["db"],
    mongo_config["collection"],
)
mongo_db._connect()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return JSONResponse(content={"message": "rooms Info"}, status_code=200)


@app.get("/rooms/")
def get_rooms(
    sort_by: Optional[str] = None,
    order: Optional[str] = Query(None, min_length=3, max_length=4),
):

    try:
        result = mongo_db.find(order, sort_by)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong !!")

    return JSONResponse(
        content={"status": "OK", "data": result},
        status_code=200,
    )


@app.get("/rooms/{rooms_id}")
def get_rooms_by_id(rooms_id: str = Path(None, min_length=10, max_length=10)):
    print("bank")
    try:
        result = mongo_db.find_one(rooms_id)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong !!")

    if result is None:
        raise HTTPException(status_code=404, detail="Room Id not found !!")

    return JSONResponse(
        content={"status": "OK", "data": result},
        status_code=200,
    )


@app.post("/rooms")
def create(rooms: createRoomsModel):
    print(rooms)
    print("bank")
    try:
        rooms_id = mongo_db.create(rooms)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong !!")

    return JSONResponse(
        content={
            "status": "ok",
            "data": {
                "rooms_id": rooms_id,
            },
        },
        status_code=201,
    )


@app.patch("/rooms/{rooms_id}")
def update_rooms(
    rooms: updateRoomsModel,
    rooms_id: str = Path(None, min_length=10, max_length=10),
):
    print("rooms", rooms)
    try:
        updated_rooms_id, modified_count = mongo_db.update(rooms_id, rooms)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong !!")

    if modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail=f"rooms Id: {updated_rooms_id} is not update want fields",
        )

    return JSONResponse(
        content={
            "status": "ok",
            "data": {
                "rooms_id": updated_rooms_id,
                "modified_count": modified_count,
            },
        },
        status_code=200,
    )


@app.delete("/rooms/{rooms_id}")
def delete_rooms_by_id(rooms_id: str = Path(None, min_length=10, max_length=10)):
    try:
        deleted_rooms_id, rooms_count = mongo_db.delete(rooms_id)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong !!")

    if rooms_count == 0:
        raise HTTPException(
            status_code=404, detail=f"rooms Id: {deleted_rooms_id} is  Deleted"
        )

    return JSONResponse(
        content={
            "status": "ok",
            "data": {
                "rooms_id": deleted_rooms_id,
                "deleted_count": rooms_count,
            },
        },
        status_code=200,
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=True)
