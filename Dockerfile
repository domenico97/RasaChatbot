FROM tensorflow/tensorflow:2.2.0
RUN mkdir -p /rasa_app
WORKDIR /rasa_app
COPY . /rasa_app
RUN python -m pip install -U pip
RUN pip install -U spacy
#RUN pip install -r requirements.txt
#RUN pip3 install --user rasa-nlu==0.14.0
#RUN pip3 install --user rasa-core==0.13.2
RUN pip install numpy
RUN pip install pandas
RUN pip install gunicorn
RUN pip install --user -U nltk
RUN python -m spacy download en
RUN pip install --user rasa==2.8.2
RUN pip install --user sanic==19.9.0
RUN pip install Flask
RUN pip install -U scikit-learn
RUN pip install tornado

