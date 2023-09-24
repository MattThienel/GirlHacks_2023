import pygame.camera
import matplotlib
import matplotlib.pyplot as plt
import pickle
from tensorflow import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing import image
import numpy as np
from database import *
from datetime import datetime

pygame.camera.init()
camlist = pygame.camera.list_cameras()

cam = None

if camlist:
	cam = pygame.camera.Camera(camlist[0], (64,64))
	cam.start()

if cam:
	photo_image = cam.get_image()


db = Database("localhost", 6379, None)
current_time = None

model = keras.Sequential()
model.add(Convolution2D(32,(3,3),activation='relu', input_shape=(64,64,3))) #convolution layer
model.add(MaxPooling2D(pool_size=(2, 2))) #Maxpooling layer
model.add(Flatten()) #Flatten layer
model.add(Dense(400,activation='relu')) #Hidden Layer 1
model.add(Dense(200,activation='relu')) #Hidden Layer 2
model.add(Dense(6,activation='softmax')) #Output Layer
model.load_weights('Garbage.h5', False, True)#model.load('Garbage.h5')
#model = tf.keras.models.load_model('Garbage.h5')

#img = image.load_img('/content/dataset/Test/cardboard/cardboard398.jpg', target_size=(64,64))

if photo_image:
	current_time = datetime.now().strftime('%Y-%m-%d:%H-%M-%S')
	image_array = pygame.surfarray.array3d(photo_image)
	im = image_array[int((len(image_array)/2)-32):int((len(image_array)/2)+32),int((len(image_array[0])/2)-32):int((len(image_array[0])/2)+32),:]
	#im = image_array[int((len(image_array)/2)-64):int((len(image_array)/2)+64),int((len(image_array[0])/2)-64):int((len(image_array[0])/2)+64),:]
	serial_im = pickle.dumps(im)

	pygame.image.save(pygame.surfarray.make_surface(im), "photo.jpg")
	
	img = image.load_img('photo.jpg',target_size=(64,64))
	f = image.img_to_array(img)
	#f = image.img_to_array(im)
	f = np.expand_dims(f, axis=0) 
	#print(model.predict(f))
	#print(np.argmax(model.predict(f)))
	pred = np.argmax(model.predict(f))
	op = ['Cardboard','Glass','Metal','Paper','Plastic','Trash']
	print(op[pred])
	
	db.addTrashEntry(current_time, op[pred], f'model.predict(f)[0][pred]', serial_im)

#print(db.getKeys())
entries = db.getTrashEntries(current_time.encode('UTF-8'))

pygame.init()
X = 64
Y = 64
#print(bytearray(current_time.encode('UTF-8')))
#db_image = pickle.loads(entries[current_time.encode('UTF-8')][b'photo'])
db_image = pickle.loads(entries[b'photo'])

scrn = pygame.display.set_mode((X,Y))
pygame.display.set_caption('image')
scrn.blit(pygame.surfarray.make_surface(db_image), (0,0))

pygame.display.flip()
status = True
while(status):
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			status = False

pygame.quit()


		
