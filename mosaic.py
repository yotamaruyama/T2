{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "def mosaic(img, rect, size):\n",
    "    # モザイクをかける領域を取得\n",
    "    (x1, y1, x2, y2) = rect\n",
    "    w = x2 - x1\n",
    "    h = y2 - y1\n",
    "    i_rect = img[y1:y2, x1:x2]\n",
    "    # モザイク処理のため一度縮小して拡大する\n",
    "    i_small = cv2.resize(i_rect, ( size, size))\n",
    "    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)\n",
    "    # 画像にモザイク画像を重ねる\n",
    "    img2 = img.copy()\n",
    "    img2[y1:y2, x1:x2] = i_mos\n",
    "    return img2\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
