./darknet detect cfg/yolov3.cfg yolov3.weights $1
python crop.py $1
