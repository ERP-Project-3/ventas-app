# PowerShell script para iniciar backend y frontend

Start-Process powershell -ArgumentList "cd backend; .\env\Scripts\Activate.ps1; uvicorn app.main:app --reload"
Start-Process powershell -ArgumentList "cd frontend; npm run dev"
