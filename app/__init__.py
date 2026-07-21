from app.errors import register_error_handlers

def create_app():
    # ... inicializações do db, blueprint, flasgger ...
    
    register_error_handlers(app)
    
    return app