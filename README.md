### setup

1. install requirement from requirements.txt

    ```pip install -r requirement.txt```

2. download **deepdanbooru.onnx** and **tags.txt** from https://huggingface.co/chinoll/deepdanbooru/tree/main
and store in the root folder

3. run

    ```python server.py```

4. The API struction is

    ```
    HTTP METHOD: POST
    HTTP ADDRESS: http://localhost:12421/predict
    Content-Type: multipart/form-data;
    formdata: {
      filepath: "path/to/picture"
    }

    response data: {
        Content-Type: "application/json",
        data: {
            "tag1": weight as float,
            "tag2": weight as float
        }
    }
    ```