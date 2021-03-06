FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install streamlit
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
