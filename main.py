import os
import base64
import re
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Barcode Ticket Generator")

if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

IMG_DIR = r"C:\Users\User\Desktop\yenri\codigos\tortuguita\imagenes"
PDF_DIR = r"C:\Users\User\Desktop\yenri\codigos\tortuguita\pdfs"


class TicketData(BaseModel):
    nombre: str
    sku: str
    png: str
    pdf: str


def sanitize(name, max_len=40):
    cleaned = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    return cleaned[:max_len]


@app.post("/api/save-ticket")
async def save_ticket(data: TicketData):
    os.makedirs(IMG_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)

    safe_name = sanitize(data.nombre)
    safe_sku = sanitize(data.sku)

    png_path = os.path.join(IMG_DIR, f"{safe_name}_{safe_sku}.png")
    pdf_path = os.path.join(PDF_DIR, f"{safe_name}_{safe_sku}.pdf")

    with open(png_path, "wb") as f:
        f.write(base64.b64decode(data.png))
    with open(pdf_path, "wb") as f:
        f.write(base64.b64decode(data.pdf))

    return {"ok": True, "png": png_path, "pdf": pdf_path}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8005))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
