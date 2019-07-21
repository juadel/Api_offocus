# client for api
from skimage.filters import laplace
from scipy.ndimage import variance
import cv2
import pickle
import numpy as np
import socket  
import ipaddress
import pandas as pd
from skimage.color import rgb2gray
from skimage.restoration import estimate_sigma
from skimage.transform import resize
from tkinter import *
from tkinter import filedialog
import datetime
import sys
import os
from joblib import load