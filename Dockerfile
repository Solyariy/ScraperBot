FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /saz_scraper

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/bin/sh" \
    --uid "1000" \
    appuser

RUN python -m venv /saz_scraper/.venv

ENV PATH="/saz_scraper/.venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /saz_scraper

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5050", "--reload"]