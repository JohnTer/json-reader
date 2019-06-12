FROM python:3.6.8-stretch
ADD parser/ /
ADD parser/*.py /parser/
ADD parser/*.txt /parser/
ADD parser/data /parser/data
ADD parser/structs /parser/structs
ADD parser/out /parser/out
WORKDIR /parser
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["./main.py"]



