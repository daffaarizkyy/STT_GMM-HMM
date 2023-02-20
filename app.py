from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from werkzeug.utils import secure_filename
import librosa
from scipy.io import wavfile
from sklearn.mixture import GaussianMixture
import soundfile
import os
import IPython
from python_speech_features import mfcc
from hmmlearn import hmm
from scipy.io import wavfile

class HMMTrainer(object):
   def __init__(self, model_name='GaussianHMM', n_components=4):
     self.model_name = model_name
     self.n_components = n_components
     self.model=hmm.GaussianHMM(n_components=4)
     self.models = []
     
   def train(self, X):
       self.models.append(self.model.fit(X))
   def get_score(self, input_data):
       return self.model.score(input_data)

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.wav']

@app.route('/')
def index():
	return(render_template('about.html'))

@app.route('/prediction')
def upload_page():
    return render_template('index.html')

@app.route("/prediction", methods=['POST'])
def main():
	if request.method == 'POST':
		global name
		uploaded_file = request.files['file']
		name = filename = secure_filename(uploaded_file.filename)
		file_ext = os.path.splitext(filename)[1]
		if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
			message = 'Format File Not Allowed !'
			return render_template('index.html', message=message)
		uploaded_file.save(os.path.join("./static/uploads/", filename))
		arch = request.form.get('arch')
		if(arch=="gmm"):
			result = kenali_suara_gmm("./static/uploads/"+filename)
		elif(arch=="hmm"):
			result = kenali_suara_hmm("./static/uploads/"+filename)
		#os.remove("./static/uploads/"+filename)
		return render_template('index.html', result=result, name=filename)
	else:
		return ("Unsupported Request Method")

@app.route('/deletefile')
def delete_file():
	try:
		check_file = "./static/uploads"
		filename_wav = f"{os.path.join(check_file, name)}"
		os.remove(filename_wav)
	except Exception as e:
		return(render_template(e))
	finally:
		return(render_template('delete_file.html'))

@app.route('/prediction')
def kenali_suara_gmm(input_file):
	benar=0
	if(cekfile(input_file)):
		audio_signal, sampling_rate = soundfile.read(input_file)
		# MFCC configuration:
		N_MFCC = 20
		N_MELS = 60 
		WINDOW_LENGTH = int(0.025 * sampling_rate)  # To obtain 25 ms window
		HOP_LENGTH = int(0.010 * sampling_rate)  # 10 ms shift between consecutive windows
		mfcc_features = librosa.feature.mfcc(audio_signal, sr=sampling_rate, n_mfcc=20, n_mels=60, n_fft=int(0.025 * sampling_rate), hop_length=int(0.010 * sampling_rate),).T
		
		#Feature Normalization
		mfcc_features -= np.mean(mfcc_features, axis=0)
		mfcc_features /= np.std(mfcc_features, ddof=0, axis=0)
		
		predict = request.form.get('predict')
		if(predict=="word"):
			modelfile = open('./model/modelgmmLinguaLibre.pkl', 'rb')

		elif(predict=="digit"):
			modelfile = open('./model/modelgmmDigit.pkl', 'rb')

		elif(predict=="fruit"):
			modelfile = open('./model/modelgmmfruit.pkl', 'rb')

		else:
			return ("Unsupported Prediction Selected")
		
		# Scoring a test recording agaist all digit-specific GMMs
		gmms = pickle.load(modelfile)
		scores=[]
		for item in gmms:
			gmm, label = item          
			score = gmm.score(mfcc_features)         
			scores.append(score)            
			index=np.array(scores).argmax()
			result = gmms[index][1]
		return result
		
	else:
		return ("Not Available")

@app.route('/prediction')
def kenali_suara_hmm(input_file):
	if(cekfile(input_file)):
		sampling_freq, audio = wavfile.read(input_file)
		mfcc_features = mfcc(audio, sampling_freq)
		scores=[]
		
		predict = request.form.get('predict')
		if(predict=="word"):
			modelfile = open('./model/modelhmm15.pkl', 'rb')
			modelhmm = pickle.load(modelfile)
		
			for item in modelhmm:
				hmm_model, label = item
				score=float('-inf')
				try:
					score = hmm_model.get_score(mfcc_features)
				finally:
					scores.append(score)
					index=np.array(scores).argmax()
					return(modelhmm[index][1][1:])

		elif(predict=="digit"):
			modelfile = open('./model/modelhmm9.pkl', 'rb')

		elif(predict=="fruit"):
			modelfile = open('./model/modelhmm14.pkl', 'rb')

		else:
			return ("Unsupported Prediction Selected")
		
		modelhmm = pickle.load(modelfile)
		
		for item in modelhmm:
		  hmm_model, label = item
		  score = hmm_model.get_score(mfcc_features)
		  scores.append(score)
		  index=np.array(scores).argmax()
		return(modelhmm[index][1])
	else:
		return ("Not Available")

def cekfile(input_file):
	return(input_file.endswith('wav'))

if __name__ == '__main__':
	app.run(port=5000, debug=True)
	
