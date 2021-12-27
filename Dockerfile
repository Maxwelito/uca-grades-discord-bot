FROM python:3
RUN mkdir /opt/GradeChecker
WORKDIR /opt/GradeChecker
ADD . /opt/GradeChecker
RUN pip install -r requirements.txt
ENV USERNAME ''
ENV PASSWORD ''
ENV FORMATION ''
ENV TOKEN ''
CMD ["python3", "-u", "./main_bot.py"]