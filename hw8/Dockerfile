FROM python:3.11

WORKDIR /code

COPY . .

RUN python -m venv /venv
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/venv/bin:$PATH"

RUN chmod +x ./scripts/launch.sh

EXPOSE 8000

ENTRYPOINT ["sh", "./scripts/launch.sh"]