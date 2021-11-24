FROM python:3.9.7
RUN apt-get update && apt-get install -y python3-pip

WORKDIR /usr/src/app

# Install requirements
RUN pip install --user poetry
ENV PATH="${PATH}:/home/user/.local/bin"
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# This is a little optimization to avoid downloading the same image twice
# Docker will cache the image and check each command against the image
# So, if we change our source code, we only have to run this next step. However,
# if we change our requirements, we have to run all steps after it again.
# Including the pip install, which takes a long time.
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
