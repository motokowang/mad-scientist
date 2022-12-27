from fastapi import FastAPI
from thing1.database import Base


def create_app() -> FastAPI:
    
    app = FastAPI()

    # class Student(BaseModel):
    #     student_id: int
    #     age: int
    #     name: str


    @app.get('/')
    async def root():
        return {'message': 'hello world'}


    @app.get('/student')
    async def student():
        # メタ.connect()
        return {'message': 'student'}
    
    
    return app
    

app = create_app()