from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    origins = [
        "http://localhost:3000",  # URL de tu frontend en desarrollo
        "http://192.168.20.17:8000",# Otra URL o IP permitida en la red local
        "http://localhost:3001",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
