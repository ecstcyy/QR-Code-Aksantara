  import pyzbar.pyzbar as pyzbar
  import cv2

  # input dir
  im = 'image.jpg'

  # main program
  objArray = pyzbar.decode(cv2.imread(im))
  info = objArray[0].data
  print('Decoded Data :', str(info.decode('utf-8')), '\n')