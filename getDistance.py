#import cv2
import math

# 단위 mm
# 초점거리 calibration으로 얻을 수 있음
fx = 550
fy = 550
# 높이
h = 750
# 카메라 각도
theta_tilt = -30

x=300
y=500

#cap = cv2.VideoCapture(0)

#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = 1980
height = 1080


cx = width/2
cy = height/2

u = (x-cx)/fx
v = (y-cy)/fy

print(u, v)

c_p_ = h * math.tan(math.radians(90+theta_tilt) - math.atan(v))
cp_ = math.sqrt(h*h+c_p_*c_p_)
print(cp_)
cp = math.sqrt(1+v*v)
pp_ = u*cp_/cp

d = math.sqrt(c_p_*c_p_ + pp_*pp_)
theta = -1*math.atan2(pp_,c_p_)
theta = math.degrees(theta)
print(theta)
