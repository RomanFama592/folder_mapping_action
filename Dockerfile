FROM python:3.9.18-alpine3.18

WORKDIR /folder_mapping

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install --root-user-action=ignore -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "/folder_mapping/index.py"]