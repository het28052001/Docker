from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the route path as a variable
USERS_ROUTE = '/users/'

class UserDetails(BaseModel):
    user_name: str

@app.post(USERS_ROUTE)
async def user_func(user: UserDetails):
    if not user.user_name:
        raise HTTPException(status_code=400, detail="User name is missing")
    
    return {'status': 'Success', 'message': f'Hi! Welcome to fx datalabs {user.user_name}'}