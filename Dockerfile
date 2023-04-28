FROM debian:stable

WORKDIR /app

COPY . .

RUN apt -yq update

RUN apt -yq upgrade

RUN apt -yq install wget unzip curl python3-pip

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt install -yq ./google-chrome-stable_current_amd64.deb

RUN pip3 install -r requirement.txt

# RUN export chrome_driver="$(curl 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE')"

# RUN echo $chrome_driver

# RUN curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/${chrome_driver}/chromedriver_linux64.zip"

# RUN mkdir -p "chromedriver/stable"

# RUN unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable" 

# RUN chmod +x "chromedriver/stable/chromedriver"
