import cv2
import numpy as np
from math import cos,sin,pi,atan2

h = 480
w = 640


def draw_joint(img, p):
    p = tuple(p.astype(int))
    color = (0,0,255)
    radius1 = 18
    radius2 = 6

    cv2.circle(img, p, radius1, color)
    cv2.circle(img, p, radius2, color)

def draw_link(img, pa, pb):
    pa = tuple(pa.astype(int))
    pb = tuple(pb.astype(int))
    color = (0,0,255)
    
    cv2.line(img, pa, pb, color)

def rot(t, p1):
    c = cos(t)
    s = sin(t)
    xnew = p1[0] * c - p1[1] * s
    ynew = p1[0] * s + p1[1] * c
    return (xnew, ynew)

def draw_ee(img, pa, pb):
    color = (0,0,255)
    t = ( pa - pb )
    t = atan2(t[1], t[0])
    r = 18
    r2 = 10
    p1 = [0, r]
    p2 = [0, -r]
    p1 = rot(t, p1) + pb
    p2 = rot(t, p2) + pb
    p1 = tuple(p1.astype(int))
    p2 = tuple(p2.astype(int))
    cv2.line(img, p1, p2, color)
    p1a = [-r2, r]
    p2a = [-r2, -r]
    p1a = rot(t, p1a) + pb
    p2a = rot(t, p2a) + pb
    p1a = tuple(p1a.astype(int))
    p2a = tuple(p2a.astype(int))
    cv2.line(img, p1, p1a, color)
    cv2.line(img, p2, p2a, color)
    

t1 = 0.0
t2 = 0.0

p0 = np.array([w//2, h//2])
l1 = 100
l2 = 100

def draw(joint_angles):
    [t1, t2] = joint_angles
    img = np.zeros((h,w,3), np.uint8)

    p1 = p0 + l1*np.array([ sin(t1), cos(t1) ])
    p2 = p1 + l2*np.array([ sin(t2), cos(t2) ])

    draw_joint(img, p0 )
    draw_link(img, p0, p1 )
    draw_joint(img, p1 )
    draw_link(img, p1, p2 )
    draw_ee(img, p1, p2 )

    cv2.imshow("x", img)
    cv2.waitKey(100)

    t1+=0.1
    t2+=0.3