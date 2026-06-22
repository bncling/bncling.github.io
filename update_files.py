import os 
import shutil

SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2026/Syllabus/1232_Syllabus_Summer_26.pdf"
WEB_SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/1232-summer-26/GW1232_summer_26_syllabus.pdf"

CV_PATH = "/Users/benclingenpeel/Desktop/CV/Current/Ben_Clingenpeel_CV.pdf"
WEB_CV_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents"

NOTES_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2026/Lecture notes"
WEB_NOTES_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/1232-summer-26/lecture-notes"

# copy things over
shutil.copy(SYLLABUS_PATH, WEB_SYLLABUS_PATH)
shutil.copy(CV_PATH, WEB_CV_PATH)
shutil.copytree(NOTES_PATH, WEB_NOTES_PATH, dirs_exist_ok = True)


print("Successfully updated files!")

