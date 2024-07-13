# -*- coding:  utf-8 -*-
"""
created on Thu July 11 05:22 2024

@author: https://github.com/BilalAhmad096

@project: Handwritten Text Extraction
"""

from src.handwritten_text_extraction import handwritten_text_extraction

if __name__ == "__main__":
    # img_path = 'D:/Programming/GitHub/Handwritten-Text-Extraction/data/test.png'
    img_path = './data/javed.jpg'
    handwritten_text_extraction(img_path)