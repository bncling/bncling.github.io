import os 
import shutil

SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2025/Math 1232/Syllabus/1232_Syllabus_Summer_25.pdf"
WEB_SYLLABUS_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/1232-summer-25/GW1232_summer_25_syllabus.pdf"

CV_PATH = "/Users/benclingenpeel/Desktop/CV/Current/Ben_Clingenpeel_CV.pdf"
WEB_CV_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents"

#NOTES_PATH = "/Users/benclingenpeel/Desktop/GW/Summer 2024/1231/Notes/to_upload.pdf"
#WEB_NOTES_PATH = "/Users/benclingenpeel/Desktop/Projects/bncl/assets/documents/1231_summer_24_notes.pdf"

# copy things over
shutil.copy(SYLLABUS_PATH, WEB_SYLLABUS_PATH)
shutil.copy(CV_PATH, WEB_CV_PATH)
#shutil.copy(NOTES_PATH, WEB_NOTES_PATH)


print("Successfully updated files!")

