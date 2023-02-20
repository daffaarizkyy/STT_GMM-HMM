# Speech-to-Text using Gaussian Mixture Model & Hidden Markov Model
![Logo](static/img/text-to-speech.png)
> Speech-to-Text is a technology that can convert voice data into text data. This allows computers to understand human language through voice commands. We combine machine learning technology into Speech-to-Text, namely the Gaussian Mixture Model and the Hidden Markov Model to identify sounds in text.

> Live Demo Now is [_UNAVAILABLE_](). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [Description] (#speech-to-text-using-gaussian-mixture-model-&-hidden-markov-model)
* [General Info](#general-information)  
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Speech-to-Text is a technology that can convert voice data into text data. This allows computers to understand human language through voice commands. We combine machine learning technology into Speech-to-Text, namely the Gaussian Mixture Model and the Hidden Markov Model to identify sounds in text.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Flask==2.2.2
- hmmlearn==0.2.8
- ipython==8.10.0
- librosa==0.9.2
- numpy==1.23.5
- PySoundFile==0.9.0.post1
- python_speech_features==0.6
- scikit_learn==1.2.1
- scipy==1.10.0
- soundfile==0.11.0
- Werkzeug==2.2.2



## Features
- Easy to Use
- Able to perform speech recognition and convert to text automatically

## Lacks
- For now only supports English Language & File Format .wav


## Screenshots
![Example screenshot](/static/img/screenshot/about.png)
![Example screenshot](/static/img/screenshot/prediction.png)
![Example screenshot](/static/img/screenshot/prediction_2.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
The `requirements.txt` file should list all Python libraries that needed for this project.
This library will be installed using:

```
pip install -r requirements.txt
```

## Usage
Type on your CMD or Terminal :

- Clone this Repository

```
git clone https://github.com/daffaarizkyy/STT_GMM-HMM
```

- cd to your directory (on where's you clone this project)

For Example:

  ```
  cd STT_GMM-HMM
  ```

- Run `pip install -r requirements.txt`

- And Run `python app.py`

- Open your browser and enter `localhost:5000` or `http://127.0.0.1:5000/`


## Project Status
Project is: _complete_


## Room for Improvement

Room for improvement:
- The Speech Recognition Processing needs to be improved so that the processing is more faster

To do for future development:
- Added more supported languages and file formats


## Acknowledgements
- This project was inspired by Youtube Closed Captions and Many Films with Subtitle.

Many thanks to:

- Irvan Kurniawan : Modelling HMM
  Sriwijaya University, Majoring in Informatics Engineering

- Muhammad Daffa Rizky Fatarah : Modelling GMM and UI/UX Designer
  Sriwijaya University, Majoring in Informatics Engineering


## Contact
Created by [@Wibu x Nolep](https://www.unsri.ac.id/) - feel free to contact us!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->