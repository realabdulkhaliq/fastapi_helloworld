# FastAPI HelloWorld Project

1.  Create an New project
    ```
    poetry new fastapi_helloworld
    ```
2.  Add FastAPI and Uvicorn Server

    ```
    poetry add fastapi "uvicorn[standard]"
    ```

3.  Run Uvicorn Server

    ```
    poetry run uvicorn fastapi_helloworld.main:app --reload
    ```

4.  Ctrl + Click on Generated URL

5.  FastApi DOCS

    ```
    http://127.0.0.1:8000/docs
    ```

    _It is the documentation of all routes_

6.  Pytest

    ```
    poetry add pytest
    ```

7.  Run Pytest

    ```
    poetry run pytest
    ```

    _You can also use -v flag_

        poetry run pytest -v

8.  Project paths
    ```
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/piaic/
    http://127.0.0.1:8000/docs/
    http://127.0.0.1:8000/openapi.json
    ```
