# fastapi_helloworld

1. Create an New project
   ```
   poetry new fastapi_helloworld
   ```
2. Add FastAPI and Uvicorn Server

   ```
   poetry add fastapi "uvicorn[standard]"
   ```
3. Run Unicorn Server

   ```
   poetry run uvicorn fastapi_helloworld.main:app --reload
   ```
