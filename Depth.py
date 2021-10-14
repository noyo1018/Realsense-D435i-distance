import cv2
import pyrealsense2
from realsense_depth import *
import pandas as pd

RESULT_NAME = "參佰"
DISTANCE_NAME = "300"

#產出CSV檔                
def OutputCSV():   
      
    Result ='D:\RealSense\Data\\' + RESULT_NAME + 'mm.csv'

    df_SAMPLE = pd.DataFrame.from_dict( df )
    df_SAMPLE.to_csv( Result  , index=False )
    
    print( '成功產出'+Result )


# Initialize Camera Intel Realsense

point = (250,250)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)
    print("Point:" + str(point))

dc = DepthCamera()

# Create mouse event
cv2.namedWindow("color frame")
cv2.setMouseCallback("color frame", show_distance)
counter = 0
col1 = []
col2 = []
trigger = False
while  not counter == 1000:
    
    ret, depth_frame, color_frame = dc.get_frame()

    # Show distance for a specific point
    

    cv2.circle(color_frame, point, 4, (0, 0, 255))


    distance = depth_frame[point[1], point[0]]
    
    if trigger:
        counter += 1
        col1.append(DISTANCE_NAME)
        col2.append(distance)

    print(distance)
    # print(distance)
    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("color frame",color_frame)
    key =cv2.waitKey(1)
    if key == ord('r'):
        print("==============================Start Record==================================\n\n\n\n\n")
        trigger = True

df = pd.DataFrame({"label":col1, "data": col2})
print(df)
OutputCSV()

