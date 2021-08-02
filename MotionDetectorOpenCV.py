import cv2, time, pandas
from datetime import datetime
first_frame = None
statu_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start" , "End"])
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    statu = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue
    statu = 1
    detla_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(detla_frame, 30 , 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None , iterations= 0)
    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 100:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame , (x,y) , (x+w , y+h), (0,255,0),3)
    statu_list.append(statu)
    statu_list = statu_list[-2:]

    if statu_list[-1] == 1 and statu_list[-2] ==0:
        times.append(datetime.now())
    if statu_list[-1] == 0 and statu_list[-2] ==1:
        times.append(datetime.now())

    cv2.imshow("FRAME" , frame)
    cv2.imshow("GRAY", gray)
    cv2.imshow("Delta" ,detla_frame)
    cv2.imshow("thresh",thresh_delta)
    print(statu_list)
    print(times)
    # for i in range(0, len(times), 2):
    #     df = df.append({"Start" : times[i], "End": times[i+1], ignore_index=True})
    # df.to_csv("Times.csv")
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import cv2, time
# video = cv2.VideoCapture(0)
# first_frame = None
# while True:
#     check, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (21,21), 0)
#     if first_frame is None:
#         first_frame = gray
#         continue
#     delta_frame = cv2.absdiff(first_frame, gray)
#     thresshold_frame = cv2.threshold(delta_frame, 30 , 255, cv2.THRESH_BINARY) [1]
#     thresshold_frame = cv2.dilate(thresshold_frame, None , iterations= 1)

#     (cntr,_) = cv2.findContours(thresshold_frame.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
#     for contour in cntr:
#         if cv2.contourArea(contour) < 500:
#             continue
#         (x,y,w,h) = cv2.boundingRect(contour)
#         cv2.rectangle(frame, (x,y) , (x+w , y+h) , (0,255,0), 3)

#     cv2.imshow("FRAME", frame)
#     key = cv2.waitKey(1)
#     if key == ord(" "):
#         break
# video.release()
# cv2.destroyAllWindows()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""